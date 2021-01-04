%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @redhat-cloud-services/frontend-components

Name: %{?scl_prefix}nodejs-redhat-cloud-services-frontend-components
Version: 2.5.0
Release: 1%{?dist}
Summary: Common components for RedHat Cloud Services project
License: Apache-2.0
Group: Development/Libraries
URL: https://github.com/RedHatInsights/frontend-components/tree/master/packages/components#readme
Source0: https://registry.npmjs.org/@redhat-cloud-services/frontend-components/-/frontend-components-2.5.0.tgz
Source1: https://registry.npmjs.org/@redhat-cloud-services/frontend-components-utilities/-/frontend-components-utilities-2.2.8.tgz
Source2: https://registry.npmjs.org/@scalprum/core/-/core-0.0.8.tgz
Source3: https://registry.npmjs.org/@scalprum/core/-/core-0.0.9.tgz
Source4: https://registry.npmjs.org/@scalprum/react-core/-/react-core-0.0.7.tgz
Source5: https://registry.npmjs.org/@sentry/browser/-/browser-5.29.2.tgz
Source6: https://registry.npmjs.org/@sentry/core/-/core-5.29.2.tgz
Source7: https://registry.npmjs.org/@sentry/hub/-/hub-5.29.2.tgz
Source8: https://registry.npmjs.org/@sentry/minimal/-/minimal-5.29.2.tgz
Source9: https://registry.npmjs.org/@sentry/types/-/types-5.29.2.tgz
Source10: https://registry.npmjs.org/@sentry/utils/-/utils-5.29.2.tgz
Source11: https://registry.npmjs.org/@types/debounce-promise/-/debounce-promise-3.1.3.tgz
Source12: https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz
Source13: https://registry.npmjs.org/awesome-debounce-promise/-/awesome-debounce-promise-2.1.0.tgz
Source14: https://registry.npmjs.org/awesome-imperative-promise/-/awesome-imperative-promise-1.0.1.tgz
Source15: https://registry.npmjs.org/awesome-only-resolves-last-promise/-/awesome-only-resolves-last-promise-1.0.3.tgz
Source16: https://registry.npmjs.org/axios/-/axios-0.19.2.tgz
Source17: https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz
Source18: https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz
Source19: https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz
Source20: https://registry.npmjs.org/commander/-/commander-6.2.1.tgz
Source21: https://registry.npmjs.org/debounce-promise/-/debounce-promise-3.1.2.tgz
Source22: https://registry.npmjs.org/debug/-/debug-3.1.0.tgz
Source23: https://registry.npmjs.org/dom-serializer/-/dom-serializer-1.2.0.tgz
Source24: https://registry.npmjs.org/domelementtype/-/domelementtype-2.1.0.tgz
Source25: https://registry.npmjs.org/domhandler/-/domhandler-3.3.0.tgz
Source26: https://registry.npmjs.org/domhandler/-/domhandler-4.0.0.tgz
Source27: https://registry.npmjs.org/domutils/-/domutils-2.4.4.tgz
Source28: https://registry.npmjs.org/entities/-/entities-2.1.0.tgz
Source29: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source30: https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.5.10.tgz
Source31: https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz
Source32: https://registry.npmjs.org/htmlparser2/-/htmlparser2-4.1.0.tgz
Source33: https://registry.npmjs.org/lodash/-/lodash-4.17.20.tgz
Source34: https://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source35: https://registry.npmjs.org/parse-srcset/-/parse-srcset-1.0.2.tgz
Source36: https://registry.npmjs.org/postcss/-/postcss-7.0.35.tgz
Source37: https://registry.npmjs.org/react-content-loader/-/react-content-loader-5.1.4.tgz
Source38: https://registry.npmjs.org/sanitize-html/-/sanitize-html-1.27.5.tgz
Source39: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source40: https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz
Source41: https://registry.npmjs.org/supports-color/-/supports-color-6.1.0.tgz
Source42: https://registry.npmjs.org/tslib/-/tslib-1.14.1.tgz
Source43: nodejs-redhat-cloud-services-frontend-components-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@redhat-cloud-services/frontend-components)) = 2.5.0
Provides: bundled(npm(@redhat-cloud-services/frontend-components-utilities)) = 2.2.8
Provides: bundled(npm(@scalprum/core)) = 0.0.8
Provides: bundled(npm(@scalprum/core)) = 0.0.9
Provides: bundled(npm(@scalprum/react-core)) = 0.0.7
Provides: bundled(npm(@sentry/browser)) = 5.29.2
Provides: bundled(npm(@sentry/core)) = 5.29.2
Provides: bundled(npm(@sentry/hub)) = 5.29.2
Provides: bundled(npm(@sentry/minimal)) = 5.29.2
Provides: bundled(npm(@sentry/types)) = 5.29.2
Provides: bundled(npm(@sentry/utils)) = 5.29.2
Provides: bundled(npm(@types/debounce-promise)) = 3.1.3
Provides: bundled(npm(ansi-styles)) = 3.2.1
Provides: bundled(npm(awesome-debounce-promise)) = 2.1.0
Provides: bundled(npm(awesome-imperative-promise)) = 1.0.1
Provides: bundled(npm(awesome-only-resolves-last-promise)) = 1.0.3
Provides: bundled(npm(axios)) = 0.19.2
Provides: bundled(npm(chalk)) = 2.4.2
Provides: bundled(npm(color-convert)) = 1.9.3
Provides: bundled(npm(color-name)) = 1.1.3
Provides: bundled(npm(commander)) = 6.2.1
Provides: bundled(npm(debounce-promise)) = 3.1.2
Provides: bundled(npm(debug)) = 3.1.0
Provides: bundled(npm(dom-serializer)) = 1.2.0
Provides: bundled(npm(domelementtype)) = 2.1.0
Provides: bundled(npm(domhandler)) = 3.3.0
Provides: bundled(npm(domhandler)) = 4.0.0
Provides: bundled(npm(domutils)) = 2.4.4
Provides: bundled(npm(entities)) = 2.1.0
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(follow-redirects)) = 1.5.10
Provides: bundled(npm(has-flag)) = 3.0.0
Provides: bundled(npm(htmlparser2)) = 4.1.0
Provides: bundled(npm(lodash)) = 4.17.20
Provides: bundled(npm(ms)) = 2.0.0
Provides: bundled(npm(parse-srcset)) = 1.0.2
Provides: bundled(npm(postcss)) = 7.0.35
Provides: bundled(npm(react-content-loader)) = 5.1.4
Provides: bundled(npm(sanitize-html)) = 1.27.5
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(supports-color)) = 5.5.0
Provides: bundled(npm(supports-color)) = 6.1.0
Provides: bundled(npm(tslib)) = 1.14.1
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

%setup -T -q -a 43 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/components %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/create-styles.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.css %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/tsconfig.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%doc node_modules/%{npm_name}/README.md

%changelog
* Mon Jan 04 2021 Ron Lavi <1ronlavi@gmail.com> 2.5.0-1
- Add nodejs-redhat-cloud-services-frontend-components generated by npm2rpm using the bundle strategy

