# Generated from unicode-display_width-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name unicode-display_width
%global rubyabi 1.9.1

Summary: Support for east_asian_width string widths
Name: rubygem-%{gem_name}
Version: 0.1.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/janlelis/unicode-display_width
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) >= 1.3.6
Requires: ruby
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This gem adds String#display_size to get the display size of a string using
EastAsianWidth.txt.


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
/usr/share/gems/gems/unicode-display_width-0.1.1/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/LICENSE.txt

%changelog
* Thu Jun 14 2012 jason - 0.1.1-1
- Initial package
