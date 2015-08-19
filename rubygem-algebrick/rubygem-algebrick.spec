%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name algebrick

Summary: Algebraic types and pattern matching
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.7.3
Release: 2%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/pitr-ch/algebrick
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(activesupport)

%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
Requires: %{?scl_prefix}ruby(abi)
BuildRequires: %{?scl_prefix}ruby(abi)
%else
Requires: %{?scl_prefix}ruby(release)
BuildRequires: %{?scl_prefix}ruby(release)
%endif

BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
It's a gem providing algebraic types and pattern matching seamlessly
integrates with standard features Ruby.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-ri --no-rdoc
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.txt
%{gem_instdir}/VERSION
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/README_FULL.md
%doc %{gem_instdir}/doc

%changelog
* Tue Jul 07 2015 Dominic Cleal <dcleal@redhat.com> 0.7.3-1
- Update algebrick to 0.7.3 (dcleal@redhat.com)

* Thu Jul 02 2015 Dominic Cleal <dcleal@redhat.com> 0.7.0-1
- Update algebrick to 0.7.0 (inecas@redhat.com)
- Add full rubygems.org source URL (dcleal@redhat.com)

* Mon Jan 20 2014 Ivan Nečas <inecas@redhat.com> 0.4.0-2
- Fix scl build (inecas@redhat.com)

* Mon Jan 20 2014 Ivan Nečas <inecas@redhat.com> 0.4.0-1
- new package built with tito

