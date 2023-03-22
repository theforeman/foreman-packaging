#!/usr/bin/env python3

import argparse
import bz2
import json
import lzma
import requests
import sqlite3
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

from packaging.version import Version
from list_updatable_packages import Spec

DISTS = ['el8']
COMPONENTS = [path.name for path in Path('packages/').glob('*')]
NIGHTLY_PACKAGES = ['foreman', 'foreman-installer', 'foreman-proxy', 'foreman-release', 'foreman-selinux', 'rubygem-hammer_cli', 'rubygem-hammer_cli_foreman', 'rubygem-katello', 'katello-repos', 'rubygem-hammer_cli_katello', 'katello']
EXCLUDE_PACKAGES = [
    'jsoncpp',  # build-time only dependency according to https://github.com/theforeman/foreman-packaging/pull/6229
]


def get_repo_packages(component, release='nightly', dist='el8', arch='x86_64', staging=False):
    packages = defaultdict(lambda: '0')
    if staging:
        if component == 'plugins':
            component = 'foreman-plugins'
        elif component == 'client':
            component = 'foreman-client'
        if component == 'katello':
            repo_url = f'http://koji.katello.org/releases/yum/{component}-{release}/{component}/{dist}/{arch}/'
        else:
            repo_url = f'http://koji.katello.org/releases/yum/{component}-{release}/{dist}/{arch}/'
    else:
        if component == 'foreman':
            component = 'releases'
        if component == 'katello':
            repo_url = f'https://yum.theforeman.org/{component}/{release}/{component}/{dist}/{arch}/'
        else:
            repo_url = f'https://yum.theforeman.org/{component}/{release}/{dist}/{arch}/'
    r = requests.get(f'{repo_url}/repodata/repomd.xml')
    repomd = ET.fromstring(r.content)

    sqlite_location = repomd.find('.//*[@type="primary_db"]/{http://linux.duke.edu/metadata/repo}location').get('href')
    sqlite_url = f'{repo_url}/{sqlite_location}'
    if sqlite_url.endswith('.xz'):
        decompress = lzma.decompress
    elif sqlite_url.endswith('.bz2'):
        decompress = bz2.decompress
    else:
        raise ValueError(sqlite_url)

    s = requests.get(sqlite_url)

    with tempfile.NamedTemporaryFile() as sqlitefile:
        sqlitefile.write(decompress(s.content))
        sqlitefile.flush()
        primarydb = sqlite3.connect(sqlitefile.name)
        primarydb.row_factory = sqlite3.Row
        cur = primarydb.cursor()
        cur.execute("select distinct rpm_sourcerpm,version from packages;")
        for row in cur:
            source = row['rpm_sourcerpm'].replace(f'.{dist}.src.rpm', '')
            (package, _version, _release) = source.rsplit('-', 2)
            version = row['version']
            if release == 'nightly' and package in NIGHTLY_PACKAGES:
                continue
            if package in EXCLUDE_PACKAGES:
                continue
            if Version(packages[package]) < Version(version):
                packages[package] = version
        primarydb.close()

    return set(packages.items())


def get_git_packages(component, release='nightly'):
    package_specs = [Spec(s) for s in Path(f'packages/{component}').glob('**/*.spec')]
    packages = set()
    for spec in package_specs:
        if release == 'nightly' and spec.is_nightly:
            continue
        if spec.package_name in EXCLUDE_PACKAGES:
            continue
        packages.add((str(spec.package_name), str(spec.version)))
    return packages


def get_release_from_git_branch(default='nightly'):
    release = default
    git_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], encoding='utf-8').strip()
    if git_branch.startswith('rpm/'):
        release = git_branch.replace('rpm/', '')
        if release == 'develop':
            release = 'nightly'
    return release


def main():
    default_release = get_release_from_git_branch()
    parser = argparse.ArgumentParser(description='compare git and rpm repo')
    parser.add_argument('--release', default=default_release, help='release to compare for (default: %(default)s)')
    parser.add_argument('--staging', action='store_true', help='check staging repository')
    parser.add_argument('--json', action='store_true', help='JSON output')
    args = parser.parse_args()
    result = {}
    for component in COMPONENTS:
        git_packages = get_git_packages(component, release=args.release)
        repo_packages = get_repo_packages(component, release=args.release, staging=args.staging)
        result[component] = {'repo_only': list(repo_packages-git_packages), 'git_only': list(git_packages-repo_packages)}
    if args.json:
        print(json.dumps(result))
    else:
        for component, data in result.items():
            print(component)
            print("In repo but not in git:")
            print(data['repo_only'])
            print("In git but not in repo:")
            print(data['git_only'])


if __name__ == '__main__':
    main()
