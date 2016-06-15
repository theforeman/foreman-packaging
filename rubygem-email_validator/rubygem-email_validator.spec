%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name email_validator

Summary: An email validator for Rails 3 and 4
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.6.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/balexand/email_validator
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Provides an email validations for Rails applications

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}

%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0} --no-ri --no-rdoc
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/spec
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Changes.md

%changelog
