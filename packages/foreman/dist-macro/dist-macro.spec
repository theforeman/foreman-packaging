%define base_release_version 7
%define dist .el%{base_release_version}

Name:     dist-macro
Version:  1.0
Release:  1

Summary:  Package to define the dist macro
Group:    System Environment/Base
License:  GPLv3+
URL:      https://theforeman.org

BuildArch: noarch

%description
Sets the dist macro to basic distribution and major version.

%install
install -d -m 755 %{buildroot}/etc/rpm
cat >> %{buildroot}/etc/rpm/dist-macro.dist << EOF
%%rhel %{base_release_version}
%%dist %dist
%%el%{base_release_version} 1
EOF

%files
/etc/rpm/dist-macro.dist

%changelog
* Thu Sep 06 2018 Eric D. Helms <ericdhelms@gmail.com> 1.0-1
- Initial release to set dist macro

