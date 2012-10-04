# Generated from oauth-0.4.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name oauth
%global rubyabi 1.9.1

Summary: OAuth Core Ruby implementation
Name: rubygem-%{gem_name}
Version: 0.4.6
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
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
OAuth Core Ruby implementation


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
            --bindir .%{_bindir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x


%files
#%dir %{gem_instdir}
%{_bindir}/oauth
#%{gem_instdir}/bin
#%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems/gems/oauth-0.4.6/

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/TODO

%changelog
* Sun Aug 05 2012 jason - 0.4.6-1
- Initial package
