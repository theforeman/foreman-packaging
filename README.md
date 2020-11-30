# deb packaging branches

The deb/\* branches contain the Debian packaging files for Foreman and it's
dependencies. The repo mirrors [Foreman Core](https://github.com/theforeman/foreman),
i.e. deb/develop is for packaging branch 'develop', deb/1.3 is for packaging release
1.3 and so on

## Contributing

It's generally best to contribute to 'deb/develop' unless something is specifically
broken for an older release. Please fork and send a PR.

PRs will get automatically tested and test packages will be built into a
per-user area on [stagingdeb.theforeman.org](http://stagingdeb.theforeman.org).
Example for adding a repository:

    # curl -L https://stagingdeb.theforeman.org/foreman.asc | sudo apt-key add -
    # deb http://stagingdeb.theforeman.org/ buster ares-nightly

Our PR test jobs are very picky about branch names, for which we apologise.  Please
prefix *your* branch with the name of the target branch and a hyphen.  For example,
a PR to `deb/develop` could be called `deb/develop-fix-foo`.

## HOWTO: update a package

### Quick update

Automatic update for any plugin or regular dependency.

1. `scripts/update_package.rb -n my-package -v 1.2.3`
1. Update any dependencies that may have changed
1. `git commit -am "Updated my-package to 1.2.3"`

### Core project (foreman, foreman-proxy, foreman-installer)

Update under `debian/*/foreman`, once per OS.

These are built as regular full Debian packages.  Foreman itself ships its
dependencies via a bundler cache stored inside the binary deb and uses the cache
to install them during postinst.

To quickly bump version in all core projects, run e.g.:
```
scripts/changelog.rb -v 2.0.0 -m "Bump changelog to 2.0.0 to match VERSION" debian/{bionic,buster}/foreman{,-installer,-proxy}/changelog
```

### Foreman plugins

Foreman plugins are shipped as debs containing additional gems to add into the
bundler cache, so get installed with core dependencies.

1. Change version number in `plugins/ruby-foreman-example/debian/gem.list` and
   update any dependencies where possible
1. Change version number in `plugins/ruby-foreman-example/foreman_example.rb`
1. Run `scripts/changelog.rb -v 1.2.3 plugins/ruby-foreman-example/debian/changelog`

### Smart proxy plugins

Smart proxy plugins are shipped as regular Debian Ruby packages built to install
gems into the system paths.

1. Change version number in `plugins/smart_proxy_example/example.rb`
1. Run `scripts/changelog.rb -v 1.2.3 plugins/smart_proxy_example/debian/changelog`

### Dependencies

Dependencies are regular Debian Ruby packages that are used directly (such as Hammer)
or as deps for smart proxy and Hammer or their plugins.  They are built to install
gems into system paths.

1. Run `scripts/changelog.rb -v 1.2.3 dependencies/*/example/changelog`

## HOWTO: create a package

Adding a package into this repository.

### Prerequisites

1. Debian machine (VM or container)
1. Install `gem2deb` and a few optional dependencies: `apt install gem2deb apt-file python3-debian`
1. Update `apt-file` cache, it's used for calculating dependencies: `apt-file update`

### Packaging Plugins

1. TBD

### Packaging Dependencies

1. Use `gem2deb` utility from Debian to generate a good starting point: `gem2deb -s GEM_NAME`, this will produce a `ruby-GEM_NAME-VERSION` directory (the gem name will be mangled to match Debian rules: no underscores, lowercase only).
1. Create new directory `dependencies/*/GEM_NAME` (ensure it's exactly the name of the gem)
1. Copy the contents of `ruby-GEM_NAME-VERSION/debian/` to `dependencies/*/GEM_NAME`
1. Review the `control` file, debian package name must not include underscores, use dash characters instead (e.g. `Source: ruby-rubygem-name`)
1. Review build dependencies, packages typically depend on `debhelper`, `gem2deb` and optionally on `git`
1. Review runtime dependencies
1. Review the `copyright` file and check the gem license
1. Review the `*.docs` file
1. Review the `changelog` file
1. See the Contributing section above for instructions on where to download the final build
