# Generated from terminal-table-1.4.5.gem by gem2rpm -*- rpm-spec -*-
%global gemname terminal-table

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Simple, feature rich ascii table generation library
Name: rubygem-%{gemname}
Version: 1.4.5
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/visionmedia/terminal-table
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Simple, feature rich ascii table generation library


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -pa .%{gemdir}/* \
        %{buildroot}%{gemdir}/


%files
%dir %{geminstdir}
%{geminstdir}/lib
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%{geminstdir}/tasks
%{geminstdir}/spec
%{geminstdir}/Rakefile
%{geminstdir}/Manifest
%exclude %{geminstdir}/%{gemname}.gemspec


%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/History.rdoc
%doc %{geminstdir}/Todo.rdoc
%doc %{geminstdir}/examples

%changelog
* Wed Jul 31 2013  <shk@linux.com> - 1.4.5-1
- Initial package
