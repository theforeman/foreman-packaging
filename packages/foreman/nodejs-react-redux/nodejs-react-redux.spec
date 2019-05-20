%global npm_name react-redux

Name: nodejs-react-redux
Version: 5.1.1
Release: 1%{?dist}
Summary: Official React bindings for Redux
License: MIT
Group: Development/Libraries
URL: https://github.com/reduxjs/react-redux
Source0: https://registry.npmjs.org/react-redux/-/react-redux-5.1.1.tgz
Source1: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source2: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-3.3.0.tgz
Source3: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source4: https://registry.npmjs.org/prop-types/-/prop-types-15.7.2.tgz
Source5: https://registry.npmjs.org/@babel/runtime/-/@babel/runtime-7.4.4.tgz
Source6: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source7: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source8: https://registry.npmjs.org/react-is/-/react-is-16.8.6.tgz
Source9: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.13.2.tgz
Source10: https://registry.npmjs.org/react-lifecycles-compat/-/react-lifecycles-compat-3.0.4.tgz
Source11: %{name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/runtime)) = 7.4.4
Provides: bundled(npm(hoist-non-react-statics)) = 3.3.0
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.7.2
Provides: bundled(npm(react-is)) = 16.8.6
Provides: bundled(npm(react-lifecycles-compat)) = 3.0.4
Provides: bundled(npm(react-redux)) = 5.1.1
Provides: bundled(npm(regenerator-runtime)) = 0.13.2
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
%setup -T -q -a 11 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/es %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE.md
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Mon May 20 2019 Avi Sharvit <asharvit@redhat.com> 5.1.1-1
- Update to 5.1.1

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 5.0.7-1
- Update to 5.0.7

* Fri Nov 17 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.0.6-1
- Bump nodejs-react-redux to 5.0.6 (ewoud@kohlvanwijngaarden.nl)

* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 5.0.2-2
- Use existing react, redux peer dependencies (dominic@cleal.org)

* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 5.0.2-1
- new package built with tito

