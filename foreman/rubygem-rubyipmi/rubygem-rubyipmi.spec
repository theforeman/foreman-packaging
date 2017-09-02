%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rubyipmi

Summary: A ruby wrapper for ipmi command line tools
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.10.0
Release: 2%{?dist}
Group: Development/Languages
License: LGPLv2.1
URL: http://github.com/logicminds/rubyipmi
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18 || 0%{?rhel} >= 7
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi)
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: ipmitool
%if 0%{?fedora} > 18 || 0%{?rhel} >= 7
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This gem is a ruby wrapper for the freeipmi and ipmitool command line tools. It
provides a ruby implementation of ipmi commands that will make it simple to
connect to BMC devices from ruby.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}
%{gem_instdir}/LICENSE.txt
%{gem_instdir}/README.md
%{gem_instdir}/RELEASE_NOTES.md
%{gem_instdir}/Rakefile
%{gem_instdir}/VERSION

%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile*

%changelog
* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.10.0-2
- Use gem_install macro (dominic@cleal.org)
- Converted spec files (dcleal@redhat.com)

* Mon Apr 13 2015 Dominic Cleal <dcleal@redhat.com> 0.10.0-1
- Update rubyipmi to 0.10.0 (dcleal@redhat.com)

* Fri Mar 20 2015 Dominic Cleal <dcleal@redhat.com> 0.9.2-1
- Update rubyipmi to 0.9.2 (dcleal@redhat.com)

* Wed Mar 11 2015 Dominic Cleal <dcleal@redhat.com> 0.9.1-1
- Update rubyipmi to 0.9.1 (dcleal@redhat.com)

* Tue Mar 10 2015 Dominic Cleal <dcleal@redhat.com> 0.9.0-1
- Update rubyipmi to 0.9.0 (dcleal@redhat.com)

* Tue Oct 28 2014 Michael Moll <mmoll@mmoll.at> 0.8.1-1
- Update to rubyipmi 0.8.1
- Reflect license change

* Mon May 19 2014 Dominic Cleal <dcleal@redhat.com> 0.7.0-2
- Modernise and update for EL7

* Thu Oct 17 2013 Dominic Cleal <dcleal@redhat.com> 0.7.0-1
- Rebase to rubyipmi 0.7.0 (dcleal@redhat.com)

* Mon Jul 08 2013 Dominic Cleal <dcleal@redhat.com> 0.6.0-2
- Add ipmitool dependency (dcleal@redhat.com)

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 0.6.0-1
- Rebase to rubyipmi 0.6.0 (dcleal@redhat.com)

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 0.5.1-1
- new package built with tito
