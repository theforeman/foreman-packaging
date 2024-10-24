%global gem_name foreman_scap_client
%global config_dir %{_sysconfdir}/%{gem_name}

%define rubyabi 1.8

%if 0%{?suse_version}
%define mod_name %{gem_name}
%define gem_instdir %{gem_base}/gems/%{gem_name}-%{version}
%define gem_libdir %{gem_instdir}/lib
%define gem_docdir %{gem_base}/doc/%{gem_name}-%{version}
%define gem_cache %{gem_base}/cache/%{gem_name}-%{version}.gem
%define gem_spec %{gem_base}/specifications/%{gem_name}-%{version}.gemspec
%endif

Name: rubygem-%{gem_name}
Version: 0.6.2
Release: 2%{?dist}
Summary: Client script that runs OpenSCAP scan and uploads the result to foreman proxy
Group: Development/Languages
License: GPLv3
URL: https://github.com/theforeman/foreman_scap_client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: bzip2
Requires: rubygem(json)
%if 0%{?suse_version} == 0
Requires: ruby(rubygems)
%endif
%if 0%{?el6}
Requires: ruby(abi)
Requires: rubygem(json) >= 1.4
Requires: rubygem(json) < 2.0
%else
%if 0%{?suse_version} == 0
Requires: ruby(release)
%endif
%endif
%if 0%{?suse_version}
Requires: openscap-utils
%else
Requires: openscap-scanner
%endif
%if 0%{?el6}
BuildRequires: ruby(abi)
%else
%if 0%{?suse_version} == 0
BuildRequires: ruby(release)
%endif
%endif
%if 0%{?suse_version} == 0
BuildRequires: ruby(rubygems)
BuildRequires: rubygems-devel
%endif
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: deprecated()


%description
Client script that runs OpenSCAP scan and uploads the result to foreman proxy.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
# %%gem_install on SUSE takes care of all that, so we don't have to
%if 0%{?suse_version} == 0
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%endif

# create config directory
mkdir -p %{buildroot}%{config_dir}

%files
%dir %{gem_instdir}
%{_bindir}/foreman_scap_client*
%{config_dir}
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%if (0%{?rhel} >= 7) || (0%{?fedora} >= 27)
%license %{gem_instdir}/LICENSE
%else
%doc %{gem_instdir}/LICENSE
%endif
%doc %{gem_instdir}/config

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Jul 25 2024 Oleh Fedorenko <ofedoren@redhat.com> - 0.6.2-2
- Mark rubygem-foreman_scap_client as deprecated

* Wed Jul 24 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.6.2-1
- Release rubygem-foreman_scap_client 0.6.2

* Tue Jun 18 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.6.0-1
- Release rubygem-foreman_scap_client 0.6.0

* Mon Jun 17 2024 Evgeni Golov - 0.5.3-2
- Make it build on SUSE too

* Wed May 15 2024 Oleh Fedorenko <ofedoren@redhat.com> - 0.5.3-1
- Release rubygem-foreman_scap_client 0.5.3

* Fri Dec 15 2023 Oleh Fedorenko <ofedoren@redhat.com> - 0.5.2-1
- Release rubygem-foreman_scap_client 0.5.2

* Wed May 10 2023 Evgeni Golov - 0.5.1-1
- Release rubygem-foreman_scap_client 0.5.1

* Tue May 18 2021 Ondrej Prazak <oprazak@redhat.com> 0.5.0-1
- Update to 0.5.0

* Fri Jul 17 2020 Ondrej Prazak <oprazak@redhat.com> 0.4.7-1
- Update to 0.4.7

* Wed Jan 08 2020 Evgeni Golov - 0.4.6-2
- Rebuild for EL8 client repository

* Thu May 09 2019 Marek Hulan <mhulan@redhat.com> 0.4.6-1
- Update to 0.4.6

* Tue Apr 09 2019 Marek Hulan <mhulan@redhat.com> 0.4.5-1
- Update to 0.4.5

* Thu Mar 07 2019 Marek Hulan <mhulan@redhat.com> 0.4.3-1
- Update to 0.4.3

* Tue Feb 12 2019 Marek Hulan <mhulan@redhat.com> 0.4.2-1
- Update to 0.4.2

* Tue Jan 29 2019 Marek Hulan <mhulan@redhat.com> 0.4.1-1
- Update to 0.4.1

* Mon Oct 29 2018 Evgeni Golov - 0.4.0-3
- build on EL6+ and Fedora only

* Wed Oct 24 2018 Evgeni Golov - 0.4.0-2
- make rubygem-foreman_scap_client build on EL5 and EL6

* Fri Oct 12 2018 Marek Hulan <mhulan@redhat.com> 0.4.0-1
- Update to 0.4.0

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.3.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.3.0-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Feb 20 2017 Dominic Cleal <dominic@cleal.org> 0.3.0-1
- Update foreman_scap_client to 0.3.0 (mhulan@redhat.com)
- Modernise spec file (dominic@cleal.org)

* Fri Sep 02 2016 Dominic Cleal <dominic@cleal.org> 0.2.0-1
- Update foreman_scap_client to 0.2.0 (oprazak@redhat.com)

* Mon Nov 02 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- foreman_scap_client 0.1.2 (shlomi@ben-hanna.com)

* Fri May 15 2015 Šimon Lukašík <slukasik@redhat.com> - 0.1.1-1
- new upstream release

* Fri Jan 30 2015 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-1
- new upstream release

* Fri Jan 23 2015 Marek Hulan <mhulan@redhat.com> 0.0.1-3
- new package built with tito

* Tue Jan 13 2015 Šimon Lukašík <slukasik@redhat.com> - 0.0.1-2
- allow build for rhel6

* Tue Jan 13 2015 Šimon Lukašík <slukasik@redhat.com> - 0.0.1-1
- Initial package
