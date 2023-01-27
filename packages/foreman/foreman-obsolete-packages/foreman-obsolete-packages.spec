Name: foreman-obsolete-packages
Version: 0.9
Release: 1%{?dist}
License: MIT
Summary: A package to obsolete retired packages
URL: https://github.com/theforeman/foreman-packaging
BuildArch: noarch

Obsoletes: rubygem-google-api-client < 0.33.2-3

%description
This package exists only to obsolete other packages which need to be removed
from the distribution for some reason.

%prep

%build

%install

%files

%changelog
* Fri Jan 27 2023 Evgeni Golov - 0.9-1
- Backport to 3.4 branch, keeping the google-api-client obsolete,
  but dropping the fog-google one
