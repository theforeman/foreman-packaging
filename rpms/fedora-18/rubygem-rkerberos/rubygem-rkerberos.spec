%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name rkerberos

%if !("%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16)
%define gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%define gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%define gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%endif

%define version 0.1.1
%define release 4

Summary: A Ruby interface for the the Kerberos library
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Artistic 2.0
URL: http://github.com/domcleal/rkerberos
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-root

Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygems

BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygems
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
BuildRequires: %{?scl_prefix}rubygems-devel
%endif
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: krb5-devel
BuildRequires: %{?scl_prefix}rubygem-rake-compiler

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
The rkerberos library is an interface for the Kerberos 5 network
authentication protocol. It wraps the Kerberos C API.

%package doc
Summary: Documentation for rubygem-%{gem_name}
Group: Documentation
Requires: %{?scl_prefix}rubygem-%{gem_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for rubygem-%{gem_name}.



%prep
%setup -n %{pkg_name}-%{version} -q -T -c

%build

%{__rm} -rf %{buildroot}
mkdir -p ./%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}' --with-%{gem_name}-include=/usr/include/et"
%{?scl:scl enable %{scl} "}
gem install --local --install-dir ./%{gem_dir} -V --force %{SOURCE0}
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}/%{gem_dir}
# .so is copied into lib/
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/{ext,tmp}
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/.yardoc
# rake-compiler isn't needed on the system itself
sed -i '/rake-compiler/ s/runtime/development/' %{buildroot}/%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/MANIFEST
%{gem_instdir}/lib/rkerberos.so
%{gem_instdir}/rkerberos.gemspec
%{gem_cache}
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_docdir}
%{gem_instdir}/test
%{gem_instdir}/Rakefile


%changelog
* Thu May 23 2013 Dominic Cleal <dcleal@redhat.com> 0.1.1-4
- Remove rubygems version requirement (dcleal@redhat.com)

* Wed May 22 2013 Dominic Cleal <dcleal@redhat.com> 0.1.1-3
- Support building in non-SCL Ruby (dcleal@redhat.com)

* Tue May 21 2013 Martin Bačovský <mbacovsk@redhat.com> 0.1.1-2
- new package built with tito
- added support for SCL


* Wed May 08 2013 Dominic Cleal <dcleal@redhat.com> 0.1.1-1
- Update to 0.1.1 release
- Remove patch 103cea7d

* Wed May 08 2013 Dominic Cleal <dcleal@redhat.com> 0.1.0-1
- Initial 0.1.0 release
- Add patch 103cea7d (Add credential cache argument to get_init_creds_keytab)

