# template: hammer_plugin
%global gem_name hammer_cli_foreman_virt_who_configure
%global plugin_name foreman_virt_who_configure

%global hammer_confdir %{_sysconfdir}/hammer

Name: rubygem-%{gem_name}
Version: 0.1.2
Release: 1%{?foremandist}%{?dist}
Summary: Plugin for configuring Virt Who
License: GPLv3+
URL: https://github.com/theforeman/hammer-cli-foreman-virt-who-configure
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: hammer-cli-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Plugin for configuring Virt Who.


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

mkdir -p %{buildroot}%{hammer_confdir}/cli.modules.d
install -m 0644 .%{gem_instdir}/config/%{plugin_name}.yml \
                %{buildroot}%{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%config(noreplace) %{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/config
%{gem_instdir}/test

%changelog
* Thu Feb 20 2025 Chris Roberts <chrobert@redhat.com> - 0.1.2-1
- Update to 0.1.2

* Fri Sep 20 2024 Chris Roberts <chrobert@redhat.com> - 0.1.1-1
- Update to 0.1.1

* Tue Jan 09 2024 Oleh Fedorenko <ofedoren@redhat.com> - 0.1.0-1
- Update to 0.1.0

* Wed Oct 19 2022 Evgeni Golov 0.0.9-2
- Regenerate spec based on latest template

* Wed Nov 10 2021 Jonathon Turel <jturel@gmail.com> 0.0.9-1
- Update to 0.0.9

* Mon Jul 12 2021 Odilon Sousa <osousa@redhat.com> - 0.0.8-1
- Release rubygem-hammer_cli_foreman_virt_who_configure 0.0.8

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.7-2
- Rebuild for Ruby 2.7

* Mon Dec 14 2020 Jonathon Turel <jturel@gmail.com> 0.0.7-1
- Update to 0.0.7

* Fri Mar 13 2020 Marek Hulan <mhulan@redhat.com> 0.0.6-1
- Update to 0.0.6

* Wed Nov 27 2019 Marek Hulan <mhulan@redhat.com> 0.0.5-1
- Update to 0.0.5

* Wed Sep 04 2019 Marek Hulan <mhulan@redhat.com> 0.0.4-1
- Update to 0.0.4

* Tue Sep 11 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.0.3-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Jan 10 2018 Eric D. Helms <ericdhelms@gmail.com> 0.0.3-2
- new package built with tito

* Mon Jun 26 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.3-1
- Update hammer_cli_foreman_virt_who_configure to 0.0.3 (tstrachota@redhat.com)

* Wed Jun 07 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.2-1
- new package built with tito

