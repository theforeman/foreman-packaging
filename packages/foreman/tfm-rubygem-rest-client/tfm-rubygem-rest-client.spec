%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name rest-client

Summary: Simple REST client for Ruby, inspired by microframework syntax for specifying actions
Name: tfm-rubygem-%{gem_name}
Version: 2.0.1
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/rest-client/rest-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix}rubygem(http-cookie) >= 1.0.2
Requires: %{?scl_prefix}rubygem(http-cookie) < 2.0
Requires: %{?scl_prefix_ror}rubygem(mime-types) >= 1.16
Requires: %{?scl_prefix_ror}rubygem(mime-types) < 4.0
Requires: %{?scl_prefix}rubygem(netrc) >= 0.8
Requires: %{?scl_prefix}rubygem(netrc) < 1.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A simple Simple HTTP and REST client for Ruby, inspired by the Sinatra
microframework style of specifying actions: get, put, post, delete.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -T -c
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

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
%defattr(-, root, root, -)
%{_bindir}/restclient
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/AUTHORS
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/history.md

%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/*.gemspec
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/Rakefile

%changelog
* Thu Aug 16 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.1-3
- Rebuild for Rails 5.2

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.1-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri Apr 07 2017 Dominic Cleal <dominic@cleal.org> 2.0.1-1
- Update rest-client to 2.0.1 (dominic@cleal.org)

* Wed May 25 2016 Dominic Cleal <dominic@cleal.org> 1.8.0-1
- Update rest-client to 1.8.0

* Wed May 25 2016 Dominic Cleal <dominic@cleal.org> 1.6.7-6
- Modernise and add -doc subpackage (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.6.7-5
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.6.7-4
- Fix build errors and modernise specs (dcleal@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.6.7-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Tue May 27 2014 Dominic Cleal <dcleal@redhat.com> 1.6.7-2
- Remove specific ABI version (dcleal@redhat.com)

* Tue May 27 2014 Dominic Cleal <dcleal@redhat.com> 1.6.7-1
- Update to 1.6.7, support RHEL 7

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.6.1-4
- BR rubygems-devel (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.6.1-3
- new package built with tito

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 1.6.1-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 1.6.1-1
- Initial package
