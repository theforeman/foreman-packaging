%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name react-router-dom

Name: %{?scl_prefix}nodejs-react-router-dom
Version: 5.1.2
Release: 1%{?dist}
Summary: DOM bindings for React Router
License: MIT
Group: Development/Libraries
URL: https://github.com/ReactTraining/react-router#readme
Source0: https://registry.npmjs.org/@babel/runtime/-/runtime-7.27.6.tgz
Source1: https://registry.npmjs.org/history/-/history-4.10.1.tgz
Source2: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-3.3.2.tgz
Source3: https://registry.npmjs.org/isarray/-/isarray-0.0.1.tgz
Source4: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source5: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source6: https://registry.npmjs.org/mini-create-react-context/-/mini-create-react-context-0.3.3.tgz
Source7: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source8: https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-1.9.0.tgz
Source9: https://registry.npmjs.org/prop-types/-/prop-types-15.8.1.tgz
Source10: https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz
Source11: https://registry.npmjs.org/react-router/-/react-router-5.1.2.tgz
Source12: https://registry.npmjs.org/react-router-dom/-/react-router-dom-5.1.2.tgz
Source13: https://registry.npmjs.org/resolve-pathname/-/resolve-pathname-3.0.0.tgz
Source14: https://registry.npmjs.org/tiny-invariant/-/tiny-invariant-1.3.3.tgz
Source15: https://registry.npmjs.org/tiny-warning/-/tiny-warning-1.0.3.tgz
Source16: https://registry.npmjs.org/value-equal/-/value-equal-1.0.1.tgz
Source17: nodejs-react-router-dom-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/runtime)) = 7.27.6
Provides: bundled(npm(history)) = 4.10.1
Provides: bundled(npm(hoist-non-react-statics)) = 3.3.2
Provides: bundled(npm(isarray)) = 0.0.1
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(mini-create-react-context)) = 0.3.3
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(path-to-regexp)) = 1.9.0
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(react-router)) = 5.1.2
Provides: bundled(npm(react-router-dom)) = 5.1.2
Provides: bundled(npm(resolve-pathname)) = 3.0.0
Provides: bundled(npm(tiny-invariant)) = 1.3.3
Provides: bundled(npm(tiny-warning)) = 1.0.3
Provides: bundled(npm(value-equal)) = 1.0.1
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

%setup -T -q -a 17 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --legacy-peer-deps --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/BrowserRouter.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/HashRouter.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/Link.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/MemoryRouter.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/NavLink.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/Prompt.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/Redirect.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/Route.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/Router.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/StaticRouter.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/Switch.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/cjs %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/es %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/esm %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/generatePath.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/matchPath.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/umd %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/warnAboutDeprecatedCJSRequire.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/withRouter.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Sun Jun 29 2025 root <root> 5.1.2-1
- Add nodejs-react-router-dom generated by npm2rpm using the bundle strategy

