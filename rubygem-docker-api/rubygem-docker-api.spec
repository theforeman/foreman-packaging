%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name docker-api
%global rubyabi 1.9.1

Summary: A simple REST client for the Docker Remote API
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.17.0
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/swipely/docker-api
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(archive-tar-minitar)
Requires: %{?scl_prefix}rubygem(excon) >= 0.38
Requires: %{?scl_prefix_ruby}rubygem(json)
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This gem provides an object-oriented interface to the Docker Remote API. Every
method listed there is implemented, with the exception of attaching to the
STDIN of a Container. At the time of this writing, docker-api is meant to
interface with Docker version 0.9.*.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{name}


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
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/*.gemspec
%{gem_spec}

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/TESTING.md

%changelog
* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.17.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jan 13 2015 Dominic Cleal <dcleal@redhat.com> 1.17.0-1
- Update docker-api to 1.17.0 (dcleal@redhat.com)

* Tue Nov 25 2014 Dominic Cleal <dcleal@redhat.com> 1.15.0-1
- Update docker-api to 1.15.0 (dcleal@redhat.com)

* Wed Oct 22 2014 David Davis <daviddavis@redhat.com> 1.13.6-1
- Updating to docker-api 1.13.6 for foreman_docker 0.1.0

* Wed Apr 30 2014 Dominic Cleal <dcleal@redhat.com> 1.8.4-2
- Fix pkg_name macro for -doc require (dcleal@redhat.com)

* Tue Apr 29 2014 Dominic Cleal <dcleal@redhat.com> 1.8.4-1
- new package built with tito
