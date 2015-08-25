%global gem_name apipie-bindings

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

Summary: The Ruby bindings for Apipie documented APIs
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.13
Release: 2%{?dist}
Group: Development/Libraries
License: MIT
URL: http://github.com/Apipie/apipie-bindings
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(rest-client) < 1.8.0
Requires: %{?scl_prefix}rubygem(rest-client) >= 1.6.5
Requires: %{?scl_prefix}rubygem(awesome_print)
Requires: %{?scl_prefix}rubygem(oauth)
Requires: %{?scl_prefix_ruby}rubygem(json) >= 1.2.1

%if "%{?scl_ruby}" == "ruby193" || (0%{?el6} && 0%{!?scl:1})
Requires:      %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
%else
Requires:      %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
%endif

BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Bindings for API calls that are documented with Apipie. Bindings are generated on the fly.

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for %{name}

%description doc
This package contains documentation for %{name}.

%prep

%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/test


%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/doc


%changelog
* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.0.13-2
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Apr 23 2015 Dominic Cleal <dcleal@redhat.com> 0.0.13-1
- Update apipie-bindings to 0.0.13 (dcleal@redhat.com)

* Mon Mar 23 2015 Dominic Cleal <dcleal@redhat.com> 0.0.12-1
- Update apipie-bindings to 0.0.12 (dcleal@redhat.com)

* Mon Nov 10 2014 Dominic Cleal <dcleal@redhat.com> 0.0.11-1
- Update rubygem-apipie-bindings to 0.0.11 (martin.bacovsky@gmail.com)
- Remove unused fastercsv dependency (dcleal@redhat.com)

* Thu Sep 18 2014 Dominic Cleal <dcleal@redhat.com> 0.0.10-1
- Update rubygem-apipie-bindings to 0.0.10 (dcleal@redhat.com)

* Fri Aug 29 2014 Dominic Cleal <dcleal@redhat.com> 0.0.9-1
- Packaged /doc (martin.bacovsky@gmail.com)
- Update rubygem-apipie-bindings to 0.0.9 (martin.bacovsky@gmail.com)

* Thu Jul 17 2014 Lukas Zapletal <lzap+git@redhat.com> 0.0.8-4
- Fixed dependency in the -doc subpackage (lzap+git@redhat.com)
- Fixed doc subpackages (lzap+git@redhat.com)

* Thu Jul 17 2014 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.8-3
- Fixed dependency in the -doc subpackage

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 0.0.8-2
- Modernise and update for EL7 (dcleal@redhat.com)

* Wed May 07 2014 Martin Bačovský <martin.bacovsky@gmail.com> 0.0.8-1
- Update apipie-bindings to 0.0.8 (martin.bacovsky@gmail.com)

* Wed May 07 2014 Martin Bačovský <martin.bacovsky@gmail.com> 0.0.7-1
- Update apipie-bindings to 0.0.7 (martin.bacovsky@gmail.com)

* Fri Mar 21 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.6-1
- Bump to 0.0.6 (mbacovsk@redhat.com)

* Thu Mar 20 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.5-1
- Bump to 0.0.5 (mbacovsk@redhat.com)

* Wed Mar 19 2014 Jason Montleon <jmontleo@redhat.com> 0.0.4-3
- fix scl package name and provides for apipie-bindings (jmontleo@redhat.com)

* Wed Mar 19 2014 Jason Montleon <jmontleo@redhat.com> 0.0.4-2
- fix scl builds (jmontleo@redhat.com)

* Wed Mar 19 2014 Jason Montleon <jmontleo@redhat.com> 0.0.4-1
- new package built with tito

* Wed Mar 19 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.4-1
- new package built with tito

* Tue Feb 19 2014 Martin Bacovsky <mbacovsk@redhat.com> 0.0.4-1
- new package built with tito
