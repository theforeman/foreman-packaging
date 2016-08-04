%global npm_name babel-loader

Name: nodejs-%{npm_name}
Version: 6.2.4
Release: 1%{?dist}
Summary: babel module loader for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/babel/babel-loader
Source0: http://registry.npmjs.org/babel-loader/-/babel-loader-6.2.4.tgz
Source1: http://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source2: http://registry.npmjs.org/object-assign/-/object-assign-4.1.0.tgz
Source3: http://registry.npmjs.org/loader-utils/-/loader-utils-0.2.15.tgz
Source4: http://registry.npmjs.org/json5/-/json5-0.5.0.tgz
Source5: http://registry.npmjs.org/emojis-list/-/emojis-list-2.0.1.tgz
Source6: http://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source7: http://registry.npmjs.org/big.js/-/big.js-3.1.3.tgz
Source8: babel-loader-6.2.4-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildRequires: npm(webpack)
BuildRequires: npm(babel-core)
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(babel-loader) = 6.2.4
Provides: bundled-npm(mkdirp) = 0.5.1
Provides: bundled-npm(object-assign) = 4.1.0
Provides: bundled-npm(loader-utils) = 0.2.15
Provides: bundled-npm(json5) = 0.5.0
Provides: bundled-npm(emojis-list) = 2.0.1
Provides: bundled-npm(minimist) = 0.0.8
Provides: bundled-npm(big.js) = 3.1.3
AutoReq: no
AutoProv: no

%description
babel module loader for webpack

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{npm_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 8 -D -n npm_cache

%build
mkdir node_modules/
# Notice I make regular symlinks instead of running npm link, as the latter will ask for
# root permissions
ln -s %{nodejs_sitelib}/webpack node_modules/webpack
ln -s %{nodejs_sitelib}/babel-core node_modules/babel-core
npm install babel-loader@6.2.4 --cache-min Infinity --cache .

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/babel-loader
cp -pfr README.md ../../
cp -pfr index.js lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here
mkdir -p %{buildroot}%{nodejs_sitelib}/${npm_name}/bin
mkdir -p %{buildroot}%{_bindir}/

%check

%files
%{nodejs_sitelib}/%{npm_name}

%files doc
%doc README.md

%changelog
