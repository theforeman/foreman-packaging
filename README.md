# deb packaging branches

The `deb/*` branches contain the Debian packaging files for Foreman and it's
dependencies. The repo mirrors [Foreman Core](https://github.com/theforeman/foreman),
i.e. `deb/develop` is for packaging branch `develop`, `deb/3.2` is for packaging release
3.2 and so on.

## Contributing

It's generally best to contribute to `deb/develop` unless something is specifically
broken for an older release. Please fork and send a PR.

PRs will get automatically tested and test packages will be built into a
per-user area on [stagingdeb.theforeman.org](https://stagingdeb.theforeman.org).
Example for adding a repository:

    # wget https://deb.theforeman.org/foreman.asc -O /etc/apt/trusted.gpg.d/foreman.asc
    # echo "deb http://stagingdeb.theforeman.org/ bookworm $USER-nightly" >> /etc/apt/sources.list.d/foreman.list

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
scripts/changelog.rb -v 2.0.0 -m "Bump changelog to 2.0.0 to match VERSION" debian/{buster,focal}/foreman{,-installer,-proxy}/changelog
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

### Packaging Plugins

Instructions are the same as for dependencies (see above) with the following differences:

1. Directory must be created in `plugins/GEM_NAME`
2. Plugins typically depend on `foreman` or `foreman-proxy`

## HOWTO: compare packages

Sometimes it is beneficial to compare the contents of this Git repository with the contents on deb.theforeman.org.

```console
$ ./scripts/compare_deb_repo.py --release X.Y
bionic
In repo but not in git:
{('ruby-foreman-ansible-core', '4.0.0-2'), ('ruby-yard', '0.9.8-1'), ('ruby-awesome-print', '1.8.0-1'), ('ruby-foreman-remote-execution-core', '1.5.0-1'), ('ruby-concurrent', '1.1.6+dfsg-2')}
In git but not in repo:
{('foreman-installer', '3.1.0-1'), ('foreman', '3.1.0-1'), ('foreman-proxy', '3.1.0-1')}
…
```

The output is formatted for each know "suite" (buster, focal, plugins) and lists packages (and their versions) that are either found in the repository, but not in git, or vice versa.

If there are packages that are in the repository, but not in git, this usually means that those packages weren't properly cleaned up.

If there are packages that are in git, but not in the repository, this usually means that the corresponding build failed or wasn't properly scheduled.

## HOWTO: removing packages

There is no automated way of removing packages from the Debian repository, once they have been removed from Git.

To remove a package from the Debian repository, two things need to happen:
1. The package file needs to be removed from the server
    * For core and dependencies, this happens in `/var/www/freight/apt/$SUITE/nightly/` *and* `/var/www/freightstage/apt/$SUITE/theforeman-nightly/`
    * For plugins, this happens in `/var/www/freight/apt/plugins/nightly`
1. The package index needs to be regenerated
    * This happens automatically on the next run of the cronjob, so you just need to wait

## HOWTO: add new Debian release

### Prerequisites

1. verify that the Ruby version is supported by Foreman
1. add the new release to the build infrastructure, like [bullseye was added in foreman-infra@15ebf5b](https://github.com/theforeman/foreman-infra/commit/15ebf5bdf553d4af2e4ff87ac89b8e39b124a706)
1. add the new release to forklift, like [bullseye was added in forklift@b2ea4fe](https://github.com/theforeman/forklift/commit/b2ea4fead5f247358e2a23a49e16f1bef3b5f9b8)
1. verify `puppet-agent` and `puppetserver` packages are available from `apt.puppet.com`
    * if `puppet-agent` isn't available `foreman-installer` won't build or run
    * if `puppetserver` isn't available packages will build, but deployment of Foreman will fail

### Prepare our repositories

When building packages, we add our own repositories to the build environment, as they carry build dependencies.
Because of that, we will have to create the repositories *before* building the first packages.

On the repository host, create the directories:
* `/var/www/freight/apt/$SUITE/nightly/` for the "real" repository
* `/var/www/freightstage/apt/$SUITE/theforeman-nightly/` for the "staging" repository

`chown` the directories to the `freight` and `freightstage` users accordingly.

As `freight` doesn't publish repositories that have no content, we need to drop *some* `.deb` package in each of these directories.
Ideally the package will have an older version, so it will be automatically cleaned up when we build the real package.

Once done, manually publish both repositories once:

```console
# sudo -u freight /usr/bin/freight-cache -c /home/freight/freight.conf
# sudo -u freightstage /usr/bin/freight-cache -c /home/freightstage/freight.conf
```

### Build dependencies

Once all the infrastructure is in place, it's time to build the packages from the `dependencies` directory.

The easiest way to do that is to copy the individual package directories from another Debian (or Ubuntu) release directory, preferable from the *newest* one.

While adding packages, please check if any of them are (now) available in Debian/Ubuntu and might not need packaging by us.

### Build core

After the depdendencies are built, you can copy over `foreman`, `foreman-proxy` and `foreman-installer` from another release directory.

## HOWTO: remove a Debian release

First make sure the removal is announced, usually done with an RFC and a release note.
For this a newer Debian/Ubuntu release needs to be supported together with the old release.
This gives users a chance to upgrade their distribution separate from the Foreman version.

1. Drop the release from [the website/manual](https://github.com/theforeman/theforeman.org) and [foreman-documentation](https://github.com/theforeman/foreman-documentation)
2. Update [jenkins-jobs](https://github.com/theforeman/jenkins-jobs)
  * Update the `operating_system` for dependency building in [`theforeman.org/pipelines/lib/packaging.groovy`](https://github.com/theforeman/jenkins-jobs/blob/master/theforeman.org/pipelines/lib/packaging.groovy) if it's the oldest release
  * Update `foreman_debian_releases` and `pipelines_deb` in [`theforeman.org/pipelines/vars/foreman/nightly.groovy`](https://github.com/theforeman/jenkins-jobs/blob/master/theforeman.org/pipelines/vars/foreman/nightly.groovy)
3. Drop it from [forklift](https://github.com/theforeman/forklift)'s [vagrant/config/versions.yaml](https://github.com/theforeman/forklift/blob/master/vagrant/config/versions.yaml)
4. Drop it from foreman-packaging's `deb/develop` branch
  * Drop the packaging definitions: `git rm -r {debian,dependencies}/$SUITE`
  * Update any remaining entries in the repository: `$EDITOR $(git grep -l $SUITE)`
5. Remove nightly packages
  * `sudo rm -r /var/www/freight/apt/$SUITE/nightly && sudo -u freight /usr/bin/freight-cache -c /home/freight/freight.conf`
  * `sudo rm -r /var/www/freightstage/apt/$SUITE/theforeman-nightly && sudo -u freightstage /usr/bin/freight-cache -c /home/freightstage/freight.conf`
6. Close the RFC on Discourse as resolved

## HOWTO: Archive a Foreman release

1. Identify which releases are affected:
```console
# ls /var/www/freight/apt/*
/var/www/freight/apt/bionic:
2.0  2.1  2.2  2.3  2.4  2.5  3.0
…
/var/www/freight/apt/focal:
2.5  3.0  3.1  3.10  3.11  3.2  3.3  3.4  3.5  3.6  3.7  3.8  3.9  nightly
…
```

2. Also check which releases are already archived:
```console
# ls /var/www/freightarchive/apt/*
/var/www/freightarchive/apt/bionic:
1.19  1.20  1.21  1.22  1.23  1.24
…
```

3. Move as planned:
```console
# mv /var/www/freight/apt/bionic/* /var/www/freightarchive/apt/bionic/

# mkdir /var/www/freightarchive/apt/focal
# mv /var/www/freight/apt/focal/2.5 /var/www/freightarchive/apt/focal/
# mv /var/www/freight/apt/focal/3.0 /var/www/freightarchive/apt/focal/
# mv /var/www/freight/apt/focal/3.1 /var/www/freightarchive/apt/focal/
# mv /var/www/freight/apt/focal/3.2 /var/www/freightarchive/apt/focal/
# mv /var/www/freight/apt/focal/3.3 /var/www/freightarchive/apt/focal/
# mv /var/www/freight/apt/focal/3.4 /var/www/freightarchive/apt/focal/
```

4. Adjust permissions
```console
# chown -R freightarchive.freightarchive /var/www/freightarchive/apt/
```

5. Regenerate package indexes
```console
# sudo -u freightarchive /usr/bin/freight-cache -c /home/freightarchive/freight.conf
# sudo -u freight /usr/bin/freight-cache -c /home/freight/freight.conf
```
