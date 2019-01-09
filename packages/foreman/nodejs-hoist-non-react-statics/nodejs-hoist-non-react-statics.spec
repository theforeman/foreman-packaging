%global npm_name hoist-non-react-statics

Name: nodejs-hoist-non-react-statics
Version: 2.5.5
Release: 1%{?dist}
Summary: Copies non-react specific statics from a child component to a parent component
License: BSD-3-Clause
Group: Development/Libraries
URL: https://github.com/mridgway/hoist-non-react-statics#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.md
%doc README.md

%changelog
* Wed Jan 09 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.5.5-1
- Update to 2.5.5

* Tue Dec 19 2017 Daniel Lobato Garcia <me@daniellobato.me> 2.3.1-1
- new package built with tito

