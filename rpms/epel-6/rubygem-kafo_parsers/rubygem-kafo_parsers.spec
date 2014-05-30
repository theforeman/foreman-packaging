%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name kafo_parsers

Summary: Puppet module parsers
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.3
Release: 1%{?dist}
Group: Development/Libraries
License: GPLv3+
URL: https://github.com/theforeman/kafo_parsers
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && 0%{!?scl:1})
Requires: %{?scl_prefix}ruby(abi)
%else
Requires: %{?scl_prefix}ruby(release)
%endif
Requires: %{?scl_prefix}puppet
Requires: %{?scl_prefix}rubygem(rdoc)
Requires: %{?scl_prefix}rubygems

BuildRequires: %{?scl_prefix}rubygems-devel

%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && 0%{!?scl:1})
BuildRequires: %{?scl_prefix}ruby(abi)
%else
BuildRequires: %{?scl_prefix}ruby(release)
%endif
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This gem can parse values, validations, documentation, types, groups and conditions of parameters from your puppet modules

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
sed -i "/add_runtime_dependency.*puppet/d" ./%{gem_spec}
sed -i "/add_dependency.*puppet/d" ./%{gem_spec}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib

%doc %{gem_instdir}/LICENSE.txt

%exclude %{gem_instdir}/README.md
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
# add once tests are added (maybe spec dir instead)
#%exclude %{gem_instdir}/test
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md

%changelog
* Fri May 30 2014 Marek Hulan <mhulan@redhat.com> 0.0.3-1
- Modernise and update spec file for EL7 (dcleal@redhat.com)
- Fix annoying typo (dcleal@redhat.com)

* Mon Mar 31 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-1
- Fix validation parsing of classes without code (mhulan@redhat.com)
- Correct example in README (jcmcken@gmail.com)
- Update readme (mhulan@redhat.com)

