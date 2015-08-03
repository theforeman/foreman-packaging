%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name concurrent-ruby-edge
%global rubyabi 1.9.1

Summary: Edge concepts for the modern concurrency tools for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.0
Release: 1%{?dist}
Group: Development/Languages

License: MIT
URL: https://github.com/ruby-concurrency/concurrent-ruby
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}ruby(rubygems)
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
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
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
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
* Mon Aug 03 2015 Ivan Nečas <inecas@redhat.com> 0.1.0-1
- Update concurrent-ruby-edge to 0.1.0 (inecas@redhat.com)
- Automatic commit of package [rubygem-concurrent-ruby-edge] minor release
  [0.1.0.pre3-1]. (dcleal@redhat.com)
- Initial build of concurrent-ruby library (inecas@redhat.com)

* Thu Jul 02 2015 Ivan Nečas <inecas@redhat.com>
- new package built with tito


