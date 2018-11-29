%global npm_name react-router

Name: nodejs-%{npm_name}
Version: 4.3.1
Release: 1%{?dist}
Summary: Declarative routing for React
License: MIT
Group: Development/Libraries
URL: https://github.com/ReactTraining/react-router#readme
Source0: https://registry.npmjs.org/react-router/-/react-router-4.3.1.tgz
Source1: https://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source2: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source3: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-2.5.0.tgz
Source4: https://registry.npmjs.org/warning/-/warning-4.0.1.tgz
Source5: https://registry.npmjs.org/prop-types/-/prop-types-15.6.1.tgz
Source6: https://registry.npmjs.org/history/-/history-4.7.2.tgz
Source7: https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-1.7.0.tgz
Source8: https://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source9: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source10: https://registry.npmjs.org/fbjs/-/fbjs-0.8.16.tgz
Source11: https://registry.npmjs.org/resolve-pathname/-/resolve-pathname-2.2.0.tgz
Source12: https://registry.npmjs.org/value-equal/-/value-equal-0.4.0.tgz
Source13: https://registry.npmjs.org/isarray/-/isarray-0.0.1.tgz
Source14: https://registry.npmjs.org/warning/-/warning-3.0.0.tgz
Source15: https://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source16: https://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source17: https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source18: https://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.18.tgz
Source19: https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-2.0.4.tgz
Source20: https://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source21: https://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source22: https://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source23: https://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source24: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source25: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.23.tgz
Source26: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source27: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(asap)) = 2.0.6
Provides: bundled(npm(core-js)) = 1.2.7
Provides: bundled(npm(encoding)) = 0.1.12
Provides: bundled(npm(fbjs)) = 0.8.16
Provides: bundled(npm(history)) = 4.7.2
Provides: bundled(npm(hoist-non-react-statics)) = 2.5.0
Provides: bundled(npm(iconv-lite)) = 0.4.23
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(isarray)) = 0.0.1
Provides: bundled(npm(isomorphic-fetch)) = 2.2.1
Provides: bundled(npm(js-tokens)) = 3.0.2
Provides: bundled(npm(loose-envify)) = 1.3.1
Provides: bundled(npm(node-fetch)) = 1.7.3
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(path-to-regexp)) = 1.7.0
Provides: bundled(npm(promise)) = 7.3.1
Provides: bundled(npm(prop-types)) = 15.6.1
Provides: bundled(npm(react-router)) = 4.3.1
Provides: bundled(npm(resolve-pathname)) = 2.2.0
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(setimmediate)) = 1.0.5
Provides: bundled(npm(ua-parser-js)) = 0.7.18
Provides: bundled(npm(value-equal)) = 0.4.0
Provides: bundled(npm(warning)) = 3.0.0
Provides: bundled(npm(warning)) = 4.0.1
Provides: bundled(npm(whatwg-fetch)) = 2.0.4
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
%setup -T -q -a 27 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/MemoryRouter.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/Prompt.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/Redirect.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/Route.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/Router.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/StaticRouter.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/Switch.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/es %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/generatePath.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/matchPath.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/umd %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/withRouter.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Jun 07 2018 Eric D. Helms <ericdhelms@gmail.com> 4.3.1-1
- Update to 4.3.1

* Sun Apr 22 2018 Eric D. Helms <ericdhelms@gmail.com> 4.2.0-1
- Add nodejs-react-router generated by npm2rpm using the bundle strategy

