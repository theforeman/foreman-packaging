%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from audited-activerecord-3.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name audited-activerecord

Summary: Log all changes to your ActiveRecord models
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.2.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/collectiveidea/audited
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(audited) = 4.2.0
Requires: %{?scl_prefix_ror}rubygem(activerecord) => 4.0
Requires: %{?scl_prefix_ror}rubygem(activerecord) < 5
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Log all changes to your ActiveRecord models


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
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 3.0.0-4
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 3.0.0-2
- new package built with tito

* Wed Nov 28 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.0-1
- Initial package
