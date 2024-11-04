%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name babel-plugin-transform-class-properties

Name: %{?scl_prefix}nodejs-babel-plugin-transform-class-properties
Version: 6.24.1
Release: 5%{?dist}
Summary: This plugin transforms static class properties as well as properties declared with the property initializer syntax
License: MIT
Group: Development/Libraries
URL: https://github.com/babel/babel/tree/master/packages/babel-plugin-transform-class-properties
Source0: https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source1: https://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source2: https://registry.npmjs.org/babel-code-frame/-/babel-code-frame-6.26.0.tgz
Source3: https://registry.npmjs.org/babel-helper-function-name/-/babel-helper-function-name-6.24.1.tgz
Source4: https://registry.npmjs.org/babel-helper-get-function-arity/-/babel-helper-get-function-arity-6.24.1.tgz
Source5: https://registry.npmjs.org/babel-messages/-/babel-messages-6.23.0.tgz
Source6: https://registry.npmjs.org/babel-plugin-syntax-class-properties/-/babel-plugin-syntax-class-properties-6.13.0.tgz
Source7: https://registry.npmjs.org/babel-plugin-transform-class-properties/-/babel-plugin-transform-class-properties-6.24.1.tgz
Source8: https://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source9: https://registry.npmjs.org/babel-template/-/babel-template-6.26.0.tgz
Source10: https://registry.npmjs.org/babel-traverse/-/babel-traverse-6.26.0.tgz
Source11: https://registry.npmjs.org/babel-types/-/babel-types-6.26.0.tgz
Source12: https://registry.npmjs.org/babylon/-/babylon-6.18.0.tgz
Source13: https://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source14: https://registry.npmjs.org/core-js/-/core-js-2.6.9.tgz
Source15: https://registry.npmjs.org/debug/-/debug-2.6.9.tgz
Source16: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source17: https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
Source18: https://registry.npmjs.org/globals/-/globals-9.18.0.tgz
Source19: https://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source20: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source21: https://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source22: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source23: https://registry.npmjs.org/lodash/-/lodash-4.17.15.tgz
Source24: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source25: https://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source26: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.1.tgz
Source27: https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source28: https://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source29: https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-1.0.3.tgz
Source30: nodejs-babel-plugin-transform-class-properties-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(ansi-regex)) = 2.1.1
Provides: bundled(npm(ansi-styles)) = 2.2.1
Provides: bundled(npm(babel-code-frame)) = 6.26.0
Provides: bundled(npm(babel-helper-function-name)) = 6.24.1
Provides: bundled(npm(babel-helper-get-function-arity)) = 6.24.1
Provides: bundled(npm(babel-messages)) = 6.23.0
Provides: bundled(npm(babel-plugin-syntax-class-properties)) = 6.13.0
Provides: bundled(npm(babel-plugin-transform-class-properties)) = 6.24.1
Provides: bundled(npm(babel-runtime)) = 6.26.0
Provides: bundled(npm(babel-template)) = 6.26.0
Provides: bundled(npm(babel-traverse)) = 6.26.0
Provides: bundled(npm(babel-types)) = 6.26.0
Provides: bundled(npm(babylon)) = 6.18.0
Provides: bundled(npm(chalk)) = 1.1.3
Provides: bundled(npm(core-js)) = 2.6.9
Provides: bundled(npm(debug)) = 2.6.9
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(esutils)) = 2.0.3
Provides: bundled(npm(globals)) = 9.18.0
Provides: bundled(npm(has-ansi)) = 2.0.0
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(js-tokens)) = 3.0.2
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(lodash)) = 4.17.15
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(ms)) = 2.0.0
Provides: bundled(npm(regenerator-runtime)) = 0.11.1
Provides: bundled(npm(strip-ansi)) = 3.0.1
Provides: bundled(npm(supports-color)) = 2.0.0
Provides: bundled(npm(to-fast-properties)) = 1.0.3
AutoReq: no
AutoProv: no

%if 0%{?scl:1}
%define npm_cache_dir npm_cache
%else
%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%endif

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done
%{?scl:end_of_scl}

%setup -T -q -a 30 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --legacy-peer-deps --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Feb 01 2024 Eric D. Helms <ericdhelms@gmail.com> - 6.24.1-5
- Use --legacy-peer-deps during npm install

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 6.24.1-4
- Bump packages to build for el8

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.24.1-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.24.1-2
- Update specs to handle SCL

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.24.1-1
- new package built with tito
