%global npm_name redux-logger

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 2.8.1
Release: 1%{?dist}
Summary: Logger for Redux
License: MIT
URL: https://github.com/theaqua/redux-logger#readme
Source0: http://registry.npmjs.org/redux-logger/-/redux-logger-2.8.1.tgz
Source1: http://registry.npmjs.org/deep-diff/-/deep-diff-0.3.4.tgz
Source2: redux-logger-2.8.1-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(redux-logger)) = 2.8.1
Provides: bundled(npm(deep-diff)) = 0.3.4
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
cd node_modules/redux-logger
cp -pfr CHANGELOG.md LICENSE README.md dist lib package.json src node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md LICENSE README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 2.8.1-1
- new package built with tito

