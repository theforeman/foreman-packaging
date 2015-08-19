%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name concurrent-ruby-edge

Summary: Edge concepts for the modern concurrency tools for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.0
Release: 4%{?dist}
Epoch: 1
Group: Development/Languages

License: MIT
URL: https://github.com/ruby-concurrency/concurrent-ruby
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby

%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
Requires: %{?scl_prefix}ruby(abi)
BuildRequires: %{?scl_prefix}ruby(abi)
%else
Requires: %{?scl_prefix}ruby(release)
BuildRequires: %{?scl_prefix}ruby(release)
%endif

BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Edge concepts for modern concurrency tools including agents, futures,
promises, thread pools, actors, supervisors, and more. Inspired by
Erlang, Clojure, Go, JavaScript, actors, and classic concurrency
patterns.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            -V --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.txt
%{gem_libdir}

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}

%changelog
* Thu Aug 06 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-3
- Fix dep to include epoch between -doc and main package (dcleal@redhat.com)

* Wed Aug 05 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-2
- Increase the epoch number for the concurrent-ruby gems (inecas@redhat.com)

* Mon Aug 03 2015 Ivan Nečas <inecas@redhat.com> 0.1.0-1
- Update concurrent-ruby-edge to 0.1.0 (inecas@redhat.com)
- Automatic commit of package [rubygem-concurrent-ruby-edge] minor release
  [0.1.0.pre3-1]. (dcleal@redhat.com)
- Initial build of concurrent-ruby library (inecas@redhat.com)

* Thu Jul 02 2015 Ivan Nečas <inecas@redhat.com>
- new package built with tito


