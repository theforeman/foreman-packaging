# template: smart_proxy_plugin
%global gem_name smart_proxy_shellhooks
%global plugin_name shellhooks

%global foreman_proxy_min_version 2.3
%global foreman_proxy_dir %{_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_sharedstatedir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: rubygem-%{gem_name}
Version: 0.9.4
Release: 1%{?foremandist}%{?dist}
Summary: Run shell scripts via Foreman webhooks
License: GPLv3+
URL: https://github.com/theforeman/smart_proxy_shellhooks
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Provides easy integration with 3rd parties for Foreman.


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

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/%{plugin_name}.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/shellhooks.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/shellhooks.yml

# example scripts
install -d -m755 %{buildroot}%{foreman_proxy_statedir}/%{plugin_name}
mv %{buildroot}%{gem_instdir}/examples/* %{buildroot}%{foreman_proxy_statedir}/%{plugin_name}

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/shellhooks.yml
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/bundler.d
%{gem_libdir}
%exclude %{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}
%{foreman_proxy_statedir}/%{plugin_name}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Aug 05 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.9.4-1
- Update to 0.9.4

* Wed Jul 29 2026 Zach Huntington-Meath <zhunting@redhat.com> - 0.9.3-2
- Rebuild for EL10

* Wed May 15 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.9.3-1
- Release rubygem-smart_proxy_shellhooks 0.9.3

* Mon May 09 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.9.2-3
- Drop unused smart_proxy_dynflow_core_bundlerd_dir macro

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.9.2-2
- Rebuild for Ruby 2.7

* Tue Mar 16 2021 Lukas Zapletal <lzap+rpm@redhat.com> 0.9.2-1
- Update to 0.9.2

* Thu Dec 17 2020 Lukas Zapletal <lzap+rpm@redhat.com> 0.9.1-1
- Initial version
