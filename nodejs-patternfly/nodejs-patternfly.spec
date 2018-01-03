%global npm_name patternfly
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 3.32.1
Release: 1%{?dist}
Summary: A reference implementation of PatternFly based on Bootstrap v3
License: Apache-2.0
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(bootstrap) >= 3.3.7
Requires: npm(bootstrap) < 3.4.0
Requires: npm(bootstrap-datepicker) >= 1.6.4
Requires: npm(bootstrap-datepicker) < 1.7.0
Requires: npm(bootstrap-sass) >= 3.3.7
Requires: npm(bootstrap-sass) < 4.0.0
Requires: npm(bootstrap-select) >= 1.12.2
Requires: npm(bootstrap-select) < 2.0.0
Requires: npm(bootstrap-slider) >= 9.9.0
Requires: npm(bootstrap-slider) < 10.0.0
Requires: npm(bootstrap-switch) >= 3.3.4
Requires: npm(bootstrap-switch) < 3.4.0
Requires: npm(bootstrap-touchspin) >= 3.1.1
Requires: npm(bootstrap-touchspin) < 3.2.0
Requires: npm(c3) >= 0.4.11
Requires: npm(c3) < 0.5.0
Requires: npm(d3) >= 3.5.17
Requires: npm(d3) < 3.6.0
Requires: npm(datatables.net) >= 1.10.15
Requires: npm(datatables.net) < 2.0.0
Requires: npm(datatables.net-colreorder) >= 1.3.2
Requires: npm(datatables.net-colreorder) < 1.4.0
Requires: npm(datatables.net-colreorder-bs) >= 1.3.2
Requires: npm(datatables.net-colreorder-bs) < 1.4.0
Requires: npm(datatables.net-select) >= 1.2.0
Requires: npm(datatables.net-select) < 1.3.0
Requires: npm(drmonty-datatables-colvis) >= 1.1.2
Requires: npm(drmonty-datatables-colvis) < 1.2.0
Requires: npm(eonasdan-bootstrap-datetimepicker) >= 4.17.47
Requires: npm(eonasdan-bootstrap-datetimepicker) < 5.0.0
Requires: npm(font-awesome) >= 4.7.0
Requires: npm(font-awesome) < 5.0.0
Requires: npm(font-awesome-sass) >= 4.7.0
Requires: npm(font-awesome-sass) < 5.0.0
Requires: npm(google-code-prettify) >= 1.0.5
Requires: npm(google-code-prettify) < 1.1.0
Requires: npm(jquery) >= 3.2.1
Requires: npm(jquery) < 3.3.0
Requires: npm(jquery-match-height) >= 0.7.2
Requires: npm(jquery-match-height) < 1.0.0
Requires: npm(moment) >= 2.14.1
Requires: npm(moment) < 2.15.0
Requires: npm(moment-timezone) >= 0.4.1
Requires: npm(moment-timezone) < 1.0.0
Requires: npm(patternfly-bootstrap-combobox) >= 1.1.7
Requires: npm(patternfly-bootstrap-combobox) < 1.2.0
Requires: npm(patternfly-bootstrap-treeview) >= 2.1.0
Requires: npm(patternfly-bootstrap-treeview) < 2.2.0
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
cp -pfr tests %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.txt
%doc README.md

%changelog
* Wed Nov 08 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.29.13-1
- new package built with tito

