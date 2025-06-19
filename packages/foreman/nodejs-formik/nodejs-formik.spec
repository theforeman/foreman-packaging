%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name formik

Name: %{?scl_prefix}nodejs-formik
Version: 1.5.8
Release: 1%{?dist}
Summary: Forms in React, without tears
License: MIT
Group: Development/Libraries
URL: https://github.com/jaredpalmer/formik#readme
Source0: https://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source1: https://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source2: https://registry.npmjs.org/create-react-context/-/create-react-context-0.2.3.tgz
Source3: https://registry.npmjs.org/deepmerge/-/deepmerge-2.2.1.tgz
Source4: https://registry.npmjs.org/encoding/-/encoding-0.1.13.tgz
Source5: https://registry.npmjs.org/fbjs/-/fbjs-0.8.18.tgz
Source6: https://registry.npmjs.org/formik/-/formik-1.5.8.tgz
Source7: https://registry.npmjs.org/gud/-/gud-1.0.0.tgz
Source8: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-3.3.2.tgz
Source9: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.6.3.tgz
Source10: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source11: https://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source12: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source13: https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz
Source14: https://registry.npmjs.org/lodash-es/-/lodash-es-4.17.21.tgz
Source15: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source16: https://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source17: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source18: https://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source19: https://registry.npmjs.org/prop-types/-/prop-types-15.8.1.tgz
Source20: https://registry.npmjs.org/react-fast-compare/-/react-fast-compare-2.0.4.tgz
Source21: https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz
Source22: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source23: https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source24: https://registry.npmjs.org/tiny-warning/-/tiny-warning-1.0.3.tgz
Source25: https://registry.npmjs.org/tslib/-/tslib-1.14.1.tgz
Source26: https://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.40.tgz
Source27: https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-3.6.20.tgz
Source28: nodejs-formik-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(asap)) = 2.0.6
Provides: bundled(npm(core-js)) = 1.2.7
Provides: bundled(npm(create-react-context)) = 0.2.3
Provides: bundled(npm(deepmerge)) = 2.2.1
Provides: bundled(npm(encoding)) = 0.1.13
Provides: bundled(npm(fbjs)) = 0.8.18
Provides: bundled(npm(formik)) = 1.5.8
Provides: bundled(npm(gud)) = 1.0.0
Provides: bundled(npm(hoist-non-react-statics)) = 3.3.2
Provides: bundled(npm(iconv-lite)) = 0.6.3
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(isomorphic-fetch)) = 2.2.1
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(lodash-es)) = 4.17.21
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(node-fetch)) = 1.7.3
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(promise)) = 7.3.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-fast-compare)) = 2.0.4
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(setimmediate)) = 1.0.5
Provides: bundled(npm(tiny-warning)) = 1.0.3
Provides: bundled(npm(tslib)) = 1.14.1
Provides: bundled(npm(ua-parser-js)) = 0.7.40
Provides: bundled(npm(whatwg-fetch)) = 3.6.20
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

%setup -T -q -a 28 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --legacy-peer-deps --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Jun 19 2025 MariaAga <mariaaga@redhat.com> 1.5.8-1
- Add nodejs-formik generated by npm2rpm using the bundle strategy

