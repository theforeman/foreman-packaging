# rpm packaging branches

The rpm/\* branches contain RPM spec files for Foreman's dependencies and
related projects (mostly rubygems and npm modules).

## Requirements

If you're just submitting a fix, you don't need anything special.

If you're submitting a patch which adds/updates a gem package, you will need:

* [gem2rpm](https://rubygems.org/gems/gem2rpm) or rubygem-gem2rpm
* [gem-compare](https://rubygems.org/gems/gem-compare)
* [git-annex](http://git-annex.branchable.com/)

For npm modules (nodejs- packages) you will need:

* [npm2rpm](https://www.npmjs.com/package/npm2rpm)
* [git-annex](http://git-annex.branchable.com/)

To build locally or release RPMs from this repo, you also require:

* [obal](https://github.com/theforeman/obal) 0.0.2 or higher
* [tito](https://github.com/dgoodwin/tito) 0.6.1 or higher
* [mock](http://fedoraproject.org/wiki/Projects/Mock) or koji client and an account (certificate) on koji.katello.org
* scl-utils-build package (Fedora or Red Hat repositories)

## HOWTO: checkout

Run:

* `git clone https://github.com/theforeman/foreman-packaging -b rpm/develop`
* `git annex init` to set up this repo for using git annex
* `./setup_sources.sh` to register git-annex file URLs

## HOWTO: test a package

Before releasing a build, please test it.  Using tito's --test flag, you can
generate test (S)RPMs by first committing your changes locally, then it will
use the SHA in the RPM version.

### With mock

Configuration for mock is supplied in mock/ and can be used to build any of
the packages locally and quickly.

1. Copy mock/site-defaults.cfg.basic to site-defaults.cfg, or look at other
   example configs for more options.
1. `tito build --rpm --test --builder tito.builder.MockBuilder --arg mock_config_dir=mock/ --arg mock=el7-scl`

The last argument is the name of the mock config in mock/, which includes SCL
and non-SCL variants.

### With koji access

If you have a certificate for our Koji server (regular packagers can get them),
then you can use tito to build scratch packages on Koji, though it's slower
than mock (above).

Non-core packages in the main Foreman repo, with sources in git(-annex):

    tito release koji-foreman --test --scratch

Packages in the plugins repo:

    tito release koji-foreman-plugins --test --scratch

Core nightly Foreman packages:

* foreman: `tito release --scratch --arg jenkins_job=test_develop koji-foreman-nightly`
* foreman-installer: `tito release --scratch --arg jenkins_job=packaging_trigger_installer_develop koji-foreman-nightly`
* foreman-proxy: `tito release --scratch --arg jenkins_job=test_proxy_develop koji-foreman-nightly`
* foreman-selinux: `tito release --scratch --arg jenkins_job=packaging_trigger_selinux_develop koji-foreman-nightly`
* rubygem-hammer\_cli: `tito release --scratch --arg jenkins_job=test_hammer_cli koji-foreman-nightly`
* rubygem-hammer\_cli\_foreman: `tito release --scratch --arg jenkins_job=test_hammer_cli_foreman koji-foreman-nightly`

Using a local git checkout, change `source_dir` as appropriate:

* Core packages: `tito release --scratch --arg source_dir=~/foreman koji-foreman-nightly`
* Plugins: `tito release --scratch --arg source_dir=~/foreman_bootdisk koji-foreman-plugins-nightly`

## HOWTO: create a new core package or dependency (gems)

1. Check if it's available in Fedora:
  * https://apps.fedoraproject.org/packages/NAME
  * http://www.isitfedoraruby.com/fedorarpms/NAME
  * If only building non-SCL and it's in both Fedora and EPEL, stop now
1. If available in Fedora, copy the spec from the SCM link on the left
1. Ensure you're on a fresh git branch because the tooling will create a commit.
1. Choose a template from gem2rpm that's suitable for the type of package and
   run:
  `./add_gem_package.sh GEM_NAME TEMPLATE TITO_TAG`
1. Improve the spec file to a reasonable standard, tidying up any gem2rpm
   weirdness.  In particular, look for:
  * Convert SPDX licences to [Fedora short names](https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Software_License_List)
  * Ensure summary is under 72 characters
  * Verify everything is added properly
  * Amend any changes to the existing commit
1. Follow the "test a package" section above until it builds for all
   targeted platforms and required SCL + non-SCL modes.
1. Submit a pull request against `rpm/develop`

## HOWTO: create a new core package or dependency (npm modules)

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
and the cache if it's a bundled package. It should have modified tito.props, comps and
added everything to git, including a commit.
1. Update the spec if needed (e.g: for peer dependencies). Amend the commit if needed.
1. Follow the "test a package" section above until it builds for all targeted platforms and
required non-SCL modes.
1. Submit a pull request against `rpm/develop`

## HOWTO: update a gem package

1. Run the update script
  1. `./bump_rpm.sh rubygem-foo`
1. Check the output of [gem-compare](https://rubygems.org/gems/gem-compare)
  1. update `Requires` to match changes in runtime dependencies
  1. add/remove entries in %files if required for new root files
1. Commit the changes
  1. `git commit -m "Update NAME to VERSION"`
1. Follow the "test a package" section above until it builds for all
   targeted platforms and required SCL + non-SCL modes.
1. Submit a pull request against `rpm/develop`

## HOWTO: build multiple packages

If you have multiple packages that you want to build together because they
depend on each other, `mockchain` can be very helpful. To do this:

1. Use tito to generate a SRPM for every package. Run  `tito build --srpm
--test --builder` on every package directory
1. Run `mockchain -r el7-scl --tmp_prefix tfm --recurse /tmp/tito/*.src.rpm`
to build the SRPMs created in the previous step. This will attempt to build
all your packages in alphabetical order and will retry.
1. The results of mockchain will be put in '/var/tmp/mock-chain-tfm.../'.
To benefit from that and avoid building packages that were already successfully
built, run  `mockchain -l /var/tmp/mock-chain-tfm.../` adjusting the path for
the location of your packages.

## HOWTO: removing a package

1. `git rm -r rubygem-example/`
1. Remove all entries (both main package and doc) from `comps/` and
   `rel-eng/tito.props`
1. Add an `Obsoletes` entry to `tfm/tfm.spec` for `< Version-(Release+1)`
   if the package is a dependency in either core or plugin repos
1. On merge, untag all builds from nightly Koji tags (`untag-build --all`),
   block the package (`block-pkg`) and rebuild `tfm` if applicable

Leave the rel-eng/packages/ file in place so a permanent record of the last EVR
is kept.

## How does this repo work?

This repo contains a directory per source package and some tito configuration
and state (under rel-eng/).  Each source package directory contains a spec
file and patches under version control plus references to the source files
(i.e. gems or tarballs).

These references are managed using git-annex, a git extension for tracking
large binary blobs outside of the git repo itself.  This means we can
reference source files directly on rubygems.org etc, or perhaps set up a kind
of lookaside cache in the future.  For now, we use the [special web remote](http://git-annex.branchable.com/tips/using_the_web_as_a_special_remote/)
with URLs to all of our source files available on the web.

Obal's custom git-annex support for tito will automatically (lazily) fetch
files and cache them in your local git checkout as and when you build packages.

tito works in two key stages: tagging and releasing.  Obal's custom git-annex
support helps bypass the tagging stage.

tito lets you build a SRPM and submit to koji, which builds the binary package
(whereupon it gets pulled into our yum repositories).

This repository is branched like Foreman itself, with rpm/1.x branches
for major releases.

To find tito build targets do this:

    $ tito release -l
    [koji-foreman]
    [koji-foreman-nightly]
    [koji-foreman-plugins]

To build a new release package for foreman project for example, do this:

    $ tito release koji-foreman

## Releasing a package

After a PR has been merged to add or update a package, then the package should be released.  In
case it's a new package, be sure to add it to the correct koji tags as well.  [Here's a helper script](https://github.com/theforeman/foreman-packaging/blob/rpm/develop/rel-eng/compare-with-tags.rb)

1. Switch to the directory for the package to be released, i.e. for the rubygem-mysql2 package:

    `$ cd packages/foreman/rubygem-mysql2/`

1. Do a scratch build of the release first:

    `$ tito release --scratch koji-foreman koji-foreman-plugins`

1. Verify package built successfully in koji, and then release:

    `$ tito release koji-foreman koji-foreman-plugins`

* This uses local filesystem, so please be sure your using a clean checkout with no local changes

## License

Spec files are generally based on Fedora spec files, which means that unless a
spec file contains an explicit license attribution within it, it is available
under the MIT license.

## TODO / ideas

Instead of using KojiReleaser, we should use KojiGitReleaser so Koji checks
out this repo from git and runs `make srpm`, which could use tito to build
the SRPM.  This has the nice benefit of not accepting random SRPMs as builds
in Koji, giving end to end safety + verification.  The Makefile could be in a
common/ directory.

  * http://www.redhat.com/archives/fedora-buildsys-list/2008-August/msg00014.html
  * http://www.redhat.com/archives/fedora-buildsys-list/2007-September/msg00023.html
  * https://git.fedorahosted.org/cgit/koji/tree/koji/daemon.py#n320
