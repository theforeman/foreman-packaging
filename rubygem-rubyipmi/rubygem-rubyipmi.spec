%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rubyipmi

Summary: A ruby wrapper for ipmi command line tools
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.7.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv3+
URL: http://github.com/logicminds/rubyipmi
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18 || 0%{?rhel} >= 7
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi)
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: ipmitool
%if 0%{?fedora} > 18 || 0%{?rhel} >= 7
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi)
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This gem is a ruby wrapper for the freeipmi and ipmitool command line tools. It
provides a ruby implementation of ipmi commands that will make it simple to
connect to BMC devices from ruby.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}
%{gem_instdir}/LICENSE.txt
%{gem_instdir}/README.md
%{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/VERSION

%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile*

%changelog
* Thu Oct 17 2013 Dominic Cleal <dcleal@redhat.com> 0.7.0-1
- Rebase to rubyipmi 0.7.0 (dcleal@redhat.com)

* Mon Jul 08 2013 Dominic Cleal <dcleal@redhat.com> 0.6.0-2
- Add ipmitool dependency (dcleal@redhat.com)

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 0.6.0-1
- Rebase to rubyipmi 0.6.0 (dcleal@redhat.com)

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 0.5.1-1
- new package built with tito

