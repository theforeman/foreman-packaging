# rpm packaging branches

The rpm/\* branches contain RPM spec files for Foreman's dependencies and
related projects (mostly rubygems and npm modules).

## Requirements

If you're just submitting a fix, you don't need anything special.

If you're submitting a patch which adds/updates a gem package, you will need:

* [gem2rpm](https://rubygems.org/gems/gem2rpm) or rubygem-gem2rpm
* [git-annex](http://git-annex.branchable.com/)
* ruamel: for fedora use `dnf install python3-ruamel-yaml`
* python3-semver: for fedora use `dnf install python3-semver`

If you're submitting a patch which adds/updates npm modules (nodejs- packages) you will need:

* [npm2rpm](https://www.npmjs.com/package/npm2rpm)
* [git-annex](http://git-annex.branchable.com/)

To build locally or release RPMs from this repo, you also require:

* [obal](https://github.com/theforeman/obal) 0.10.0 or higher
* [mock](http://fedoraproject.org/wiki/Projects/Mock) or Copr client and a Fedora account

## HOWTO: checkout

Run:

* `git clone https://github.com/theforeman/foreman-packaging -b rpm/develop`
* `git annex init` to set up this repo for using git annex
* `./setup_sources.sh` to register git-annex file URLs

## HOWTO: test a package

Before releasing a build, please test it. This can either be done locally with
mock or, if you have access, using the Foreman Koji instance.

### With mock

Configuration for mock is supplied in mock/ and can be used to build any of
the packages locally and quickly.

```sh
obal mock PACKGE --config ./mock/el8.cfg
```

### With Koji access

If you have a certificate for our Koji server (regular packagers can get them),
then you can use Obal to build scratch packages on Koji, though it's slower
than mock (above).

    obal scratch PACKAGE

## HOWTO: Add a package

### Adding gem packages

1. Ensure you're on a fresh git branch because the tooling will create a commit.
1. Choose a template from gem2rpm that's suitable for the type of package and
   run:
  `./add_gem_package.sh GEM_NAME TEMPLATE REPO`
   Running without arguments will list the templates and repos.
1. Improve the spec file to a reasonable standard, tidying up any gem2rpm
   weirdness.  In particular, look for:
   * Convert SPDX licences to [Fedora short names](https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Software_License_List)
   * Ensure summary is under 72 characters
   * Verify everything is added properly
   * Amend any changes to the existing commit
1. Submit a pull request against `rpm/develop`

### npm2rpm instructions

In order to add or update npm dependencies, you will need [npm2rpm](https://www.npmjs.com/package/npm2rpm).

1. Until npm2rpm is released, you will need to install it from source (git clone).
1. In your `npm2rpm` directory, run `npm install`.
1. Make a symlink from `npm2rpm.js` to `npm2rpm` (with no extension).  This is so the update script, `add_npm_package.sh`, can find it.
  ```
  ln -s ~/npm2rpm/bin/npm2rpm.js ~/npm2rpm/bin/npm2rpm
  ```
1. Make sure that `npm2rpm` is in your $PATH
1. Before you run the update script, make sure the following are installed:
  * nokogiri - `gem install nokogiri`
  * python3 - `yum install python3`

### Adding npm packages

First, you need to decide if your package will include bundled dependencies or not.
If you can resolve all the npm modules dependencies tree using the packages available, then
you'll build a package without bundled dependencies.

Otherwise we will bundle the dependencies. You can read an explanation of how we do this in
[npm2rpm](https://www.npmjs.com/package/npm2rpm#packaging-npm-modules-with-bundled-dependencies--s---stategy-bundle)

In both cases:

1. Ensure you're on a fresh git branch because the tooling will create a commit.
1. Generate the spec and download the sources automatically with npm2rpm.
   * For packages without dependencies - `./add_npm_package.sh example version single`
   * For packages that bundle dependencies - `./add_npm_package.sh example version bundle`
1. This should have created a nodejs-example directory with the packages needed, the spec,
and the cache if it's a bundled package. It should have modified comps and
added everything to git, including a commit.
1. Add the package to `package_manifest.yaml`
1. Amend the commit
1. Update the spec if needed (e.g: for peer dependencies). Amend the commit if needed.
1. Follow the "test a package" section above until it builds for all targeted platforms and
required non-SCL modes.
1. Submit a pull request against `rpm/develop`

## HOWTO: Updating packages

### Updating gem packages

1. Run the update script
   * `./bump_rpm.sh rubygem-foo`
1. Check the output
   * update `Requires` to match changes in runtime dependencies
   * add/remove entries in `%files` if required for new root files
1. Amend the commit if needed
1. Follow the "test a package" section above until it builds for all
   targeted platforms and required SCL + non-SCL modes.
1. Submit a pull request against `rpm/develop`

### Updating npm packages

In order to update npm packages, first you will need to follow the [npm2rpm instructions](https://github.com/theforeman/foreman-packaging/tree/rpm/develop#npm2rpm-instructions) above.  Once that's done,

1. Run the update script
  ```sh
  # update or install package latest version
  ./add_npm_package.sh PACKAGE

  # update or install package with a given version
  ./add_npm_package.sh PACKAGE VERSION

  # to update @theforeman/vendor and @theforeman/builder to latest
  ./update_vendor.sh
  # to update @theforeman/vendor and @theforeman/builder to version 1.0.0
  ./update_vendor.sh 1.0.0
  ```
1. Verify the changes
1. Amend the commit if needed
1. Follow the "test a package" section above until it builds for all
   targeted platforms and required SCL + non-SCL modes.
1. Submit a pull request against `rpm/develop`

### Updating nightly dependencies

The nightly packages are slightly special because we can't use a gem or npm
package to extract dependencies from. That's why we have our own tools:

#### Foreman

To update foreman we'll assume a git checkout at `~/foreman`:

    ./get-gemfile-deps ~/foreman/Gemfile | ./update-requirements specfile - packages/foreman/foreman/foreman.spec
    ./update-requirements npm ~/foreman/package.json packages/foreman/foreman/foreman.spec

#### Katello

To update Katello we'll assume a git checkout at `~/katello`:

    # TODO: extract dependencies from gemspec
    ./update-requirements npm ~/katello/package.json packages/katello/rubygem-katello/rubygem-katello.spec

## HOWTO: build multiple packages

If you have multiple packages that you want to build together because they
depend on each other, `mockchain` can be very helpful. To do this use Obal `mock`:

   obal mock rubygem-rails rubygem-actioncable --config mock/el8.cfg

## HOWTO: removing a package

1. `./remove_package rubygem-example`
1. On merge, delete the package from Copr:

    copr-cli delete-package --name rubygem-example @theforeman/$PROJECT-nightly-staging

## Handle gems that are default Ruby gems

Look at https://stdgems.org/ and see if a gem is listed as a default gem. The website https://docs.ruby-lang.org/en/master/NEWS_md.html can also help in determining what will or is default and for what version of Ruby.

Use`%gemspec_remove_dep <GEM_NAME>` to drop the gem from the gemspec and manually add a dependency on ruby-default-gems as a rich dependency: `(rubygem(<GEM_NAME>) or ruby-default-gems < 3.4)`.

## How does this repo work?

This repo contains a directory per source package and configuration in `package_manifest.yaml`.
Each source package directory contains a spec file and patches under version control plus references to the source files (i.e. gems or tarballs).

These references are managed using git-annex, a git extension for tracking
large binary blobs outside of the git repo itself.  This means we can
reference source files directly on rubygems.org etc, or perhaps set up a kind
of lookaside cache in the future.  For now, we use the [special web remote](http://git-annex.branchable.com/tips/using_the_web_as_a_special_remote/)
with URLs to all of our source files available on the web.

Obal's custom git-annex support will automatically (lazily) fetch
files and cache them in your local git checkout as and when you build packages.

Obal lets you build a SRPM and submit to Copr, which builds the binary package
(whereupon it gets pulled into our yum repositories).

This repository is branched like Foreman itself, with rpm/1.x branches
for major releases.

To build a new release package for foreman project for example, do this:

    $ obal release foreman

## License

Spec files are generally based on Fedora spec files, which means that unless a
spec file contains an explicit license attribution within it, it is available
under the MIT license.
