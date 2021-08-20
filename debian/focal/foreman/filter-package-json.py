#!/usr/bin/env python3

import json

# We need a list of packages that are devDependencies but not needed to build
EXCLUDE_NPM_PACKAGES = [
    '@sheerun/mutationobserver-shim',
    '@testing-library/jest-dom',
    '@testing-library/react',
    '@theforeman/env',
    '@theforeman/eslint-plugin-foreman',
    '@theforeman/stories',
    '@theforeman/test',
    '@theforeman/vendor-dev',
    '@theforeman/find-foreman',
    'axios-mock-adapter',
    'babel-eslint',
    'babel-jest',
    'babel-plugin-dynamic-import-node',
    'coveralls',
    'cross-env',
    'highlight.js',
    'jest',
    'nock',
    'prettier',
    'raw-loader',
    'react-addons-test-utils',
    'react-dnd-test-backend',
    'react-dnd-test-utils',
    'react-remarkable',
    'react-test-renderer',
    'react-redux-test-utils',
    'redux-mock-store',
    'surge',
    'webpack-bundle-analyzer',
    'webpack-dev-server',
]

EXCLUDE_NPM_PREFIXES = [
    '@storybook/',
    'enzyme',
    'eslint',
    'jest-',
    'stylelint',
]

def is_excluded(package):
    return (package in EXCLUDE_NPM_PACKAGES
            or any(package.startswith(prefix) for prefix in EXCLUDE_NPM_PREFIXES))

def filter_section(packages, section):
    deps = packages.get(section, {})
    for package, version in sorted(deps.items()):
        if not is_excluded(package):
            yield (package, version)

with open('package.json') as package_json:
    data = json.load(package_json)
for section in ('devDependencies', 'dependencies'):
    data[section] = {package: version for (package, version) in filter_section(data, section)}

with open('package.json', 'w') as package_json:
    json.dump(data, package_json, indent=2)
