%global npm_name stats-webpack-plugin
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 0.6.1
Release: 2%{?dist}
Summary: Write the stats of a build to a file
License: MIT
URL: git://github.com/unindented/stats-webpack-plugin.git
Source0: http://registry.npmjs.org/stats-webpack-plugin/-/stats-webpack-plugin-0.6.1.tgz
Source1: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source2: stats-webpack-plugin-0.6.1-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(stats-webpack-plugin) = 0.6.1
Provides: bundled-npm(lodash) = 4.17.4
AutoReq: no
AutoProv: no


%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 2 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/stats-webpack-plugin
cp -pfr README.md index.js package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md ../../
# If any binaries are included, symlink them to bindir here

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
#$CHECK
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc README.md

%changelog
* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com> 0.6.1-1
- update webpack to v3.0 (ohadlevy@gmail.com)

