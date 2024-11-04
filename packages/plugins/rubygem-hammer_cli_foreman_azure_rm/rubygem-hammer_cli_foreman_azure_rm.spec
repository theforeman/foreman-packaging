# template: hammer_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hammer_cli_foreman_azure_rm
%global plugin_name foreman_azure_rm

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}
%global hammer_confdir %{_root_sysconfdir}/hammer

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.2
Release: 1%{?foremandist}%{?dist}
Summary: Foreman AzureRM commands for Hammer CLI
Group: Development/Languages
License: GPLv3
URL: https://github.com/theforeman/hammer_cli_foreman_azure_rm
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Foreman AzureRM commands for Hammer CLI.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

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
%exclude %{gem_cache}
%{gem_spec}
%config %{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/config

%changelog
* Mon Nov 04 2024 Chris Roberts <chrobert@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Tue Jun 13 2023 Chris Roberts <chrobert@redhat.com> 0.2.4-1
- Update to 0.2.4

* Wed Nov 30 2022 Chris Roberts <chrobert@redhat.com> 0.2.3-1
- Update to 0.2.3

* Thu Oct 28 2021 Chris Roberts <chrobert@redhat.com> 0.2.2-1
- Update to 0.2.2

* Wed May 26 2021 Odilon Sousa <osousa@redhat.com> - 0.2.1-1
- Release rubygem-hammer_cli_foreman_azure_rm 0.2.1

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.2.0-2
- Rebuild plugins for Ruby 2.7

* Mon May 18 2020 Aditi Puntambekar <apuntamb@redhat.com> 0.2.0-1
- Update to 0.2.0

* Thu Jan 09 2020 Aditi Puntambekar <apuntamb@redhat.com> 0.1.2-1
- Update to 0.1.2

* Wed Dec 18 2019 Aditi Puntambekar <apuntamb@redhat.com> 0.1.1-1
- Update to 0.1.1

* Fri Nov 01 2019 Aditi Puntambekar <apuntamb@redhat.com> 0.1.0-1
- Add rubygem-hammer_cli_foreman_azure_rm generated by gem2rpm using the hammer_plugin template

