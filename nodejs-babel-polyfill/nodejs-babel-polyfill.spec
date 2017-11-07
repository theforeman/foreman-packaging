%global npm_name babel-polyfill
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 6.26.0
Release: 1%{?dist}
Summary: Provides polyfills necessary for a full ES2015+ environment
License: MIT
URL: https://babeljs.io/
Source0: http://registry.npmjs.org/babel-polyfill/-/babel-polyfill-6.26.0.tgz
Source1: http://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source2: http://registry.npmjs.org/core-js/-/core-js-2.5.1.tgz
Source3: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.0.tgz
Source4: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.10.5.tgz
Source5: babel-polyfill-6.26.0-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(babel-polyfill) = 6.26.0
Provides: bundled-npm(babel-runtime) = 6.26.0
Provides: bundled-npm(core-js) = 2.5.1
Provides: bundled-npm(regenerator-runtime) = 0.11.0
Provides: bundled-npm(regenerator-runtime) = 0.10.5
AutoReq: no
AutoProv: no


%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done

%setup -T -q -a 5 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/babel-polyfill
cp -pfr .npmignore README.md browser.js dist lib package-lock.json package.json scripts node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md  ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc README.md

%changelog
* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.26.0-1
- new package built with tito

