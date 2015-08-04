# deb packaging branches

The deb/\* branches contain the Debian packaging files for Foreman and it's
dependencies. The repo mirrors [Foreman Core](https://github.com/theforeman/foreman),
i.e. deb/develop is for packaging branch 'develop', deb/1.3 is for packaging release
1.3 and so on

## Contributing

It's generally best to contribute to 'deb/develop' unless something is specifically
broken for an older release. Please fork and send a PR.

PRs will get automatically tested and test packages will be built into a per-user
area on [stagingdeb.theforeman.org](http://stagingdeb.theforeman.org).

Our PR test jobs are very picky about branch names, for which we apologise.  Please
prefix *your* branch with the name of the target branch and a hyphen.  For example,
a PR to `deb/develop` could be called `deb/develop-fix-foo`.

## HOWTO: update a package

### Core project (foreman, foreman-proxy, foreman-installer)

Update under `debian/*/foreman`, once per OS.

These are built as regular full Debian packages.  Foreman itself ships its
dependencies via a bundler cache stored inside the binary deb and uses the cache
to install them during postinst.

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
