# Generated from rest-client-1.6.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rest-client
%global rubyabi 1.9.1

Summary: Simple HTTP and REST client for Ruby, inspired by microframework syntax for specifying actions
Name: rubygem-%{gem_name}
Version: 1.6.7
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/archiloque/rest-client
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby
Requires: rubygem(mime-types) >= 1.16
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A simple HTTP and REST client for Ruby, inspired by the Sinatra microframework
style of specifying actions: get, put, post, delete.


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
%dir %{gem_instdir}
%{_bindir}/restclient
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems/gems/rest-client-1.6.7/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/history.md

%changelog
* Thu Jun 14 2012 jason - 1.6.7-1
- Initial package
