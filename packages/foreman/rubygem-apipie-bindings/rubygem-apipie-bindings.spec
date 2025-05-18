# template: default
%global gem_name apipie-bindings

Name: rubygem-%{gem_name}
Version: 0.7.1
Release: 1%{?dist}
Summary: The Ruby bindings for Apipie documented APIs
License: MIT
URL: https://github.com/Apipie/apipie-bindings
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7.0
BuildRequires: ruby >= 2.7.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Bindings for API calls that are documented with Apipie. Bindings are generated
on the fly.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/doc
%{gem_instdir}/test

%changelog
* Sun May 18 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.7.1-1
- Update to 0.7.1

* Wed Jan 08 2025 Oleh Fedorenko <ofedoren@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Wed Feb 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.6.0-1
- Update to 0.6.0

* Wed May 11 2022 Evgeni Golov 0.5.0-1
- Update to 0.5.0

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
