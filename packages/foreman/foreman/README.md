# Where is the source?

The source of this package is not checked into the repo but rather generated for every nightly build. If you need to generate it, the rake task `pkg:generate_source` in the foreman repository will build the tarbal.

# Updating the nodejs dependencies

There is a `update-node-dependencies` script to update the `Requires` and `BuildRequires` in `foreman.spec` based on `package.json`.

It's written in Python 3 and needs [semver](https://pypi.python.org/pypi/semver) installed. On Debian and Fedora this is packaged as `python3-semver`. On other platforms `pip` can be used.

`
./update-node-dependencies /path/to/foreman/package.json
`

## Internal details

It uses markers to replace sections. There are 4 sections: for both devDependencies and dependencies it adds BuildRequires (for the foreman package) and Requires (for the foreman-assets package).

```
Name: foreman
...
# start package.json devDependencies BuildRequires
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires
...

%package assets
...
# start package.json devDependencies Requires
# end package.json devDependencies Requires

# start package.json dependencies Requires
# end package.json dependencies Requires
...
```

All the content between start and end is discarded while maintaining all the other lines. It then inserts generated dependencies equivalent to what's in package.json with some (static) blacklists. This is an optimization because we have no need for some this like linters or pure test dependencies. This is a lack in flexibility with `devDependencies`.
