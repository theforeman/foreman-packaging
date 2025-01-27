# template: foreman_plugin
%global gem_name foreman_dhcp_browser
%global plugin_name dhcp_browser
%global foreman_min_version 3.13.0

Summary:    DHCP browser plugin for Foreman
Name:       rubygem-%{gem_name}
Version:    0.1.2
Release:    1%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_dhcp_browser
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies
Provides: foreman-plugin-dhcp-browser = %{version}

%description
Plugin for Foreman to browse and add/edit/delete DHCP leases independent of
Foreman's host creation.


%package doc
BuildArch:  noarch
Group:      Documentation
Requires:   %{name} = %{version}-%{release}
Summary:    Documentation for %{name}

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
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%posttrans
%{foreman_plugin_log}

%changelog
* Mon Jan 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.1.2-1
- Update to 0.1.2

* Fri Jan 24 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.1.1-1
- Update to 0.1.1

* Mon May 09 2022 Evgeni Golov - 0.0.8-6
- log plugin installation in posttrans

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.8-5
- Rebuild plugins for Ruby 2.7

* Fri Jan 17 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.0.8-4
- Drop posttrans macros

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.0.8-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Sun May 27 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.8-2
- Regenerate spec file based on the current template

* Mon Mar 12 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.8-1
- Update to v0.0.8 (Michael Moll <kvedulv@kvedulv.de>)

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.7-4
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Add foremandist to more plugins (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-1
- update foreman_dhcp_browser to 0.0.7 (kvedulv@kvedulv.de)

* Mon Oct 20 2014 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- update foreman_dhcp_browser to 0.0.6 (kvedulv@kvedulv.de)

* Mon Jul 21 2014 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Update to v0.0.5 (dcleal@redhat.com)

* Tue Feb 04 2014 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- Update to v0.0.4 (dcleal@redhat.com)

* Tue Dec 10 2013 Dominic Cleal <dcleal@redhat.com> 0.0.3-1
- new package built with tito
