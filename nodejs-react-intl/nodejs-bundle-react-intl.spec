%global npm_name react-intl
%global enable_tests 0 

Name: nodejs-%{npm_name}
Version: 2.4.0
Release: 1%{?dist}
Summary: Internationalize React apps
License: BSD-3-Clause
URL: https://github.com/yahoo/react-intl
Source0: http://registry.npmjs.org/react-intl/-/react-intl-2.4.0.tgz
Source1: http://registry.npmjs.org/intl-format-cache/-/intl-format-cache-2.1.0.tgz
Source2: http://registry.npmjs.org/invariant/-/invariant-2.2.2.tgz
Source3: http://registry.npmjs.org/intl-relativeformat/-/intl-relativeformat-2.1.0.tgz
Source4: http://registry.npmjs.org/intl-messageformat/-/intl-messageformat-2.2.0.tgz
Source5: http://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source6: http://registry.npmjs.org/intl-messageformat-parser/-/intl-messageformat-parser-1.4.0.tgz
Source7: http://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source8: react-intl-2.4.0-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(react-intl) = 2.4.0
Provides: bundled-npm(intl-format-cache) = 2.1.0
Provides: bundled-npm(invariant) = 2.2.2
Provides: bundled-npm(intl-relativeformat) = 2.1.0
Provides: bundled-npm(intl-messageformat) = 2.2.0
Provides: bundled-npm(loose-envify) = 1.3.1
Provides: bundled-npm(intl-messageformat-parser) = 1.4.0
Provides: bundled-npm(js-tokens) = 3.0.2
AutoReq: no 
AutoProv: no 


%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./%{npm_cache_dir} $tgz
done

%setup -T -q -a 8 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/react-intl
cp -pfr CONTRIBUTING.md LICENSE.md README.md dist lib locale-data package.json src node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CONTRIBUTING.md LICENSE.md README.md LICENSE.md ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE.md
%doc CONTRIBUTING.md
%doc LICENSE.md
%doc README.md

%changelog
