%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name concurrent-ruby

Summary: Modern concurrency tools for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.3
Release: 7%{?foremandist}%{?dist}
Epoch: 1
Group: Development/Languages

License: MIT
URL: https://github.com/ruby-concurrency/concurrent-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby

%if 0%{?el6} && 0%{!?scl:1}
Requires: %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Modern concurrency tools including agents, futures,
promises, thread pools, actors, supervisors, and more. Inspired by
Erlang, Clojure, Go, JavaScript, actors, and classic concurrency
patterns.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

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
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_docdir}

%changelog
* Thu Aug 16 2018 Eric D. Helms <ericdhelms@gmail.com> - 1:1.0.3-7
- Rebuild for Rails 5.2

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.0.3-6
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue Mar 21 2017 Dominic Cleal <dominic@cleal.org> 1.0.3-1
- Update dynflow to 0.8.21 (me@daniellobato.me)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Mon Feb 29 2016 Dominic Cleal <dominic@cleal.org> 1.0.1-1
- Update concurrent-ruby to 1.0.1 (dominic@cleal.org)

* Tue Jan 05 2016 Dominic Cleal <dcleal@redhat.com> 1.0.0-2
- Add foremandist to plugin dependencies (dcleal@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.0.0-1
- Update concurrent-ruby to 1.0.0 (stbenjam@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.9.0-5
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.9.0-4
- Package concurrent-ruby for non-SCL el7 (stbenjam@redhat.com)

* Thu Aug 06 2015 Dominic Cleal <dcleal@redhat.com> 0.9.0-3
- Fix dep to include epoch between -doc and main package (dcleal@redhat.com)

* Wed Aug 05 2015 Dominic Cleal <dcleal@redhat.com> 0.9.0-2
- Increase the epoch number for the concurrent-ruby gems (inecas@redhat.com)

* Mon Aug 03 2015 Ivan Nečas <inecas@redhat.com> 0.9.0-1
- Update concurrent-ruby to 0.9.0 (inecas@redhat.com)
- Automatic commit of package [rubygem-concurrent-ruby] minor release
  [0.9.0.pre3-1]. (dcleal@redhat.com)
- Initial build of concurrent-ruby library (inecas@redhat.com)

* Thu Jul 02 2015 Ivan Nečas <inecas@redhat.com>
- new package built with tito
