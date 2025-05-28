%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name sass-loader

Name: %{?scl_prefix}nodejs-sass-loader
Version: 13.3.3
Release: 2%{?dist}
Summary: Sass loader for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack-contrib/sass-loader
Source0: https://registry.npmjs.org/neo-async/-/neo-async-2.6.2.tgz
Source1: https://registry.npmjs.org/sass-loader/-/sass-loader-13.3.3.tgz
Source2: nodejs-sass-loader-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(neo-async)) = 2.6.2
Provides: bundled(npm(sass-loader)) = 13.3.3
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

%setup -T -q -a 2 -D -n %{npm_cache_dir}

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
* Thu Feb 01 2024 Eric D. Helms <ericdhelms@gmail.com> - 13.3.3-2
- Use --legacy-peer-deps during npm install

* Fri Jan 26 2024 Foreman Packaging Automation <packaging@theforeman.org> 13.3.3-1
- Update to 13.3.3

* Wed Dec 13 2023 Evgeni Golov 13.3.2-1
- Update to 13.3.2

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 6.0.7-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.0.7-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.0.7-2
- Update specs to handle SCL

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 6.0.7-1
- Update to 6.0.7

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.0.6-1
- Update nodejs-sass-loader to 6.0.6 (ewoud@kohlvanwijngaarden.nl)

* Tue Feb 28 2017 Dominic Cleal <dominic@cleal.org> 4.1.1-1
- new package built with tito
