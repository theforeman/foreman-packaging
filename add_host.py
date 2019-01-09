#!/usr/bin/env python3

import click
from ruamel.yaml import YAML


@click.command()
@click.argument('section', nargs=1)
@click.argument('packages', nargs=-1)
@click.option('--filename', help='Path to the manifest', default='package_manifest.yaml',
              type=click.Path(exists=True, dir_okay=False, writable=True))
def cli(section, packages, filename):
    yaml = YAML(typ='rt')
    yaml.default_flow_style = False
    yaml.explicit_start = True
    yaml.preserve_quotes = True
    yaml.indent(sequence=4, offset=2)

    with open(filename) as manifest_fp:
        manifest = yaml.load(manifest_fp)

    try:
        hosts = manifest[section]['hosts']
    except KeyError:
        raise click.ClickException('Section {} not found'.format(section))

    for package in packages:
        if package not in hosts:
            for i, host in enumerate(hosts.keys()):
                if package < host:
                    hosts.insert(i, package, {})
                    break
            else:
                hosts[package] = {}

    with open(filename, 'w') as manifest_fp:
        yaml.dump(manifest, manifest_fp)


if __name__ == '__main__':
    cli()  # pylint: disable=no-value-for-parameter
