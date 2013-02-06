# Generated from apipie-rails-%{version}.gem by gem2rpm -*- rpm-spec -*-
%global gem_name apipie-rails
%global rubyabi 1.9.1

Summary: Rails REST API documentation tool
Name: rubygem-%{gem_name}
Version: 0.0.13
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/Pajk/apipie-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Maintain your API documentation up to date!


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
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/





%files
%dir %{gem_instdir}
#%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems/gems/apipie-rails-%{version}/

%files doc
%doc %{gem_docdir}

%changelog
* Sun Aug 05 2012 jason - 0.0.12-1
- Initial package
