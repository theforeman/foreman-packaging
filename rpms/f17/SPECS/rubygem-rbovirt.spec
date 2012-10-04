# Generated from rbovirt-0.0.11.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rbovirt
%global rubyabi 1.9.1

Summary: A Ruby client for oVirt REST API
Name: rubygem-%{gem_name}
Version: 0.0.12
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/abenari/rbovirt
Source0: %{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(nokogiri) 
Requires: rubygem(rest-client) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A Ruby client for oVirt REST API


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
/usr/share/gems/gems/rbovirt-0.0.12/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.rdoc

%changelog
* Thu Jun 14 2012 jason - 0.0.11-1
- Initial package
