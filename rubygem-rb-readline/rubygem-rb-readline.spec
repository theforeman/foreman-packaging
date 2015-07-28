%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rb-readline

Summary: Pure-Ruby Readline Implementation
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.5.1
Release: 2%{?dist}
Group: Development/Languages
License: BSD
URL: https://github.com/luislavena/rb-readline
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

%if 0%{?scl:1} || (0%{?el6} && 0%{!?scl:1})
Requires: %{?scl_prefix}ruby(abi)
%else
Requires: %{?scl_prefix}ruby(release)
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
%if 0%{?scl:1} || (0%{?el6} && 0%{!?scl:1})
BuildRequires: %{?scl_prefix}ruby(abi)
%else
BuildRequires: %{?scl_prefix}ruby(release)
%endif
BuildRequires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
The readline library provides a pure Ruby implementation of the GNU readline C library,
as well as the Readline extension that ships as part of the standard library.

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
%{?scl:scl enable %{scl} - << \EOF}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:EOF}

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
%doc %{gem_docdir}
%doc %{gem_instdir}/test
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGES

%changelog
* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 0.5.1-2
- Convert rb-readline to SCL (dcleal@redhat.com)

* Fri Aug 29 2014 Tomáš Strachota <tstrachota@redhat.com> 0.5.1-1
- Added rb-readline 0.5.1 (tstrachota@redhat.com)
