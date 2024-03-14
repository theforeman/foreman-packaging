# template: hammer_plugin
%global gem_name hammer_cli_foreman_puppet
%global plugin_name foreman_puppet

%global hammer_confdir %{_sysconfdir}/hammer

Name: rubygem-%{gem_name}
Version: 0.0.7
Release: 2%{?foremandist}%{?dist}
Summary: Foreman Puppet plugin for Hammer CLI
License: GPLv3
URL: https://github.com/theforeman/hammer-cli-foreman-puppet
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
Foreman Puppet plugin for Hammer CLI.


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
* Thu Mar 14 2024 nofaralfasi <nalfassi@redhat.com> 0.0.7-2
- Regenerate spec file based on the latest template

* Mon Jan 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.0.7-1
- Update to 0.0.7

* Fri May 13 2022 Nadja Heitmann <nadjah@atix.de> 0.0.6-1
- Update to 0.0.6
- Remove deprecated options from host/hostgroup

* Wed Mar 16 2022 Oleh Fedorenko <ofedoren@redhat.com> 0.0.5-1
- Update to 0.0.5

* Tue Nov 09 2021 Amir Fefer <amirfefer@gmail.com> 0.0.4-1
- Update to 0.0.4

* Thu Aug 05 2021 Amir Fefer <amirfefer@gmail.com> 0.0.3-1
- Update to 0.0.3

* Tue Aug 03 2021 Amir Fefer <amirfefer@gmail.com> 0.0.2-1
- Add rubygem-hammer_cli_foreman_puppet generated by gem2rpm using the hammer_plugin template

