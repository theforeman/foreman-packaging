Name: foreman-obsolete-packages
Version: 1.7
Release: 1%{?dist}
License: MIT
Summary: A package to obsolete retired packages
URL: https://github.com/theforeman/foreman-packaging
BuildArch: noarch

Obsoletes: rubygem-fog-google < 1.19.0-2
Obsoletes: rubygem-foreman_hooks < 0.3.17-4
Obsoletes: rubygem-google-api-client < 0.33.2-3
Obsoletes: rubygem-dalli < 2.7.6-4
Obsoletes: rubygem-foreman_memcache < 0.1.1-6
Obsoletes: rubygem-quantile < 0.2.0-6
Obsoletes: rubygem-runcible < 2.13.1-3
Obsoletes: rubygem-foreman_column_view < 0.4.0-7
Obsoletes: rubygem-unf < 0.1.4-2
Obsoletes: rubygem-unf_ext < 0.0.8.2-2

%description
This package exists only to obsolete other packages which need to be removed
from the distribution for some reason.

%prep

%build

%install

%files

%changelog
* Mon Mar 25 2024 Adam Ruzicka - 1.7-1
- Obsolete rubygem-foreman_hooks

* Thu Nov 16 2023 Evgeni Golov - 1.6-1
- Obsolete rubygem-unf and rubygem-unf_ext

* Wed May 10 2023 Dirk Goetz <dirk.goetz@netways.de> - 1.5-1
- Obsolete rubygem-foreman_column_view

* Thu May 04 2023 Evgeni Golov - 1.4-1
- Obsolete rubygem-runcible

* Tue Apr 04 2023 Evgeni Golov - 1.3-1
- Obsolete rubygem-quantile

* Wed Mar 01 2023 Evgeni Golov - 1.2-1
- Obsolete foreman_memcache and dalli

* Fri Jan 20 2023 Evgeni Golov - 1.1-1
- Obsolete rubygem-google-api-client < 0.33.2-3
- Mark the package as noarch

* Fri Nov 11 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0-1
- Initial package
