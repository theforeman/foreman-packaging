%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name apipie-params

Summary: DSL for describing data structures
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.4
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: https://rubygems.org/gems/apipie-params
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby

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
Allows defining structure of data and perform validation against
it using json-schema

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
            --force %{SOURCE0} --no-ri --no-rdoc
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/test

%files doc
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/%{gem_name}.gemspec

%changelog
* Mon Aug 17 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- Release apipie-params 0.0.4 (stbenjam@redhat.com)

* Mon Jan 20 2014 Ivan Nečas <inecas@redhat.com> 0.0.3-1
- Bump version (inecas@redhat.com)

* Wed May 29 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.2-2
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Tue May 07 2013 Ivan Necas <inecas@redhat.com> 0.0.2-1
- new package built with tito

