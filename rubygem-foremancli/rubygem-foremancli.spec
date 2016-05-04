%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foremancli

Summary: This is the CLI for Foreman, which is a provisioning tool and node classifier for sysadmins.
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 1.0
Release: 9%{?dist}
Group: Development/Ruby
License: GPLv2+
URL: https://github.com/ohadlevy/foreman/blob/master/extras/cli/foremancli
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems

Requires: %{?scl_prefix}rubygem-rest-client => 1.4
Requires: %{?scl_prefix}rubygem-rest-client < 2

Requires: %{?scl_prefix_ruby}rubygem-json => 1.4
Requires: %{?scl_prefix_ruby}rubygem-json < 2
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(foremancli) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%define gembuilddir %{buildroot}%{gem_dir}

%description
This is the CLI for Foreman, which is a provisioning tool and node classifier
for sysadmins.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

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
* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 1.0-9
- Use gem_install macro (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.0-8
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.0-7
- Converted to tfm SCL (dcleal@redhat.com)
- Fixes #9703 - change %%{dist} to %%{?dist} (jmontleo@redhat.com)
- Add full rubygems.org source URL (dcleal@redhat.com)

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
