#!/usr/bin/env python3

import argparse
from pathlib import Path

from ruamel.yaml import YAML


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('section', help='Add packages to this section within the manifest')
    parser.add_argument('package', nargs='+', help='Name of the package(s) to add')
    parser.add_argument('--filename', help='Path to the manifest', default='package_manifest.yaml')

    args = parser.parse_args()

    manifest_path = Path(args.filename)

    yaml = YAML(typ='rt')
    yaml.default_flow_style = False
    yaml.explicit_start = True
    yaml.preserve_quotes = True
    yaml.width = 1024
    yaml.indent(sequence=4, offset=2)

    try:
        manifest = yaml.load(manifest_path.read_text())
    except FileNotFoundError:
        raise parser.error(f'Manifest {manifest_path} was not found')

    try:
        hosts = manifest[args.section]['hosts']
    except KeyError:
        raise parser.error(f'Section {args.section} was not found')

    for package in args.package:
        if package not in hosts:
            for i, host in enumerate(hosts.keys()):
                if package < host:
                    hosts.insert(i, package, {})
                    break
            else:
                hosts[package] = {}

    with manifest_path.open('w') as manifest_fp:
        yaml.dump(manifest, manifest_fp)


if __name__ == '__main__':
    main()
