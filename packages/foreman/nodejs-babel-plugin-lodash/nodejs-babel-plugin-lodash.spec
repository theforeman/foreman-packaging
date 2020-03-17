%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name babel-plugin-lodash

Name: %{?scl_prefix}nodejs-babel-plugin-lodash
Version: 3.3.4
Release: 4%{?dist}
Summary: Modular Lodash builds without the hassle
License: MIT
Group: Development/Libraries
URL: https://github.com/lodash/babel-plugin-lodash#readme
Source0: https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.0.0.tgz
Source1: https://registry.npmjs.org/@babel/types/-/types-7.6.1.tgz
Source2: https://registry.npmjs.org/babel-plugin-lodash/-/babel-plugin-lodash-3.3.4.tgz
Source3: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz
Source4: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source5: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source6: https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
Source7: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source8: https://registry.npmjs.org/glob/-/glob-7.1.4.tgz
Source9: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source10: https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz
Source11: https://registry.npmjs.org/lodash/-/lodash-4.17.15.tgz
Source12: https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz
Source13: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source14: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source15: https://registry.npmjs.org/require-package-name/-/require-package-name-2.0.1.tgz
Source16: https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-2.0.0.tgz
Source17: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source18: nodejs-babel-plugin-lodash-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/helper-module-imports)) = 7.0.0
Provides: bundled(npm(@babel/types)) = 7.6.1
Provides: bundled(npm(babel-plugin-lodash)) = 3.3.4
Provides: bundled(npm(balanced-match)) = 1.0.0
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(esutils)) = 2.0.3
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(glob)) = 7.1.4
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.4
Provides: bundled(npm(lodash)) = 4.17.15
Provides: bundled(npm(minimatch)) = 3.0.4
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(require-package-name)) = 2.0.1
Provides: bundled(npm(to-fast-properties)) = 2.0.0
Provides: bundled(npm(wrappy)) = 1.0.2
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

%setup -T -q -a 18 -D -n %{npm_cache_dir}

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
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.3.4-4
- Bump packages to build for el8

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.3.4-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.3.4-2
- Update specs to handle SCL

* Tue Jun 19 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.3.4-1
- Update to 3.3.4

* Wed Jan 03 2018 Daniel Lobato Garcia <me@daniellobato.me> 3.3.2-1
- new package built with tito
