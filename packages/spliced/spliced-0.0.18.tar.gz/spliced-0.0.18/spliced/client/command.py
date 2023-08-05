# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import json
import random
import sys

import requests

import spliced.experiment
import spliced.utils as utils


def matrix(args, parser, extra, subparser):
    """
    Upper level function for generating an experiment matrix
    """
    # Generate a base experiment
    experiment = spliced.experiment.Experiment()
    experiment.load(args.config_yaml)

    if args.generator == "spack":
        generate_spack_matrix(args, experiment)
    elif args.generator == "manual":
        raise NotImplementedError


def command(args, parser, extra, subparser):
    """
    Generate command list
    """
    # Generate a base experiment
    experiment = spliced.experiment.Experiment()
    experiment.load(args.config_yaml)

    if args.generator == "spack":
        generate_spack_commands(args, experiment)
    elif args.generator == "manual":
        raise NotImplementedError


def get_package_versions(package):
    """
    Given a spack package, get a list of all versions
    """
    versions = requests.get(
        "https://raw.githubusercontent.com/spack/packages/main/data/packages/%s.json"
        % package
    )
    if versions.status_code != 200:
        sys.exit("Failed to get package versions")
    versions = versions.json()
    return list(
        set(
            [
                x["name"]
                for x in versions["versions"]
                if x.get("deprecated", False) == False
            ]
        )
    )


def get_compiler_labels(container):
    """
    Given a container URI, get all associated compiler labels (if they exist)
    """
    # If we have a container, get compilers. Otherwise default to "all"
    labels = ["all"]

    if container:
        response = requests.get("https://crane.ggcr.dev/config/%s" % container)
        if response.status_code != 200:
            sys.exit(
                "Issue retrieving image config for % container: %s"
                % (container, response.reason)
            )

        config = response.json()
        labels = config["config"].get("Labels", {}).get("org.spack.compilers")
        labels = [x for x in labels.strip("|").split("|") if x]
    return labels


def get_splice_versions(experiment):
    """
    Get splice versions
    """
    # Do we have splice versions? If not, the only splice is the splice
    splice_versions = [experiment.splice]
    if experiment.splice_versions:
        splice_versions = set()
        for version in experiment.splice_versions:
            splice_versions.add("%s@%s" % (experiment.splice, version))
        splice_versions = list(splice_versions)
    return splice_versions


def generate_spack_commands(args, experiment):
    """
    Generate a list of spliced commands
    """
    # These are package versions - splice versions come from list in config
    versions = get_package_versions(experiment.package)
    splice_versions = get_splice_versions(experiment)
    func = "splice" if not args.diff else "diff"

    commands = []
    # Generate list of commands
    for version in versions:

        for splice_version in splice_versions:

            # versioned package
            package = "%s@%s" % (experiment.package, version)
            cmd = (
                "spliced %s --package %s --splice %s --runner spack --replace %s --experiment %s"
                % (
                    func,
                    package,
                    splice_version,
                    experiment.replace,
                    experiment.name,
                )
            )
            commands.append(cmd)

    # flatten to be printable
    commands = "\n".join(commands)

    if args.outfile:
        utils.write_file(commands, args.outfile)
    else:
        print(commands)


def generate_spack_matrix(args, experiment):
    """
    A spack matrix derives versions from spack, and prepares
    to generate commands (and metadata) to support a spack splice
    experiment
    """
    versions = get_package_versions(experiment.package)
    splice_versions = get_splice_versions(experiment)
    func = "splice" if not args.diff else "diff"

    # We will build up a matrix of container and associated compilers
    matrix = []

    # Generate list of commands
    for version in versions:

        for splice_version in splice_versions:

            # versioned package
            package = "%s@%s" % (experiment.package, version)
            cmd = (
                "spliced %s --package %s --splice %s --runner spack --replace %s --experiment %s"
                % (
                    func,
                    package,
                    splice_version,
                    experiment.replace,
                    experiment.name,
                )
            )
            matrix.append(
                {
                    "command": cmd,
                    "package": package,
                    "runner": "spack",
                    "splice": experiment.splice,
                    "replace": experiment.replace,
                    "experiment": experiment.name,
                    "container": args.container,
                }
            )

    # We can only get up to 256 max - select randomly
    if args.limit != 0 and len(matrix) >= args.limit:
        print(
            "Warning: original output is length %s and limit is set to %s jobs!"
            % (len(matrix), args.limit)
        )
        matrix = random.sample(matrix, args.limit)

    if args.outfile:
        utils.write_json(matrix, args.outfile)
    else:
        print(json.dumps(matrix, indent=4))
    print("::set-output name=matrix::%s\n" % json.dumps(matrix))
    print('echo "matrix=%s" >> $GITHUB_ENV' % json.dumps(matrix))
