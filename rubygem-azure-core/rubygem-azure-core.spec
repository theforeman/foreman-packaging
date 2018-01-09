%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from azure-core-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name azure-core

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.1
Release: 2%{?dist}
Summary: Core library to be consumed by Ruby SDK gems
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/Azure/azure-ruby-asm-core
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(faraday) >= 0.9
Requires: %{?scl_prefix}rubygem(faraday) < 1.0
Requires: %{?scl_prefix}rubygem(faraday_middleware) >= 0.10
Requires: %{?scl_prefix}rubygem(faraday_middleware) < 1.0
Requires: %{?scl_prefix_ror}rubygem(nokogiri) >= 1.6
Requires: %{?scl_prefix_ror}rubygem(nokogiri) < 2.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9.3
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Microsoft Azure Client Core Library for Ruby SDK.

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
%exclude %{gem_instdir}/.travis.yml
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/azure-core.gemspec
%{gem_instdir}/test

%changelog
* Fri Jun 10 2016 Daniel Lobato - 0.1.1-1
- Initial package
