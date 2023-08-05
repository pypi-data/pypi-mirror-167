# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re
import shutil
import tempfile
from time import time

import spliced.utils as utils
from spliced.logger import logger
from spliced.predict.base import Prediction

from .smeagle import SmeagleRunner


class SmeaglePrediction(Prediction):
    def predict(self, splice, predict_type=None):
        """
        Run smeagle to add to the predictions
        # Testing command:
        # spliced splice --package swig@3.0.8 --splice pcre --runner spack --replace pcre --experiment experiment

        1. splice is going to have libraries found and symbols and imported missing
        2. If any imported missing, record splice fail (we need all the symbols)
        3. Get list of associated paths from elfcall, generate facts for each
          - try to mamke cache based on the library fullpath
        4. After facts are generated, spliced->smeagle runner should:
          - generate asp facts for main lib/binary for all symbols in the union set across dependencies
          - for each dependency, only genderate asp facts for the symbols that come from it
        5. An entirely new ASP model that compares A (the single binary/lib) to B (symbols across deps)
           If no splice libs OR no tools, cut out early
        """
        # Smeagle makes predictions from the spliced libs only
        if not splice.spliced:
            return

        # If we have defined a cache, use it
        self.cache_dir = os.environ.get(
            "SPLICED_SMEAGLE_CACHE_DIR",
            os.path.join(tempfile.gettempdir(), "spliced-cache"),
        )
        logger.info("Smeagle cache directory is %s" % self.cache_dir)

        # default do not cleanup cache
        cleanup = False
        if self.cache_dir and not os.path.exists(self.cache_dir):
            utils.mkdir_p(self.cache_dir)

        # ...unless it's a temporary one!
        elif not self.cache_dir:
            self.cache_dir = utils.tempdir()
            cleanup = True

        # Create a smeagle runner!
        self.smeagle = SmeagleRunner()

        # Prepare to add predictions to splice
        splice.predictions["smeagle"] = []

        if predict_type == "diff":
            self.run_stability_tests(splice)
        else:
            self.run_compatibility_tests(splice)

        if cleanup and os.path.exists(self.cache_dir):
            shutil.rmtree(self.cache_dir)

    def run_compatibility_tests(self, splice):
        """
        Run the original full compatibility tests.
        """
        # Keep subset of spliced libs->data we can generate facts for
        spliced = {}

        # For each spliced binary/lib, generate facts, save to cache
        for lib in splice.spliced:
            cache_key = self.generate_smeagle_data(lib, prefix="smeagle")
            if cache_key:
                spliced[lib] = cache_key

        # For each library/binary we can test, make predictions
        for lib, facts_path in spliced.items():
            self.compatibility_test_lib(splice, lib, facts_path)

    def run_stability_tests(self, splice):
        for libA in splice.original:
            for libB in splice.spliced:
                self.stability_test_lib(splice, libA, libB)

    def stability_test_lib(self, splice, libA, libB):
        """
        A stability test can only look at the subset of symbols.
        """
        libs = [os.path.basename(libA), os.path.basename(libB)]
        libs.sort()
        libs_uid = "-".join(libs)
        splice.stats[libs_uid] = {}

        # Look for dependency in facts cache
        libA_cache = self.generate_smeagle_data(libA, prefix="smeagle")
        libB_cache = self.generate_smeagle_data(libB, prefix="smeagle")

        # If we can't generate facts, we can't include in model
        if not libA_cache or not libB_cache:
            splice.predictions["smeagle"].append(
                {
                    "return_code": -1,
                    "original_lib": libA,
                    "lib": libB,
                    "prediction": False,
                    "message": "One or both of libraries failed to generate Smeagle facts.",
                }
            )
            return

        # Write to output so we can have examples
        lib_a_dir = os.path.dirname(libA_cache)
        output_asp = os.path.join(lib_a_dir, libs_uid + ".asp")
        out = open(output_asp, "w")

        # Stability test compares A (the main library) against B
        t1 = time()
        res = self.smeagle.stability_test(
            libA, libB, data1=libA_cache, data2=libB_cache, out=out
        )
        t2 = time()
        res["seconds"] = t2 - t1
        splice.predictions["smeagle"].append(res)
        out.close()

    def check_missing_symbols(self, splice, lib):
        """
        Ensure no missing symbols as determined by elfcall off the bat.
        """
        # If any symbols missing, fail fast - the model couldn't work
        if splice.metadata[lib]["missing"]:
            splice.predictions["smeagle"].append(
                {
                    "return_code": -1,
                    "lib": lib,
                    "prediction": False,
                    "data": splice.metadata[lib]["missing"],
                    "message": "Library is missing symbols, so smeagle model would fail.",
                }
            )
            return True
        return False

    def compatibility_test_lib(self, splice, lib, facts_path):
        """
        Given an initial library (lib) that we have facts (facts_path) for, use the
        splice lookup to derive the exact dependency libraries (and set of symbols)
        that are needed. IF a dependency library fails to generate facts, we simply
        don't include its symbols. We do this so we can still make a prediction on
        imperfect information.
        """
        if self.check_missing_symbols(lib):
            return

        # Keep stats for the splice and lib
        splice.stats[lib] = {}

        # Keep lookup of library -> symbols for facts for it, and all symbols
        symbols = set()
        deps = {}

        # If we get here we aren't missing symbols!
        for symbol, meta in splice.metadata[lib]["found"].items():
            dep = meta["lib"]["realpath"]

            # If the dep is a system lib, for the time being we cannot include
            # The reason is because no Dwarf == no symbols == no go.
            if re.search("^(/usr|/lib)", dep):
                continue

            # Look for dependency in facts cache
            cache_key = self.generate_smeagle_data(dep)

            # If we can't generate facts, we can't include in model
            if not cache_key:
                continue

            # At this point we only care about path to facts, what our model needs
            if cache_key not in deps:
                deps[cache_key] = set()
            symbols.add(symbol)
            deps[cache_key].add(symbol)

        splice.stats[lib]["total_matched_symbols"] = len(symbols)

        # Now we need to create a lookup with a set of symbols for each lib
        # Since we have this for deps, we just add our main library (A)
        # And note we are adding paths to FACTS we don't care about lib paths
        # by this point!
        B_set = list(deps.keys())
        deps[facts_path] = symbols

        # Write to output so we can have examples
        output_asp = facts_path.replace(".json", ".asp")
        out = open(output_asp, "w")

        # Stability test compares A (the main library) against all deps, B
        # Time how long it takes
        t1 = time()
        res = self.smeagle.compatible_test(facts_path, B_set, deps, out=out)
        t2 = time()
        res["seconds"] = t2 - t1
        splice.predictions["smeagle"].append(res)
        out.close()

    def generate_smeagle_data(self, lib, prefix="smeagle"):
        """
        Given a library, run smeagle to generate facts and save to cache. Return key.
        """
        # Keep same path, but under cache
        if prefix:
            cache_key = os.path.join(
                self.cache_dir, "%s-%s.json" % (prefix, lib.strip(os.sep))
            )
        else:
            cache_key = os.path.join(self.cache_dir, lib.strip(os.sep) + ".json")
        if os.path.exists(cache_key):
            return cache_key
        logger.info("Generating facts for %s with smeagle..." % lib)
        data = self.smeagle.get_smeagle_data(lib)
        if "data" in data and data["data"] and data["return_code"] == 0:
            cache_dir = os.path.dirname(cache_key)
            utils.mkdir_p(cache_dir)
            utils.write_json(data["data"], cache_key)
            return cache_key
        else:
            logger.warning(
                "Cannot generate facts for %s, will not be included in experiment."
                % lib
            )
