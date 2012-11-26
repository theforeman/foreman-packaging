# Generated from hirb-unicode-0.0.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hirb-unicode
%global rubyabi 1.9.1

Summary: Unicode support for hirb
Name: rubygem-%{gem_name}
Version: 0.0.5
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(hirb) => 0.5
Requires: rubygem(hirb) < 1
Requires: rubygem(unicode-display_width) => 0.1.1
Requires: rubygem(unicode-display_width) < 0.2
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Unicode support for hirb


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
/usr/share/gems/gems/hirb-unicode-0.0.5/
%files doc
%doc %{gem_docdir}

%changelog
* Thu Jun 14 2012 jason - 0.0.5-1
- Initial package
