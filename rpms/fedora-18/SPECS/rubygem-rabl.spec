# Generated from rabl-0.7.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rabl
%global rubyabi 1.9.1

Summary: General ruby templating with json, bson, xml and msgpack support
Name: rubygem-%{gem_name}
Version: 0.7.5
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/nesquena/rabl
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby
Requires: rubygem(activesupport) >= 2.3.14
Requires: rubygem(multi_json) => 1.0
Requires: rubygem(multi_json) < 2
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
General ruby templating with json, bson, xml and msgpack support


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
#%dir %{gem_instdir}
#%{gem_libdir}
/usr/share/gems/gems/rabl-0.7.5/
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Sun Aug 05 2012 jason - 0.7.5-1
- Initial package
