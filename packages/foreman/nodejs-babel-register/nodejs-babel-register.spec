%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name babel-register

Name: %{?scl_prefix}nodejs-babel-register
Version: 6.26.0
Release: 3%{?dist}
Summary: babel require hook
License: MIT
Group: Development/Libraries
URL: https://github.com/babel/babel/tree/master/packages/babel-register
Source0: https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source1: https://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source2: https://registry.npmjs.org/babel-code-frame/-/babel-code-frame-6.26.0.tgz
Source3: https://registry.npmjs.org/babel-core/-/babel-core-6.26.3.tgz
Source4: https://registry.npmjs.org/babel-generator/-/babel-generator-6.26.1.tgz
Source5: https://registry.npmjs.org/babel-helpers/-/babel-helpers-6.24.1.tgz
Source6: https://registry.npmjs.org/babel-messages/-/babel-messages-6.23.0.tgz
Source7: https://registry.npmjs.org/babel-register/-/babel-register-6.26.0.tgz
Source8: https://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source9: https://registry.npmjs.org/babel-template/-/babel-template-6.26.0.tgz
Source10: https://registry.npmjs.org/babel-traverse/-/babel-traverse-6.26.0.tgz
Source11: https://registry.npmjs.org/babel-types/-/babel-types-6.26.0.tgz
Source12: https://registry.npmjs.org/babylon/-/babylon-6.18.0.tgz
Source13: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz
Source14: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source15: https://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source16: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source17: https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.6.0.tgz
Source18: https://registry.npmjs.org/core-js/-/core-js-2.6.9.tgz
Source19: https://registry.npmjs.org/debug/-/debug-2.6.9.tgz
Source20: https://registry.npmjs.org/detect-indent/-/detect-indent-4.0.0.tgz
Source21: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source22: https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
Source23: https://registry.npmjs.org/globals/-/globals-9.18.0.tgz
Source24: https://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source25: https://registry.npmjs.org/home-or-tmp/-/home-or-tmp-2.0.0.tgz
Source26: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source27: https://registry.npmjs.org/is-finite/-/is-finite-1.0.2.tgz
Source28: https://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source29: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source30: https://registry.npmjs.org/jsesc/-/jsesc-1.3.0.tgz
Source31: https://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source32: https://registry.npmjs.org/lodash/-/lodash-4.17.15.tgz
Source33: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source34: https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz
Source35: https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source36: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source37: https://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source38: https://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz
Source39: https://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz
Source40: https://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz
Source41: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source42: https://registry.npmjs.org/private/-/private-0.1.8.tgz
Source43: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.1.tgz
Source44: https://registry.npmjs.org/repeating/-/repeating-2.0.1.tgz
Source45: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source46: https://registry.npmjs.org/slash/-/slash-1.0.0.tgz
Source47: https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz
Source48: https://registry.npmjs.org/source-map-support/-/source-map-support-0.4.18.tgz
Source49: https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source50: https://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source51: https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-1.0.3.tgz
Source52: https://registry.npmjs.org/trim-right/-/trim-right-1.0.1.tgz
Source53: nodejs-babel-register-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(ansi-regex)) = 2.1.1
Provides: bundled(npm(ansi-styles)) = 2.2.1
Provides: bundled(npm(babel-code-frame)) = 6.26.0
Provides: bundled(npm(babel-core)) = 6.26.3
Provides: bundled(npm(babel-generator)) = 6.26.1
Provides: bundled(npm(babel-helpers)) = 6.24.1
Provides: bundled(npm(babel-messages)) = 6.23.0
Provides: bundled(npm(babel-register)) = 6.26.0
Provides: bundled(npm(babel-runtime)) = 6.26.0
Provides: bundled(npm(babel-template)) = 6.26.0
Provides: bundled(npm(babel-traverse)) = 6.26.0
Provides: bundled(npm(babel-types)) = 6.26.0
Provides: bundled(npm(babylon)) = 6.18.0
Provides: bundled(npm(balanced-match)) = 1.0.0
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(chalk)) = 1.1.3
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(convert-source-map)) = 1.6.0
Provides: bundled(npm(core-js)) = 2.6.9
Provides: bundled(npm(debug)) = 2.6.9
Provides: bundled(npm(detect-indent)) = 4.0.0
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(esutils)) = 2.0.3
Provides: bundled(npm(globals)) = 9.18.0
Provides: bundled(npm(has-ansi)) = 2.0.0
Provides: bundled(npm(home-or-tmp)) = 2.0.0
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(is-finite)) = 1.0.2
Provides: bundled(npm(js-tokens)) = 3.0.2
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(jsesc)) = 1.3.0
Provides: bundled(npm(json5)) = 0.5.1
Provides: bundled(npm(lodash)) = 4.17.15
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(minimatch)) = 3.0.4
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(ms)) = 2.0.0
Provides: bundled(npm(number-is-nan)) = 1.0.1
Provides: bundled(npm(os-homedir)) = 1.0.2
Provides: bundled(npm(os-tmpdir)) = 1.0.2
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(private)) = 0.1.8
Provides: bundled(npm(regenerator-runtime)) = 0.11.1
Provides: bundled(npm(repeating)) = 2.0.1
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(slash)) = 1.0.0
Provides: bundled(npm(source-map)) = 0.5.7
Provides: bundled(npm(source-map-support)) = 0.4.18
Provides: bundled(npm(strip-ansi)) = 3.0.1
Provides: bundled(npm(supports-color)) = 2.0.0
Provides: bundled(npm(to-fast-properties)) = 1.0.3
Provides: bundled(npm(trim-right)) = 1.0.1
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

%setup -T -q -a 53 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
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
* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.26.0-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.26.0-2
- Update specs to handle SCL

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.26.0-1
- new package built with tito
