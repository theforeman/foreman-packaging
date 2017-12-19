%global npm_name patternfly-bootstrap-treeview
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 2.1.5
Release: 1%{?dist}
Summary: Tree View for Twitter Bootstrap
License: Apache-2.0
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly-bootstrap-treeview
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(bootstrap) >= 3.3.0
Requires: npm(bootstrap) < 3.4.0
Requires: npm(jquery) >= 2.1.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr tests %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%doc public

%changelog
