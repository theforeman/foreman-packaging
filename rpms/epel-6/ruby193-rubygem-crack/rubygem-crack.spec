%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name crack

Summary: Really simple JSON and XML parsing, ripped from Merb and Rails
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.1
Release: 6%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/jnunemaker/crack
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Keeping buildroot so I can use the same spec in EPEL5
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(bigdecimal)
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(bigdecimal)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
#BZ 781829
Epoch: 1

%description
Really simple JSON and XML parsing, ripped from Merb and Rails.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}

%description doc
This package contains documentation for %{pkg_name}.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}
rm -f %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/*.gemspec

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/History
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files doc
%defattr(-, root, root, -)
%{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Fri Mar 29 2013 Marek Hulan <ares@igloonet.cz> 0.3.1-6
- removed tests

* Fri Mar 29 2013 Marek Hulan <ares@igloonet.cz> 0.3.1-5
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:0.3.1-3
- Properly require the main package (with epoch) from the -doc subpackage.

* Wed Mar 07 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:0.3.1-2
- Update to 0.3.1

* Sun Feb 05 2012 <stahnma@fedoraproject.org> - 0.1.8-5
- Revert back to 0.1.8 as HTTParty can't use crack > 0.1.8

* Wed Dec 28 2011 <stahnma@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1
- Fix bz #715704

* Thu Nov 10 2011 Michael Stahnke <mastahnke@gmail.com> - 0.1.8-3
- rebuilt

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 23 2010 Michael Stahnke <stahnma@fedoraproject.org> - 0.1.8-1
- Broke package into main and doc
- Added tests
