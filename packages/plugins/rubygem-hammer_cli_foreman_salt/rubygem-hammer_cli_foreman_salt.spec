# template: hammer_plugin
%global gem_name hammer_cli_foreman_salt
%global plugin_name foreman_salt

%global hammer_confdir %{_sysconfdir}/hammer

Name: rubygem-%{gem_name}
Version: 0.1.0
Release: 2%{?foremandist}%{?dist}
Summary: Foreman Salt-related commands for Hammer CLI
License: GPLv3
URL: https://github.com/theforeman/hammer_cli_foreman_salt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Foreman Salt-related commands for Hammer CLI.


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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%config(noreplace) %{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/config

%changelog
* Wed Oct 19 2022 Evgeni Golov 0.1.0-2
- Regenerate spec based on latest template

* Thu Dec 02 2021 Bernhard Suttner <suttner@atix.de> 0.1.0-1
- Update to 0.1.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.5-5
- Rebuild plugins for Ruby 2.7

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.0.5-4
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 0.0.5-3
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.0.5-2
- Use gem_install macro (dominic@cleal.org)

* Thu Feb 04 2016 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Release hammer_cli_foreman_salt 0.0.5 (stbenjam@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-4
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-3
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-2
- fixes #8979 - convert hammer packages to SCL (dcleal@redhat.com)

* Wed Mar 04 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- Update hammer_cli_foreman_salt to 0.0.4 (dcleal@redhat.com)

* Tue Mar 03 2015 Stephen Benjamin <stephen@redhat.com> 0.0.3-1
- Release 0.0.3

* Thu Jan 15 2015 Stephen Benjamin <stephen@redhat.com> 0.0.1-1
- Initial release
