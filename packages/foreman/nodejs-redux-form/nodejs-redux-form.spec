%global npm_name redux-form

Name: nodejs-redux-form
Version: 8.2.0
Release: 1%{?dist}
Summary: A higher order component decorator for forms using Redux and React
License: MIT
Group: Development/Libraries
URL: https://redux-form.com/
Source0: https://registry.npmjs.org/redux-form/-/redux-form-8.2.0.tgz
Source1: https://registry.npmjs.org/es6-error/-/es6-error-4.1.1.tgz
Source2: https://registry.npmjs.org/is-promise/-/is-promise-2.1.0.tgz
Source3: https://registry.npmjs.org/lodash-es/-/lodash-es-4.17.11.tgz
Source4: https://registry.npmjs.org/prop-types/-/prop-types-15.7.2.tgz
Source5: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source6: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-3.3.0.tgz
Source7: https://registry.npmjs.org/@babel/runtime/-/@babel/runtime-7.4.4.tgz
Source8: https://registry.npmjs.org/lodash/-/lodash-4.17.11.tgz
Source9: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source10: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source11: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.13.2.tgz
Source12: https://registry.npmjs.org/react-lifecycles-compat/-/react-lifecycles-compat-3.0.4.tgz
Source13: https://registry.npmjs.org/react-is/-/react-is-16.8.6.tgz
Source14: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source15: %{name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/runtime)) = 7.4.4
Provides: bundled(npm(es6-error)) = 4.1.1
Provides: bundled(npm(hoist-non-react-statics)) = 3.3.0
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(is-promise)) = 2.1.0
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(lodash)) = 4.17.11
Provides: bundled(npm(lodash-es)) = 4.17.11
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.7.2
Provides: bundled(npm(react-is)) = 16.8.6
Provides: bundled(npm(react-lifecycles-compat)) = 3.0.4
Provides: bundled(npm(redux-form)) = 8.2.0
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
%setup -T -q -a 15 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/es %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/immutable.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu May 02 2019 Ondrej Prazak <oprazak@redhat.com> 8.2.0-1
- Update to 8.2.0

* Thu Jan 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 7.2.0-1
- Update redux-form to 7.1.2 (me@daniellobato.me)

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 7.1.2-1
- new package built with tito

