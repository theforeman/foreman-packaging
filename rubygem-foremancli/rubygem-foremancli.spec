%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foremancli

Summary: This is the CLI for Foreman, which is a provisioning tool and node classifier for sysadmins.
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 1.0
Release: 6%{dist}
Group: Development/Ruby
License: GPLv2+
URL: https://github.com/ohadlevy/foreman/blob/master/extras/cli/foremancli
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems

Requires: %{?scl_prefix}rubygem-rest-client => 1.4
Requires: %{?scl_prefix}rubygem-rest-client < 2

Requires: %{?scl_prefix}rubygem-json => 1.4
Requires: %{?scl_prefix}rubygem-json < 2
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(foremancli) = %{version}

%define gembuilddir %{buildroot}%{gem_dir}

%description
This is the CLI for Foreman, which is a provisioning tool and node classifier
for sysadmins.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -T -c

%build

%install
mkdir -p %{gembuilddir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
%{?scl:"}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin
rm -rf %{buildroot}%{gem_instdir}/.yardoc

%files
%{_bindir}/foremancli
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_docdir}

%changelog
* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 1.0-6
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Wed Mar 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.0-4
- put correct license in spec (msuchy@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 1.0-3
- new package built with tito

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 1.0-2
- polish the spec (msuchy@redhat.com)

* Thu Sep 06 2012 Miroslav Suchý <msuchy@redhat.com> 1.0-1
- new package built with tito

