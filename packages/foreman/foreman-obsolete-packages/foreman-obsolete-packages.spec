Name: foreman-obsolete-packages
Version: 1.0
Release: 1%{?dist}
License: MIT
Summary: A package to obsolete retired packages
URL: https://github.com/theforeman/foreman-packaging

Obsoletes: rubygem-fog-google < 1.19.0-2

%description
This package exists only to obsolete other packages which need to be removed
from the distribution for some reason.

%prep

%build

%install

%files

%changelog
* Fri Nov 11 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0-1
- Initial package
