# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_dhcp_browser
%global plugin_name dhcp_browser
%global foreman_min_version 1.12.0

Summary:    DHCP browser plugin for Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.0.8
Release:    3%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_dhcp_browser
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface)
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end generated dependencies
Provides: foreman-plugin-dhcp-browser
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Plugin for Foreman to browse and add/edit/delete DHCP leases independent of
Foreman's host creation.


%package doc
BuildArch:  noarch
Group:      Documentation
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for %{pkg_name}

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
%{foreman_restart}
exit 0

%changelog
* Sat Sep 08 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.0.8-3
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
