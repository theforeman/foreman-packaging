%global gem_name apipie-bindings

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

Summary: The Ruby bindings for Apipie documented APIs
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.8
Release: 2%{?dist}
Group: Development/Libraries
License: GPLv3
URL: http://github.com/Apipie/apipie-bindings
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(rest-client)
Requires: %{?scl_prefix}rubygem(awesome_print)
Requires: %{?scl_prefix}rubygem(fastercsv)
Requires: %{?scl_prefix}rubygem(oauth)
Requires: %{?scl_prefix}rubygem(json) >= 1.2.1
Requires: %{?scl_prefix}rubygem(mime-types) < 2.0.0

%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
Requires:      %{?scl_prefix}ruby(abi)
BuildRequires: %{?scl_prefix}ruby(abi)
BuildRequires: %{?scl_prefix}rubygems-devel
%else
Requires:      %{?scl_prefix}ruby(release)
BuildRequires: %{?scl_prefix}ruby(release)
BuildRequires: %{?scl_prefix}rubygems-devel
%endif

BuildRequires: %{?scl_prefix}ruby(rubygems)
BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Bindings for API calls that are documented with Apipie. Bindings are generated on the fly.

%package doc
BuildArch:  noarch
Requires:   %{gem_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

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


%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE


%changelog
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
