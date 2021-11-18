%global gem_name apipie-bindings

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

Summary: The Ruby bindings for Apipie documented APIs
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.0
Release: 2%{?dist}
Group: Development/Libraries
License: MIT
URL: https://github.com/Apipie/apipie-bindings
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(rest-client) >= 1.6.5
Requires: %{?scl_prefix}rubygem(rest-client) < 3.0.0
Requires: %{?scl_prefix}rubygem(oauth)
Requires: %{?scl_prefix_ruby}rubygem(json) >= 1.2.1
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Bindings for API calls that are documented with Apipie. Bindings are generated on the fly.

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for %{name}

%description doc
This package contains documentation for %{name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/test


%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/doc


%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.4.0-2
- Rebuild against rh-ruby27

* Fri May 29 2020 Oleh Fedorenko <ofedoren@redhat.com> 0.4.0-1
- Update to 0.4.0

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.3.0-2
- Bump to release for EL8

* Mon Oct 28 2019 Evgeni Golov 0.3.0-1
- Update to 0.3.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.2.2-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.2.2-1
- Update apipie-bindings to 0.2.2 (#2063) (martin.bacovsky@gmail.com)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.2.0-2
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Tue Apr 25 2017 Dominic Cleal <dominic@cleal.org> 0.2.0-1
- Update apipie-bindings to 0.2.0 (dominic@cleal.org)

* Tue Mar 28 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.0-1
- Update rubygem-apipie-bindings to 0.1.0 (martin.bacovsky@gmail.com)

* Wed Dec 14 2016 Dominic Cleal <dominic@cleal.org> 0.0.19-1
- Update apipie-bindings to 0.0.19 (dominic@cleal.org)

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.0.18-1
- Update rubygem-apipie-bindings to 0.0.18 (martin.bacovsky@gmail.com)

* Fri Jun 24 2016 Dominic Cleal <dominic@cleal.org> 0.0.17-1
- Update apipie-bindings to 0.0.17 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.0.16-2
- Use gem_install macro (dominic@cleal.org)

* Wed Mar 09 2016 Dominic Cleal <dominic@cleal.org> 0.0.16-1
- Update rubygem-apipie-bindings to 0.0.16 (martin.bacovsky@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.0.14-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.14-1
- update apipie-bindings to 0.0.14 (kvedulv@kvedulv.de)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.0.13-2
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Apr 23 2015 Dominic Cleal <dcleal@redhat.com> 0.0.13-1
- Update apipie-bindings to 0.0.13 (dcleal@redhat.com)

* Mon Mar 23 2015 Dominic Cleal <dcleal@redhat.com> 0.0.12-1
- Update apipie-bindings to 0.0.12 (dcleal@redhat.com)

* Mon Nov 10 2014 Dominic Cleal <dcleal@redhat.com> 0.0.11-1
- Update rubygem-apipie-bindings to 0.0.11 (martin.bacovsky@gmail.com)
- Remove unused fastercsv dependency (dcleal@redhat.com)

* Thu Sep 18 2014 Dominic Cleal <dcleal@redhat.com> 0.0.10-1
- Update rubygem-apipie-bindings to 0.0.10 (dcleal@redhat.com)

* Fri Aug 29 2014 Dominic Cleal <dcleal@redhat.com> 0.0.9-1
- Packaged /doc (martin.bacovsky@gmail.com)
- Update rubygem-apipie-bindings to 0.0.9 (martin.bacovsky@gmail.com)

* Thu Jul 17 2014 Lukas Zapletal <lzap+git@redhat.com> 0.0.8-4
- Fixed dependency in the -doc subpackage (lzap+git@redhat.com)
- Fixed doc subpackages (lzap+git@redhat.com)

* Thu Jul 17 2014 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.8-3
- Fixed dependency in the -doc subpackage

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 0.0.8-2
- Modernise and update for EL7 (dcleal@redhat.com)

* Wed May 07 2014 Martin Bačovský <martin.bacovsky@gmail.com> 0.0.8-1
- Update apipie-bindings to 0.0.8 (martin.bacovsky@gmail.com)

* Wed May 07 2014 Martin Bačovský <martin.bacovsky@gmail.com> 0.0.7-1
- Update apipie-bindings to 0.0.7 (martin.bacovsky@gmail.com)

* Fri Mar 21 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.6-1
- Bump to 0.0.6 (mbacovsk@redhat.com)

* Thu Mar 20 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.5-1
- Bump to 0.0.5 (mbacovsk@redhat.com)

* Wed Mar 19 2014 Jason Montleon <jmontleo@redhat.com> 0.0.4-3
- fix scl package name and provides for apipie-bindings (jmontleo@redhat.com)

* Wed Mar 19 2014 Jason Montleon <jmontleo@redhat.com> 0.0.4-2
- fix scl builds (jmontleo@redhat.com)

* Wed Mar 19 2014 Jason Montleon <jmontleo@redhat.com> 0.0.4-1
- new package built with tito

* Wed Mar 19 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.4-1
- new package built with tito

* Wed Feb 19 2014 Martin Bacovsky <mbacovsk@redhat.com> 0.0.4-1
- new package built with tito
