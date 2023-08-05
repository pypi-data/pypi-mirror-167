# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spliced.logger import logger

from .base import Prediction, get_prefix, match_by_prefix, time_run_decorator


class SymbolsPrediction(Prediction):
    def predict(self, splice, predict_type=None):
        """
        Run symbolator to add to the predictions
        """
        if predict_type == "diff":
            return self.diff_libs(splice)
        if splice.different_libs:
            return self.splice_different_libs(splice)
        return self.splice_equivalent_libs(splice)

    def splice_different_libs(self, splice):
        """
        This is subbing in a library with a version of itself, and requires binaries
        """
        raise NotImplementedError

    def diff_libs(self, splice):
        """
        Only do A vs B comparisons between two libs.
        """
        original_deps = self.create_elfcall_deps_lookup(splice, splice.original)
        spliced_deps = self.create_elfcall_deps_lookup(splice, splice.spliced)

        # Create a set of predictions for top level binary without considering
        # level of a dependency (binary-checks-*) and each spliced binary / lib combination
        predictions = []

        for libA, metaA in original_deps.items():
            for libB, metaB in spliced_deps.items():
                libA_fullpath = metaA["lib"]
                libB_fullpath = metaB["lib"]

                libA_symbols = splice.metadata[libA_fullpath]
                libB_symbols = splice.metadata[libB_fullpath]

                # Case 4: missing previously found symbols (abicompat)
                predictions.append(
                    diff_missing_symbols(libA, libB, libA_symbols, libB_symbols)
                )
                predictions.append(
                    diff_missing_exports(libA, libB, libA_symbols, libB_symbols)
                )

        if predictions:
            splice.predictions["symbols"] = predictions

    def splice_equivalent_libs(self, splice):
        """
        This is subbing in a library with a version of itself, and requires binaries
        """
        # For each original (we assume working) binary, find its deps from elfcall,
        # and then match to the equivalent lib (via basename) for the splice
        original_deps = self.create_elfcall_deps_lookup(splice, splice.original)
        spliced_deps = self.create_elfcall_deps_lookup(splice, splice.spliced)

        # Create a set of predictions for top level binary without considering
        # level of a dependency (binary-checks-*) and each spliced binary / lib combination
        predictions = []

        for binary, meta in original_deps.items():

            # Match the binary to the spliced one
            if binary not in spliced_deps:
                logger.warning(
                    f"{binary} is missing from splice! This should not happen!"
                )
                continue

            # Compare spliced and binary symbols
            binary_fullpath = meta["lib"]
            binary_symbols = splice.metadata[binary_fullpath]

            # Case 1: any missing symbols in original (so we cannot continue)
            if binary_symbols["missing"]:
                predictions.append(
                    {
                        "binary": binary_fullpath,
                        "splice_type": "same_lib",
                        "is_stripped_binary": binary_symbols.get(
                            "is_stripped", "Unknown"
                        ),
                        "command": "binary-checks-loader-missing-symbols-for-original",
                        "message": "Loader found missing symbols for original binary: %s"
                        % "\n".join(binary_symbols["missing"]),
                        "prediction": False,
                    }
                )
                continue

            # Case 2: Symbol provisioner change (or symbol entirely missing)
            spliced_meta = spliced_deps[binary]
            spliced_fullpath = spliced_meta["lib"]
            spliced_symbols = splice.metadata[spliced_fullpath]

            predictions.append(
                check_symbol_provisioner_change(splice, meta, spliced_meta)
            )

            # We must find a matching lib for each based on prefix
            matches = match_by_prefix(meta["deps"], spliced_meta["deps"])

            # If we don't have matches, nothing to look at
            if not matches:
                continue

            # Also cache the lib (original or after splice) if we don't have it yet
            for match in matches:

                # Case 4: missing previously found symbols (abicompat)
                predictions.append(
                    missing_previously_found_symbols(
                        binary_fullpath, binary_symbols, spliced_symbols, match
                    )
                )

                # Case 3: Look at exported symbols of the spliced in and compare with exported of the original
                # Any new missing exports (may not fail binary of interest but could fail something else)
                # abidiff case. We can only run this case for direct dependencies
                original_key = "original:" + match["original"]
                spliced_key = "spliced:" + match["spliced"]
                if (
                    original_key not in splice.metadata
                    or spliced_key not in splice.metadata
                ):
                    continue
                predictions.append(
                    missing_previously_found_exports(
                        binary_fullpath,
                        match,
                        splice.metadata[original_key],
                        splice.metadata[spliced_key],
                    )
                )

        if predictions:
            splice.predictions["symbols"] = predictions


@time_run_decorator
def diff_missing_exports(libA, libB, libA_symbols, libB_symbols):
    """
    If exports changed between an original and spliced, it won't work in different contexts
    """
    if not libA_symbols or not libB_symbols:
        # It is predicted to work if we don't have any missing symbols
        return {
            "splice_type": "different_lib",
            "original_lib": libA,
            "spliced_lib": libB,
            "command": "missing-previously-found-exports",
            "message": "Cannot derive decision, symbols not found.",
            "prediction": "Unknown",
        }

    # Want to find symbols in main binary for this dependency of interest
    before = [s for s, _ in libA_symbols["exported"].items()]
    after = [s for s, _ in libB_symbols["exported"].items()]

    # We cannot be missing symbols in original (before) that aren't in spliced (after)
    missing_symbols = [x for x in before if x not in after]

    print("Missing %s" % missing_symbols)

    # It is predicted to work if we don't have any missing symbols
    return {
        "splice_type": "different_lib",
        "original_lib": libA,
        "spliced_lib": libB,
        "is_stripped_original": libA_symbols.get("is_stripped", "Unknown"),
        "is_stripped_splice": libB_symbols.get("is_stripped", "Unknown"),
        "command": "missing-previously-found-exports",
        "message": missing_symbols,
        "prediction": not missing_symbols,
    }


@time_run_decorator
def missing_previously_found_exports(binary, match, original_symbols, spliced_symbols):
    """
    If exports changed between an original and spliced, it won't work in different contexts
    """
    # Want to find symbols in main binary for this dependency of interest
    before = [s for s, _ in original_symbols["exported"].items()]
    after = [s for s, _ in spliced_symbols["exported"].items()]

    # We cannot be missing symbols in original (before) that aren't in spliced (after)
    missing_symbols = [x for x in before if x not in after]

    # It is predicted to work if we don't have any missing symbols
    return {
        "binary": binary,
        "splice_type": "same_lib",
        "original_lib": match["original"],
        "spliced_lib": match["spliced"],
        "is_stripped_original": original_symbols.get("is_stripped", "Unknown"),
        "is_stripped_splice": spliced_symbols.get("is_stripped", "Unknown"),
        "command": "missing-previously-found-exports",
        "message": missing_symbols,
        "prediction": not missing_symbols,
    }


@time_run_decorator
def diff_missing_symbols(libA, libB, libA_symbols, libB_symbols):
    """
    A previously found (and thus needed) symbol cannot be missing after the splice.
    """
    if not libA_symbols or not libB_symbols:
        # It is predicted to work if we don't have any missing symbols
        return {
            "splice_type": "different_lib",
            "original_lib": libA,
            "spliced_lib": libB,
            "command": "missing-previously-found-symbols",
            "message": "Cannot derive decision, symbols not found.",
            "prediction": "Unknown",
        }

    # Want to find symbols in main binary for this dependency of interest
    before = set(
        list(libA_symbols.get("exported", {}).keys())
        + list(libA_symbols.get("imported", {}).keys())
    )
    after = set(
        list(libB_symbols.get("exported", {}).keys())
        + list(libB_symbols.get("imported", {}).keys())
    )
    # We cannot be missing symbols in original (before) that aren't in spliced (after)
    missing_symbols = [x for x in before if x not in after]

    print("Missing %s" % missing_symbols)

    # It is predicted to work if we don't have any missing symbols
    return {
        "splice_type": "different_lib",
        "original_lib": libA,
        "spliced_lib": libB,
        "is_stripped_original": libA_symbols.get("is_stripped", "Unknown"),
        "is_stripped_splice": libB_symbols.get("is_stripped", "Unknown"),
        "command": "missing-previously-found-symbols",
        "message": missing_symbols,
        "prediction": not missing_symbols,
    }


@time_run_decorator
def missing_previously_found_symbols(binary, original_symbols, spliced_symbols, match):
    """
    A previously found (and thus needed) symbol cannot be missing after the splice.
    """
    # Want to find symbols in main binary for this dependency of interest
    before = [
        s
        for s, x in original_symbols["found"].items()
        if "lib" in x and x["lib"]["realpath"] == match["original"]
    ]
    after = [
        s
        for s, x in spliced_symbols["found"].items()
        if "lib" in x and x["lib"]["realpath"] == match["spliced"]
    ]

    # We cannot be missing symbols in original (before) that aren't in spliced (after)
    missing_symbols = [x for x in before if x not in after]

    # It is predicted to work if we don't have any missing symbols
    return {
        "binary": binary,
        "splice_type": "same_lib",
        "original_lib": match["original"],
        "spliced_lib": match["spliced"],
        "is_stripped_original": original_symbols.get("is_stripped", "Unknown"),
        "is_stripped_splice": spliced_symbols.get("is_stripped", "Unknown"),
        "command": "missing-previously-found-symbols",
        "message": missing_symbols,
        "prediction": not missing_symbols,
    }


@time_run_decorator
def check_symbol_provisioner_change(splice, meta, spliced_meta):
    """
    Compared an original and spliced binary/lib and determind if a symbol provisioner changes
    """
    binary_fullpath = meta["lib"]
    spliced_fullpath = spliced_meta["lib"]
    binary_symbols = splice.metadata[binary_fullpath]
    spliced_symbols = splice.metadata[spliced_fullpath]

    # Case 2: Get symbol names and prefixes for each of original and spliced
    # If spliced has a symbol name from a different prefix, that's a problem.
    # E.g both swig and pcre-v1 have common dependency (A in libfoo.so)
    # and changing the dependency means that we cut off a piece of the tree with
    # the symbol we needed.
    # symbol provisioner change
    # symbol X changed from being provided by A to now provided by B
    original_symbols = compress_symbol_set(binary_symbols["found"])
    spliced_symbols = compress_symbol_set(spliced_symbols["found"])
    changed = []
    for symbol, prefix in original_symbols.items():
        if symbol not in spliced_symbols:
            changed.append("symbol {symbol} is missing in splice")
            continue
        if spliced_symbols[symbol] != prefix:
            changed.append(
                f"symbol {symbol} was originally provided by {prefix}, after splice is provided by {spliced_symbols[symbol]}"
            )

    # It is predicted to work if we don't have any changed
    return {
        "binary": binary_fullpath,
        "splice_type": "same_lib",
        "is_stripped_binary": binary_symbols.get("is_stripped", "Unknown"),
        "is_stripped_splice": spliced_symbols.get("is_stripped", "Unknown"),
        "command": "binary-checks-symbol-provisioner-change",
        "message": "Symbol provider changes: %s" % "\n".join(changed),
        "prediction": not changed,
    }


def compress_symbol_set(symbols):
    """
    Write symbol:prefix into set to compare to.
    """
    compressed = {}
    for symbol, m in symbols.items():
        if "lib" not in m:
            continue
        compressed[symbol] = get_prefix(m["lib"]["realpath"])
    return compressed
