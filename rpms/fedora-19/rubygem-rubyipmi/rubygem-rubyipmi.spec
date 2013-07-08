%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rubyipmi

# we are using this gem also as non-SCL in RHEL6
%if !("%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16)
%define gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%define gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%define gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%endif

Summary: A ruby wrapper for ipmi command line tools
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.6.0
Release: 2%{?dist}
Group: Development/Languages
License: GPLv3+
URL: http://github.com/logicminds/rubyipmi
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi)
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: ipmitool
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi)
%endif
BuildRequires: %{?scl_prefix}ruby
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
BuildRequires: %{?scl_prefix}rubygems-devel
%else
BuildRequires: %{?scl_prefix}rubygems
%endif
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
%{gem_instdir}/%{gem_name}.gemspec

%exclude %{gem_instdir}/.document
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/Gemfile*

%changelog
* Mon Jul 08 2013 Dominic Cleal <dcleal@redhat.com> 0.6.0-2
- Add ipmitool dependency (dcleal@redhat.com)

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 0.6.0-1
- Rebase to rubyipmi 0.6.0 (dcleal@redhat.com)

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 0.5.1-1
- new package built with tito

