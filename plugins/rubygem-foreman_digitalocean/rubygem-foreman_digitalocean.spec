# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_digitalocean

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir %{foreman_dir}/config/settings.plugins.d

Summary:    Provision and manage DigitalOcean from Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    1.2.0
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman-digitalocean
Source0:    http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman-compute >= 1.13.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-digitalocean
Provides: foreman-digitalocean
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This plugin enables provisioning and managing DigitalOcean in Foreman.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/%{gem_name}.rb
gem '%{gem_name}'
GEMFILE

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/locale
%exclude %{gem_cache}
%exclude %{gem_instdir}/test
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Tue Jan 03 2017 Dominic Cleal <dominic@cleal.org> 1.2.0-1
- Update foreman_digitalocean to 1.2.0 (mail@timogoebel.name)

* Mon Oct 03 2016 Dominic Cleal <dominic@cleal.org> 1.1.0-1
- Update foreman-digitalocean to 1.1 (me@daniellobato.me)
- Use gem_install macro (dominic@cleal.org)

* Mon Apr 18 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- plugins:foreman_digitalocean - 1.0.0 (elobatocs@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.2.1-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Oct 28 2015 Dominic Cleal <dcleal@redhat.com> 0.2.1-1
- plugins:foreman_digitalocean - Release 0.2.1 (elobatocs@gmail.com)
- Add foremandist (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Apr 28 2015 Tommy McNeely <tommy@lark-it.com> 0.2.0-1
- Version 0.2.0 (tommy@lark-it.com)
- #10242 - Changed template name to _base for Foreman 1.8

* Fri Feb 13 2015 Tommy McNeely <tommy@lark-it.com> 0.1.0-1
- Version 0.1.0 (tommy@lark-it.com)
- #8617 - add SSH key pair integration
- #8650 - show region name in VM details

* Wed Dec 10 2014 Daniel Lobato <dlobatog@redhat.com> 0.0.3-1
- Version 0.0.3 (dlobatog@redhat.com)

* Tue Dec 02 2014 Daniel Lobato <dlobatog@redhat.com> 0.0.2-1
- Initial version 0.0.2-1 (dlobatog@redhat.com)
