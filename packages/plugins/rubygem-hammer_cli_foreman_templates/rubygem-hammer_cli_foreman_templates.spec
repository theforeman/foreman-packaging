# template: hammer_plugin
%global gem_name hammer_cli_foreman_templates
%global plugin_name foreman_templates

%global hammer_confdir %{_sysconfdir}/hammer

Name: rubygem-%{gem_name}
Version: 0.3.0
Release: 1%{?foremandist}%{?dist}
Summary: Foreman Hammer commands for exporting and importing templates
License: GPLv3
URL: https://github.com/theforeman/hammer-cli-foreman-templates
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
CLI plugin with import and export commands for Hammer_CLI_Foreman.


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
* Mon Jan 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.0-1
- Update to 0.3.0

* Wed Oct 19 2022 Evgeni Golov 0.2.0-3
- Regenerate spec based on latest template

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.2.0-2
- Rebuild plugins for Ruby 2.7

* Mon Mar 02 2020 Oleh Fedorenko <ofedoren@redhat.com> 0.2.0-1
- Update to 0.2.0

* Wed Sep 26 2018 Oleh Fedorenko <ofedoren@redhat.com> 0.1.2-1
- Update to 0.1.2

* Wed Sep 12 2018 Bryan Kearney <bryan.kearney@gmail.com> - 0.1.0-3
- Move licenes which are GPL-* to GPLv3

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Apr 03 2018 Marek Hulan <mhulan@redhat.com> 0.1.0-1
- Add rubygem-hammer_cli_foreman_templates generated by gem2rpm using the hammer_plugin template
