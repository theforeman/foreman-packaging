# Generated from jquery-rails-1.0.19.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jquery-rails
%global rubyabi 1.9.1

Summary: Use jQuery with Rails 3
Name: rubygem-%{gem_name}
Version: 1.0.19
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubygems.org/gems/jquery-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) >= 1.3.6
Requires: ruby 
Requires: rubygem(railties) => 3.0
Requires: rubygem(railties) < 4
Requires: rubygem(thor) => 0.14
Requires: rubygem(thor) < 1
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This gem provides jQuery and the jQuery-ujs driver for your Rails 3
application.


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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems/gems/jquery-rails-1.0.19/
%files doc
%doc %{gem_docdir}

%changelog
* Thu Jun 14 2012 jason - 1.0.19-1
- Initial package
