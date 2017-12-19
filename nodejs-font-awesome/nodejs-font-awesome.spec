%global npm_name font-awesome
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 4.7.0
Release: 1%{?dist}
Summary: The iconic font and CSS framework
License: (OFL-1.1 AND MIT)
Group: Development/Libraries
URL: http://fontawesome.io/
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
cp -pfr css %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr fonts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr less %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr scss %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc HELP-US-OUT.txt
%doc README.md

%changelog
