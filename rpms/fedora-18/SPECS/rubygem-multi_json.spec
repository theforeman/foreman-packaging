# Generated from multi_json-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name multi_json
%global rubyabi 1.9.1

Summary: A gem to provide swappable JSON backends
Name: rubygem-%{gem_name}
Version: 1.2.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/intridea/multi_json
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
A gem to provide easy switching between different JSON backends, including Oj,
Yajl, the JSON gem (with C-extensions), the pure-Ruby JSON gem, and OkJson.


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
/usr/share/gems/gems/multi_json-1.2.0/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE.md
%doc %{gem_instdir}/README.md

%changelog
* Thu Jun 14 2012 jason - 1.2.0-1
- Initial package
