# Generated from tzinfo-0.3.32.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tzinfo
%global rubyabi 1.9.1

Summary: Daylight-savings aware timezone library
Name: rubygem-%{gem_name}
Version: 0.3.32
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://tzinfo.rubyforge.org/
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
TZInfo is a Ruby library that uses the standard tz (Olson) database to provide
daylight savings aware transformations between times in different time zones.


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
/usr/share/gems/gems/tzinfo-0.3.32/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README
%doc %{gem_instdir}/CHANGES

%changelog
* Thu Jun 14 2012 jason - 0.3.32-1
- Initial package
