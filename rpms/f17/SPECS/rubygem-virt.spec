# Generated from virt-0.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name virt
%global rubyabi 1.9.1

Summary: Simple to use ruby interface to libvirt
Name: rubygem-%{gem_name}
Version: 0.2.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv3
URL: https://github.com/ohadlevy/virt
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(ruby-libvirt) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Simplied interface to use ruby the libvirt ruby library


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
/usr/share/gems/gems/virt-0.2.1/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.rdoc

%changelog
* Thu Jun 14 2012 jason - 0.2.1-1
- Initial package
