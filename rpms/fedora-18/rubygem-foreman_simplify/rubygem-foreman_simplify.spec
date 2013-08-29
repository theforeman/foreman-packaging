# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_simplify

%define rubyabi 1.9.1
%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d

Summary:    Plugin for Foreman that simplifies the UI
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.0.5
Release:    1%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_simplify
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.2.0
Requires:   %{?scl_prefix}rubygem(deface)

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
Requires: %{?scl_prefix}rubygems

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-simplify

%description
Plugin for Foreman that simplifies the UI.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

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
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/lib
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb

%exclude %{gem_instdir}/.git*
%exclude %{gem_instdir}/Gemfile*
%exclude %{gem_instdir}/install
%exclude %{gem_instdir}/*.gemspec
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Thu Aug 29 2013 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- New version
- Renamed from foreman_openstack_simplify to foreman_simplify
- Refresh spec to current plugin template, require Foreman 1.2+
- Depend on upstream foreman packages (pbrady@redhat.com)

* Thu May 24 2013 Jiri Stransky <jistr@redhat.com> 0.0.4-3
- Fix post and postun scripts to use SCL where necessary.
- Make the post and postun scripts agnostic to usage of
  Bundler vs. bundler_ext.

* Wed May 22 2013 Lon Hohberger <lhh@redhat.com> 0.0.4-2
- Fix install Requires: dependency for SCL

* Mon May 20 2013 Jiri Stransky <jistr@redhat.com> 0.0.4-1
- Moved foreman_openstack_simplify.rb (for Foreman's bundler.d) into
  the gem itself, instead having it as separate source.

* Wed May 15 2013 Jiri Stransky <jistr@redhat.com> 0.0.3-2
- SCL

* Tue May 7 2013 Jiri Stransky <jistr@redhat.com> 0.0.1-1
- Initial package
