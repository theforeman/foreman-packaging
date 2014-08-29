%global gem_name rb-readline

Summary: Pure-Ruby Readline Implementation
Name: rubygem-%{gem_name}
Version: 0.5.1
Release: 1%{?dist}
Group: Development/Languages
License: BSD
URL: https://github.com/luislavena/rb-readline
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

%if 0%{?rhel} == 6
Requires: ruby(abi)
%else
Requires: ruby(release)
%endif
BuildRequires: rubygems-devel
%if 0%{?rhel} == 6
BuildRequires: ruby(abi)
%else
BuildRequires: ruby(release)
%endif
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
The readline library provides a pure Ruby implementation of the GNU readline C library,
as well as the Readline extension that ships as part of the standard library.


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
%gem_install -n %{SOURCE0}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/bench/_rl_adjust_point.rb
%exclude %{gem_instdir}/setup.rb
%exclude %{gem_instdir}/rb-readline.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/test
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGES


%changelog
* Fri Aug 29 2014 Tomáš Strachota <tstrachota@redhat.com> 0.5.1-1
- Added rb-readline 0.5.1 (tstrachota@redhat.com)

