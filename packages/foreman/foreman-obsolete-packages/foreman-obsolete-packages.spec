Name: foreman-obsolete-packages
Version: 1.18
Release: 1%{?dist}
License: MIT
Summary: A package to obsolete retired packages
URL: https://github.com/theforeman/foreman-packaging
BuildArch: noarch

Obsoletes: rubygem-dalli < 2.7.6-4
Obsoletes: rubygem-fog-google < 1.19.0-2
Obsoletes: rubygem-foreman_column_view < 0.4.0-7
Obsoletes: rubygem-foreman_hooks < 0.3.17-4
Obsoletes: rubygem-foreman_memcache < 0.1.1-6
Obsoletes: rubygem-foreman_setup < 8.0.1-3
Obsoletes: rubygem-google-api-client < 0.33.2-3
Obsoletes: rubygem-quantile < 0.2.0-6
Obsoletes: rubygem-request_store < 1.6.0-2
Obsoletes: rubygem-runcible < 2.13.1-3
Obsoletes: rubygem-unf < 0.1.4-2
Obsoletes: rubygem-unf_ext < 0.0.8.2-2
Obsoletes: rubygem-anemone < 0.7.2-2
Obsoletes: rubygem-fog-ovirt < 2.0.3-1
Obsoletes: rubygem-ovirt-engine-sdk < 4.6.0-1
Obsoletes: rubygem-hammer_cli_foreman_admin < 1.2.2
Obsoletes: rubygem-hammer_cli_foreman_admin-doc < 1.2.2
Obsoletes: rubygem-ruby_parser < 3.21.1-4
Obsoletes: rubygem-ruby_parser-doc < 3.21.1-4
Obsoletes: rubygem-hammer_cli_foreman_virt_who_configure < 0.1.4
Obsoletes: rubygem-stomp < 1.4.10-2
Obsoletes: rubygem-stomp-doc < 1.4.10-2
Obsoletes: rubygem-coffee-rails < 5.0.1
Obsoletes: rubygem-coffee-rails-doc < 5.0.1
Obsoletes: rubygem-coffee-script < 2.4.2
Obsoletes: rubygem-coffee-script-doc < 2.4.2
Obsoletes: rubygem-coffee-script-source < 1.12.3
Obsoletes: rubygem-coffee-script-source-doc < 1.12.3
Obsoletes: rubygem-apipie-params < 0.0.6
Obsoletes: rubygem-apipie-params-doc < 0.0.6
Obsoletes: rubygem-declarative-option < 0.1.1
Obsoletes: rubygem-declarative-option-doc < 0.1.1
Obsoletes: rubygem-google-apis-dns_v1 < 0.28.1
Obsoletes: rubygem-google-apis-dns_v1-doc < 0.28.1
Obsoletes: rubygem-google-apis-iamcredentials_v1 < 0.16.1
Obsoletes: rubygem-google-apis-iamcredentials_v1-doc < 0.16.1
Obsoletes: rubygem-google-apis-monitoring_v3 < 0.37.1
Obsoletes: rubygem-google-apis-monitoring_v3-doc < 0.37.1
Obsoletes: rubygem-google-apis-pubsub_v1 < 0.31.1
Obsoletes: rubygem-google-apis-pubsub_v1-doc < 0.31.1
Obsoletes: rubygem-google-apis-sqladmin_v1beta4 < 0.39.1
Obsoletes: rubygem-google-apis-sqladmin_v1beta4-doc < 0.39.1
Obsoletes: rubygem-google-apis-storage_v1 < 0.20.1
Obsoletes: rubygem-google-apis-storage_v1-doc < 0.20.1
Obsoletes: rubygem-uglifier < 4.2.1
Obsoletes: rubygem-uglifier-doc < 4.2.1

%description
This package exists only to obsolete other packages which need to be removed
from the distribution for some reason.

%prep

%build

%install

%files

%changelog
* Wed Jul 22 2026 Zach Huntington-Meath <zhunting@redhat.com> - 1.18-1
- Re-add rubygem-colorize and rubygem-method_source (still needed)

* Wed Jul 22 2026 Zach Huntington-Meath <zhunting@redhat.com> - 1.17-1
- Obsolete orphaned packages: google-apis-dns_v1, google-apis-iamcredentials_v1,
  google-apis-monitoring_v3, google-apis-pubsub_v1, google-apis-sqladmin_v1beta4,
  google-apis-storage_v1, uglifier, colorize, apipie-params, declarative-option,
  method_source

* Tue Jul 14 2026 Zach Huntington-Meath <zhunting@redhat.com> - 1.16-1
- Obsolete rubygem-coffee-rails, rubygem-coffee-script, rubygem-coffee-script-source

* Mon Jun 22 2026 Ondřej Gajdušek <ogajduse@redhat.com> - 1.15-1
- Obsolete rubygem-stomp

* Mon Jun 08 2026 Chris Roberts <chrobert@redhat.com> - 1.14-1
- Obsolete rubygem-hammer_cli_foreman_virt_who_configure

* Mon Jun 01 2026 Ondřej Gajdušek <ogajduse@redhat.com> - 1.13-1
- Obsolete rubygem-ruby_parser

* Mon May 18 2026 Archana Kumari <akumari@redhat.com> - 1.12-1
- Obsolete rubygem-hammer_cli_foreman_admin

* Tue Apr 01 2025 Leos Stejskal - 1.11-1
- Obsolete oVirt

* Mon Aug 05 2024 Samir Jha - 1.10-1
- Obsolete rubygem-anemone

* Tue Apr 30 2024 Evgeni Golov - 1.9-1
- Obsolete rubygem-request_store

* Tue Mar 26 2024 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.8-1
- Obsolete foreman_setup

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
