%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from webmock-1.6.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name webmock

%global rubyabi 1.9.1

Summary: Library for stubbing HTTP requests in Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.6.4
Release: 5%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/bblimke/webmock
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}ruby 
Requires: %{?scl_prefix}rubygem(addressable) => 2.2
Requires: %{?scl_prefix}rubygem(addressable) < 3
Requires: %{?scl_prefix}rubygem(addressable) > 2.2.5
Requires: %{?scl_prefix}rubygem(crack) >= 0.1.7
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}ruby(rubygems) 
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
WebMock allows stubbing HTTP requests and setting expectations on HTTP
requests.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/.yardoc
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/*.md
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/.gitignore
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/.rvmrc
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/Gemfile

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/Rakefile
%{gem_instdir}/lib
%{gem_instdir}/spec
%{gem_instdir}/test
%{gem_instdir}/webmock.gemspec
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Fri Mar 29 2013 Marek Hulan <ares@igloonet.cz> 1.6.4-5
- another SCL fix

* Fri Mar 29 2013 Marek Hulan <ares@igloonet.cz> 1.6.4-4
- fix for SCL

* Wed Mar 27 2013 Marek Hulan <ares@igloonet.cz> 1.6.4-3
- new package built with tito

* Fri Nov 02 2012 Miroslav Suchý <msuchy@redhat.com> 1.6.4-2
- add rubygem-webmock (msuchy@redhat.com)

* Tue Sep 13 2011 Steve Linabery - 1.6.4-1
- Initial package
