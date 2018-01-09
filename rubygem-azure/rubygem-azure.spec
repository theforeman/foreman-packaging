%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from azure-0.7.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name azure

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.7.7
Release: 2%{?dist}
Summary: Official ruby client library to consume Microsoft Azure services
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/azure/azure-sdk-for-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(addressable) >= 2.3
Requires: %{?scl_prefix}rubygem(addressable) < 3.0
Requires: %{?scl_prefix}rubygem(azure-core) >= 0.1
Requires: %{?scl_prefix}rubygem(azure-core) < 1.0
Requires: %{?scl_prefix}rubygem(faraday) >= 0.9
Requires: %{?scl_prefix}rubygem(faraday) < 1.0
Requires: %{?scl_prefix}rubygem(faraday_middleware) >= 0.10
Requires: %{?scl_prefix}rubygem(faraday_middleware) < 1.0
Requires: %{?scl_prefix_ruby}rubygem(json) >= 1.8
Requires: %{?scl_prefix_ruby}rubygem(json) < 2.0
Requires: %{?scl_prefix_ror}rubygem(mime-types) >= 1.0
Requires: %{?scl_prefix_ror}rubygem(mime-types) < 4.0
Requires: %{?scl_prefix_ror}rubygem(nokogiri) >= 1.6
Requires: %{?scl_prefix_ror}rubygem(nokogiri) < 2.0
Requires: %{?scl_prefix}rubygem(systemu) >= 2.6
Requires: %{?scl_prefix}rubygem(systemu) < 3.0
Requires: %{?scl_prefix_ruby}rubygem(thor) >= 0.19
Requires: %{?scl_prefix_ruby}rubygem(thor) < 1.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
buildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Microsoft Azure Client Library for Ruby.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/pfxer
%doc %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/azure.gemspec

%changelog
* Tue Nov 15 2016 Dominic Cleal <dominic@cleal.org> 0.7.7-1
- Update azure to 0.7.7 (dominic@cleal.org)

* Fri May 13 2016 Daniel Lobato - 0.7.5-1
- Initial package
