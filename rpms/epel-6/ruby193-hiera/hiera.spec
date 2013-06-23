%{?scl:%scl_package hiera}
%{!?scl:%global pkg_name %{name}}

%if 0%{?el5}
%global with_checks 0
%else
%global with_checks 1
%endif

Name:           %{?scl_prefix}hiera
Version:        1.0.0
Release:        5%{?dist}
Summary:        A simple hierarchical database supporting plugin data sources

Group:          System Environment/Base
License:        ASL 2.0
URL:            http://projects.puppetlabs.com/projects/%{pkg_name}/
Source0:        http://downloads.puppetlabs.com/hiera/%{pkg_name}-%{version}.tar.gz
# We use a copy of misreleased 'newer' version of 1.0.0
# http://projects.puppetlabs.com/issues/16621
Source1:        hiera.yaml
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
%if 0%{?with_checks}
BuildRequires:  %{?scl_prefix}rubygem(rspec)
BuildRequires:  %{?scl_prefix}rubygem(mocha)
%endif
BuildRequires:  %{?scl_prefix}ruby-devel
Requires:       %{?scl_prefix}ruby(abi) = 1.9.1

%description
A simple hierarchical database supporting plugin data sources.

%prep
%setup -n %{pkg_name}-%{version} -q
cp -p %{SOURCE1} hiera.yaml

%build
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_vendorlibdir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_bindir}
cp -pr lib/hiera %{buildroot}%{ruby_vendorlibdir} 
cp -pr lib/hiera.rb %{buildroot}%{ruby_vendorlibdir} 
install -p -m0755 bin/hiera %{buildroot}%{_bindir}
install -p -m0644 hiera.yaml %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_var}/lib/hiera

%check
%if 0%{?with_checks}
%{?scl:scl enable %{scl} "}
ruby spec/spec_helper.rb
%{?scl:"}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/hiera
%{ruby_vendorlibdir}/hiera.rb
%{ruby_vendorlibdir}/hiera
%dir %{_var}/lib/hiera
%config(noreplace) %{_sysconfdir}/hiera.yaml
%doc CHANGELOG COPYING README.md LICENSE

%changelog
* Thu Mar 21 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.0-5
- use rspec instead of rspec-core (msuchy@redhat.com)

* Thu Mar 21 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.0-4
- new package built with tito

* Mon Oct 1 2012 Steve Traylen <steve.traylen@cern.ch> - 1.0.0-3
- Correct ruby(abi) requirement.

* Thu Sep 27 2012 Steve Traylen <steve.traylen@cern.ch> - 1.0.0-2
- Remove _isa tag for f18 from ruby-devel?

* Thu Sep 27 2012 Steve Traylen <steve.traylen@cern.ch> - 1.0.0-1
- Update to 1.0.0
- Add LICENSE file
- Add /var/lib/hiera as default data path.

* Wed May 30 2012 Steve Traylen <steve.traylen@cern.ch> - 1.0.0-0.2.rc3
- Update to 1.0.0rc3 and drop puppet functions.

* Wed May 16 2012 Steve Traylen <steve.traylen@cern.ch> - 1.0.0-0.2rc2
- Adapt to fedora guidelines.

* Mon May 14 2012 Matthaus Litteken <matthaus@puppetlabs.com> - 1.0.0-0.1rc2
- 1.0.0rc2 release

* Mon May 14 2012 Matthaus Litteken <matthaus@puppetlabs.com> - 1.0.0-0.1rc1
- 1.0.0rc1 release

* Thu May 03 2012 Matthaus Litteken <matthaus@puppetlabs.com> - 0.3.0.28-1
- Initial Hiera Packaging. Upstream version 0.3.0.28

