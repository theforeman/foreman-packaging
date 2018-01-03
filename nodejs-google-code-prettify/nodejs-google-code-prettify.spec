%global npm_name google-code-prettify
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.0.5
Release: 1%{?dist}
Summary: Javascript code prettifier
License: Apache-2.0
Group: Development/Libraries
URL: https://github.com/mattdsteele/google-code-prettify
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
cp -pfr bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr styles %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license COPYING
%doc CHANGES.html
%doc README-zh-Hans.html
%doc README.html
%doc README.md
%doc examples

%changelog
