%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name c3

%{?nodejs_find_provides_and_requires}

Name: %{?scl_prefix}nodejs-%{npm_name}
Version: 0.4.11
Release: 1%{?dist}
Summary: D3-based reusable chart library
License: MIT
URL: https://github.com/masayuki0812/c3
Source0: http://registry.npmjs.org/c3/-/c3-0.4.11.tgz
Source1: http://registry.npmjs.org/d3/-/d3-3.5.17.tgz
Source2: c3-0.4.11-registry.npmjs.org.tgz
Requires: %{?scl_prefix_nodejs}nodejs(engine)
BuildRequires: %{?scl_prefix_nodejs}npm
BuildArch:  noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled-npm(c3) = 0.4.11
Provides: bundled-npm(d3) = 3.5.17
AutoReq: no
AutoProv: no

%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  if [ $(echo $tgz | grep -q registry.npmjs.org) ];then
%{?scl:scl enable %{scl} - <<EOF}
npm cache add --cache ./npm_cache $tgz
%{?scl:EOF}
  fi
done

%setup -T -q -a 2 -D -n npm_cache

%build
%{?scl:scl enable %{scl} - <<EOF}
npm install --cache-min Infinity --cache . --global-style true %{npm_name}@%{version}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/c3
cp -pfr .editorconfig .jshintrc .npmignore .travis.yml CONTRIBUTING.md Gruntfile.coffee LICENSE README.md bower.json c3.css c3.js c3.min.css c3.min.js component.json extensions htdocs karma.conf.js package.json spec src node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CONTRIBUTING.md LICENSE README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE
%doc CONTRIBUTING.md
%doc README.md

%changelog
* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 0.4.11-1
- new package built with tito

