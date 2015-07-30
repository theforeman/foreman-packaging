# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_hooks

%define rubyabi 1.9.1
%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d

Summary:    Run custom hook scripts on Foreman events
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.3.8
Release:    1%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_hooks
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.2.0

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
Provides: foreman-plugin-hooks

%description
Plugin engine for Foreman that enables running custom hook scripts on Foreman
events.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Requires:   %{?scl_prefix}rubygem(jgrep)
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

mkdir -p %{buildroot}%{foreman_dir}/config/hooks
ln -s %{gem_instdir} %{buildroot}%{foreman_dir}/%{gem_name}

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%{foreman_dir}/config/hooks
%{foreman_dir}/%{gem_name}

%exclude %{gem_instdir}/test
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/TODO
%{gem_instdir}/Rakefile

%changelog
* Wed Jan 07 2015 Dominic Cleal <dcleal@redhat.com> 0.3.7-3
- Add jgrep dependency to -doc for example helper (dcleal@redhat.com)

* Wed Apr 02 2014 Dominic Cleal <dcleal@redhat.com> 0.3.7-2
- Add /usr/share/foreman/foreman_hooks symlink to gem dir (dcleal@redhat.com)

* Wed Feb 26 2014 Dominic Cleal <dcleal@redhat.com> 0.3.7-1
- Update to foreman_hooks 0.3.7 (dcleal@redhat.com)

* Fri Feb 14 2014 Dominic Cleal <dcleal@redhat.com> 0.3.6-1
- Update to foreman_hooks 0.3.6 (dcleal@redhat.com)

* Mon Jan 27 2014 Dominic Cleal <dcleal@redhat.com> 0.3.5-1
- Update to foreman_hooks 0.3.5 (dcleal@redhat.com)

* Wed Jan 22 2014 Dominic Cleal <dcleal@redhat.com> 0.3.4-1
- Update to foreman_hooks 0.3.4 (dcleal@redhat.com)

* Thu Aug 29 2013 Dominic Cleal <dcleal@redhat.com> 0.3.3-1
- new package built with tito

