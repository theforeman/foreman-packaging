%global npm_name brace

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 0.10.0
Release: 1%{?dist}
Summary: browserify compatible version of the ace editor
License: MIT
URL: https://github.com/thlorenz/brace
Source0: http://registry.npmjs.org/brace/-/brace-0.10.0.tgz
Source1: http://registry.npmjs.org/w3c-blob/-/w3c-blob-0.0.1.tgz
Source2: brace-0.10.0-registry.npmjs.org.tgz
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
Provides: bundled-npm(brace) = 0.10.0
Provides: bundled-npm(w3c-blob) = 0.0.1
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
cd node_modules/brace
cp -pfr .npmignore LICENSE README.md assets example ext index.d.ts index.js keybinding mode package.json snippets test theme worker node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf LICENSE README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Fri Mar 24 2017 Dominic Cleal <dominic@cleal.org> 0.10.0-1
- new package built with tito

