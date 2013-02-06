%global gem_name actionpack
%global rubyabi 1.9.1

Summary: Web-flow and rendering framework putting the VC in MVC (part of Rails)
Name: rubygem-%{gem_name}
Epoch: 1
Version: 3.0.20
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.rubyonrails.org
Source0: %{gem_name}-%{version}.gem
Patch0: 0001-fix-actionpack-dependencies.patch
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby >= 1.8.7
Requires: rubygem(activesupport) = %{version}
Requires: rubygem(activemodel) = %{version}
Requires: rubygem(builder) => 2.1.2
Requires: rubygem(builder) < 2.2
Requires: rubygem(i18n) => 0.5.0
Requires: rubygem(i18n) < 0.6
Requires: rubygem(rack) => 1.2.5
Requires: rubygem(rack-test) => 0.5.7
Requires: rubygem(rack-mount) => 0.6.14
Requires: rubygem(tzinfo) => 0.3.23
Requires: rubygem(tzinfo) < 0.4
Requires: rubygem(erubis) => 2.6.6
Requires: rubygem(erubis) < 2.7
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby >= 1.8.7
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: %{name} = %{version}
%description
Web apps on Rails. Simple, battle-tested conventions for building and testing
MVC web applications. Works with any Rack-compatible server.


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
cd %{buildroot}%{gem_dir}
cp %{PATCH0} ./
patch -p0 < ./0001-fix-actionpack-dependencies.patch
rm ./0001-fix-actionpack-dependencies.patch




%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc /usr/share/gems/gems/actionpack-%{version}/CHANGELOG
%doc /usr/share/gems/gems/actionpack-%{version}/MIT-LICENSE
%doc /usr/share/gems/gems/actionpack-%{version}/README.rdoc

%changelog
* Mon Feb 4 2013 shk@redhat.com - 3.0.20-1
- Updated to 3.0.20
* Fri Jan 25 2013 shk@redhat.com - 3.0.19-1
- Updated to 3.0.19
* Thu Jun 14 2012 jason - 3.0.17-1
- Initial package
