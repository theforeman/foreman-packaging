#!/usr/bin/env python3

import argparse
import requests
from collections import defaultdict
from itertools import chain
from pathlib import Path
from debian.changelog import Changelog
from debian.deb822 import Packages
from debian.debian_support import NativeVersion

DISTS = [path.name for path in Path('debian/').glob('*')]
PLUGINS = ['plugins']
NIGHTLY_PACKAGES = ['foreman', 'foreman-installer', 'foreman-proxy']


def get_repo_packages(dist, release='nightly', arch='amd64', staging=False):
    packages = defaultdict(lambda: '0')
    if staging and dist != 'plugins':
        repo_url = f'https://stagingdeb.theforeman.org/dists/{dist}/theforeman-{release}/binary-{arch}/Packages'
    else:
        repo_url = f'https://deb.theforeman.org/dists/{dist}/{release}/binary-{arch}/Packages'
    remote_packages = requests.get(repo_url)
    for pkg in Packages.iter_paragraphs(remote_packages.text, use_apt_pkg=False):
        source = pkg.get('Source', pkg['Package'])
        version = pkg['Version']
        if version.startswith('9999-') and release == 'nightly' and source in NIGHTLY_PACKAGES:
            continue
        if NativeVersion(packages[source]) < NativeVersion(version):
            packages[source] = version
    return set(packages.items())


def get_git_packages(dist, release='nightly'):
    if dist == 'plugins':
        package_changelogs = Path('plugins/').glob('**/changelog')
    else:
        package_changelogs = chain(Path('debian/').glob(f'{dist}/**/changelog'), Path('dependencies/').glob(f'{dist}/**/changelog'))
    packages = set()
    for package_changelog in package_changelogs:
        with package_changelog.open() as debchangelog:
            changelog = Changelog(debchangelog)
            if release == 'nightly' and changelog.package in NIGHTLY_PACKAGES:
                continue
            packages.add((str(changelog.package), str(changelog.version)))
    return packages


def print_diff(dist, repo_packages, git_packages):
    print(dist)
    print("In repo but not in git:")
    print(repo_packages - git_packages)
    print("In git but not in repo:")
    print(git_packages - repo_packages)


def main():
    parser = argparse.ArgumentParser(description='compare git and debian repo')
    parser.add_argument('--release', default='nightly', help='release to compare for (default: %(default)s)')
    parser.add_argument('--staging', action='store_true', help='check staging repository')
    args = parser.parse_args()
    for dist in DISTS + PLUGINS:
        packages = get_git_packages(dist, release=args.release)
        repo_packages = get_repo_packages(dist, release=args.release, staging=args.staging)
        print_diff(dist, repo_packages, packages)


if __name__ == '__main__':
    main()
