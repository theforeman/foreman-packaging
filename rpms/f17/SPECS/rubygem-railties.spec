# Generated from railties-3.0.15.gem by gem2rpm -*- rpm-spec -*-
%global gem_name railties
%global rubyabi 1.9.1

Summary: Tools for creating, working with, and running Rails applications
Name: rubygem-%{gem_name}
Version: 3.0.15
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.rubyonrails.org
Source0: %{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby >= 1.8.7
Requires: rubygem(rake) >= 0.8.7
Requires: rubygem(thor) => 0.14.4
Requires: rubygem(thor) < 0.15
Requires: rubygem(rdoc) => 3.4
Requires: rubygem(rdoc) < 4
Requires: rubygem(activesupport) = 3.0.15
Requires: rubygem(actionpack) = 3.0.15
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby >= 1.8.7
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Rails internals: application bootup, plugins, generators, and rake tasks.


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
/usr/share/gems/gems/railties-3.0.15/
%files doc
%doc %{gem_docdir}

%changelog
* Thu Jun 14 2012 jason - 3.0.15-1
- Initial package
