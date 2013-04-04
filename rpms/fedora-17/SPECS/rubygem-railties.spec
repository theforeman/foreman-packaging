%global gem_name railties
%global rubyabi 1.9.1

Summary: Tools for creating, working with, and running Rails applications
Name: rubygem-%{gem_name}
Version: 3.0.20
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby >= 1.8.7
Requires: rubygem(rake) >= 0.8.7
Requires: rubygem(thor) => 0.14.4
Requires: rubygem(thor) < 0.15
Requires: rubygem(rdoc) => 3.4
Requires: rubygem(rdoc) < 4

Requires: rubygem(activesupport) = %{version}
Requires: rubygem(actionpack) = %{version}

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
/usr/share/gems/gems/railties-%{version}/
%files doc
%doc %{gem_docdir}

%changelog
* Mon Feb 4 2013 shk@redhat.com 3.0.20-1
- Updated to 3.0.20
* Fri Jan 25 2013 shk@redhat.com 3.0.19-1
- Updated to 3.0.19
* Thu Jun 14 2012 jason - 3.0.17-1
- Initial package
