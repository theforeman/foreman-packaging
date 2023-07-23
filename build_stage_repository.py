#!/usr/bin/env python3

from subprocess import check_output, STDOUT, CalledProcessError
import os
import yaml
import glob
import shutil
import time
import hashlib
import sys


def move_rpms_from_copr_to_stage(collection, version, src_folder, dest_folder, source=False):
    if source:
        print(f"Moving {collection} Source RPMs from Copr directory to stage repository")
    else:
        print(f"Moving {collection} RPMs from Copr directory to stage repository")

    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)

    repo_folder = f"{src_folder}/el8-{collection}-{version}"

    if source:
        files = glob.glob(repo_folder + f"/**/*.src.rpm")
    else:
        files = glob.glob(repo_folder + f"/**/*.rpm")

    for file in files:
        file_name = os.path.basename(file)
        shutil.move(file, os.path.join(dest_folder, file_name))

    shutil.rmtree(src_folder)


def modulemd_yaml(collection):
    return f"modulemd/modulemd-{collection}-el8.yaml"


def generate_modulemd_version(version):
    if version == 'nightly':
        modulemd_version_prefix = '9999'
    else:
        major, minor = version.split('.')
        modulemd_version_prefix = int(major)*100 + int(minor)

    modulemd_version_string = time.strftime(f"{modulemd_version_prefix}%Y%m%d%H%M%S", time.gmtime())

    return int(modulemd_version_string)


def generate_modulemd_context(collection, version):
    context_string = f"{collection}-{version}"
    digest = hashlib.sha256(context_string.encode()).hexdigest()
    return digest[:8]


def create_modulemd(collection, version, stage_dir):
    print("Adding modulemd to stage repository")
    cmd = [
        'rpm',
        '--nosignature',
        '--query',
        '--package',
        f"{stage_dir}/*.rpm",
        "--queryformat=%{name}-%{epochnum}:%{version}-%{release}.%{arch}\n"
    ]
    output = check_output(cmd)

    with open(modulemd_yaml(collection), 'r') as file:
        modules = yaml.safe_load(file)

    modules['data']['artifacts'] = {'rpms': output.splitlines()}
    modules['data']['version'] = generate_modulemd_version(version)
    modules['data']['context'] = generate_modulemd_context(collection, version)
    modules_yaml = os.path.join(stage_dir, 'repodata', 'modules.yaml')

    with open(modules_yaml, 'w') as modules_file:
        yaml.dump(modules, modules_file, default_flow_style=False, explicit_start=True, explicit_end=True)

    check_output(['modifyrepo_c', '--mdtype=modules', modules_yaml, f"{stage_dir}/repodata"])


def create_repository(repo_dir):
    check_output(['createrepo', repo_dir])


def sync_copr_repository(collection, version, target_dir, source=False):
    if source:
        print(f"Syncing {collection} {version} Source RPM repository from Copr")
    else:
        print(f"Syncing {collection} {version} RPM repository from Copr")

    cmd = [
        'dnf',
        'reposync',
        '--newest-only',
        '--repo',
        f"el8-{collection}-{version}",
        '--config',
        'reposync_config.conf',
        '--download-path',
        target_dir
    ]

    if source:
        cmd.extend([
            '--source',
        ])
    else:
        cmd.extend([
            '--exclude',
            '*.src',
        ])

    check_output(cmd)


def main():
    try:
        collection = sys.argv[1]
        version = sys.argv[2]
        operating_system = sys.argv[3]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} collection version os")

    base_dir = 'tmp'
    rpm_sync_dir = f"{base_dir}/rpms"
    srpm_sync_dir = f"{base_dir}/srpms"

    stage_dir = f"{base_dir}/{collection}/{version}/{operating_system}/"
    rpm_dir = f"{stage_dir}/x86_64"
    srpm_dir = f"{stage_dir}/source"

    if not os.path.exists(rpm_sync_dir):
        os.makedirs(rpm_sync_dir)

    if not os.path.exists(srpm_sync_dir):
        os.makedirs(srpm_sync_dir)

    if not os.path.exists(rpm_dir):
        os.makedirs(rpm_dir)

    if not os.path.exists(srpm_dir):
        os.makedirs(srpm_dir)

    sync_copr_repository(collection, version, rpm_sync_dir)
    sync_copr_repository(collection, version, srpm_sync_dir, source=True)

    move_rpms_from_copr_to_stage(collection, version, srpm_sync_dir, srpm_dir, source=True)
    move_rpms_from_copr_to_stage(collection, version, rpm_sync_dir, rpm_dir)

    create_repository(rpm_dir)
    create_repository(srpm_dir)

    if collection in ['foreman', 'katello'] and operating_system == 'el8':
        create_modulemd(collection, version, rpm_dir)


if __name__ == '__main__':
    main()
