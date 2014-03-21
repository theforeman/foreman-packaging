%global gem_name apipie-bindings

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%if !("%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16)
%global gem_dir /usr/lib/ruby/gems/1.8
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_libdir %{gem_instdir}/lib
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%endif

%global geminstdir %{gem_dir}/gems/%{gem_name}-%{version}

Summary: The Ruby bindings for Apipie documented APIs
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.6
Release: 1%{?dist}
Group: Development/Libraries
License: GPLv3
URL: http://github.com/Apipie/apipie-bindings
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: rubygem(rest-client)
Requires: rubygem(awesome_print)
Requires: rubygem(fastercsv)
Requires: rubygem(oauth)
Requires: rubygem(json)
Requires: rubygem(mime-types) < 2.0.0

%if "%{?scl}" == "ruby193"
Requires: %{?scl_prefix}ruby-wrapper
BuildRequires: %{?scl_prefix}ruby-wrapper
%endif

%if 0%{?fedora} > 18
Requires: ruby(release) = 2.0.0
BuildRequires: ruby(release) = 2.0.0
BuildRequires: rubygems-devel
%else
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires:  %{?scl_prefix}rubygems-devel
%else
Requires: ruby(abi) = 1.8
BuildRequires: ruby(abi) = 1.8
%endif
%endif
Requires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems

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
%dir %{geminstdir}
%{geminstdir}/lib
%doc %{geminstdir}/LICENSE
%{geminstdir}/test


%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{geminstdir}/README.md
%doc %{geminstdir}/LICENSE


%changelog
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
