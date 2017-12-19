%global npm_name hoist-non-react-statics
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 2.3.1
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
cp -pfr index.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.md
%doc README.md

%changelog
