%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from audited-3.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name audited
%global rubyabi 1.9.1

Summary: Log all changes to your models
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.0.0
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/collectiveidea/audited
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Log all changes to your models


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

# Remove shebang from Rakefile that do not have executable permission.
sed -i '/^#!\//d' %{buildroot}%{gem_instdir}/Rakefile


%check
# Unfortunatelly, there doesn't seems to be any test coverage of auditable gem.
# However, there are available test suites for audited's ORM adapters.


%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/.*
# audited-*.gemspec seems to be included by mistake.
# https://github.com/collectiveidea/audited/pull/124
%exclude %{gem_instdir}/audited-*.gemspec
# Seems that spec and test folders are included just by mistake.
# https://github.com/collectiveidea/audited/pull/125
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/test
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Appraisals
%doc %{gem_instdir}/CHANGELOG
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/audited.gemspec
%{gem_instdir}/gemfiles

%changelog
* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 3.0.0-4
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 3.0.0-2
- new package built with tito

* Tue Nov 27 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.0-1
- Initial package
