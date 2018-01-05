%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from fog-azure-0.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog-azure

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.2
Release: 2%{?dist}
Summary: Module for the 'fog' gem to support Azure cloud services
Group: Development/Languages
License: MIT
URL: https://github.com/fog/fog-azure
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(azure) >= 0.6
Requires: %{?scl_prefix}rubygem(azure) < 1
Requires: %{?scl_prefix}rubygem(fog-core) >= 1.27
Requires: %{?scl_prefix}rubygem(fog-core) < 2
Requires: %{?scl_prefix}rubygem(fog-json) >= 1.0
Requires: %{?scl_prefix}rubygem(fog-json) < 2
Requires: %{?scl_prefix}rubygem(fog-xml) >= 0.1
Requires: %{?scl_prefix}rubygem(fog-xml) < 1
BuildArch: noarch
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This library can be used as a module for `fog` or as standalone provider
to use the Azure cloud services in applications.

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
%{?scl:EOF}
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%doc %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fog-azure.gemspec
%{gem_instdir}/tests

%changelog
* Thu May 12 2016 Daniel Lobato - 0.0.2-1
- Initial package
