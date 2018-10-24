%define debug_package %{nil}
%global enable_checks 0
%global gem_name foreman_scap_client
%global config_dir %{_sysconfdir}/%{gem_name}

%define rubyabi 1.8

Name: rubygem-%{gem_name}
Version: 0.4.0
Release: 2%{?dist}
Summary: Client script that runs OpenSCAP scan and uploads the result to foreman proxy
Group: Development/Languages
License: GPLv3
URL: https://github.com/openscap/foreman_scap_client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: foreman_scap_client.gemspec

Requires: bzip2
Requires: ruby(rubygems)
%if (0%{?rhel} >= 7) || (0%{?fedora} >= 27)
Requires: ruby(release)
%else
Requires: ruby(abi)
%endif
Requires: openscap-scanner
%if (0%{?rhel} >= 7) || (0%{?fedora} >= 27)
BuildRequires: ruby(release)
%else
BuildRequires: ruby(abi)
%endif
BuildRequires: ruby(rubygems)
%if (0%{?rhel} >= 6) || (0%{?fedora} >= 27)
BuildRequires: rubygems-devel
%endif
BuildRequires: ruby
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%if 0%{?rhel} == 5
# set up some macros for ancient rhel5
%global gem_dir /usr/share/gems
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_libdir %{gem_instdir}/lib
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%endif

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

%if 0%{?rhel} == 5
cp -p %{SOURCE1} %{gem_name}.gemspec
%else
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%endif

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%if 0%{?rhel} == 5
gem install --local --install-dir .%{gem_dir} --force %{gem_name}-%{version}.gem
%else
# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install
%endif

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if 0%{?rhel} == 5
rm -rf %{buildroot}%{gem_dir}/bin/
%endif

mkdir -p %{buildroot}%{_bindir}
%if 0%{?rhel} == 5
cp -a .%{gem_dir}/bin/* \
        %{buildroot}%{_bindir}/
%else
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
%endif

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# create config directory
mkdir -p %{buildroot}%{config_dir}

%files
%dir %{gem_instdir}
%{_bindir}/foreman_scap_client
%{config_dir}
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/config

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
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
