%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name concurrent-ruby-edge

Summary: Edge concepts for the modern concurrency tools for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.6.0
Release: 3%{?foremandist}%{?dist}
Epoch: 1
Group: Development/Languages

License: MIT
URL: https://github.com/ruby-concurrency/concurrent-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(concurrent-ruby) >= 1.1.6
Requires: %{?scl_prefix}rubygem(concurrent-ruby) < 1.2.0

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
Edge concepts for modern concurrency tools including agents, futures,
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
%license %{gem_instdir}/LICENSE.md
%doc %{gem_instdir}/CHANGELOG.md
%{gem_libdir}/concurrent-ruby-edge

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1:0.6.0-3
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1:0.6.0-2
- Bump to release for EL8

* Wed Mar 04 2020 Adam Ruzicka <aruzicka@redhat.com> 1:0.6.0-1
- Update to 0.6.0

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1:0.4.1-2
- Update spec to remove the ror scl

* Fri Jan 04 2019 Ivan Nečas <inecas@redhat.com> 1:0.4.1-1
- Update to 0.4.1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1:0.2.4-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Jan 04 2018 Eric D. Helms <ericdhelms@gmail.com> 0.2.4-1
- Bump concurrent-ruby-edge to 0.2.4 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue Mar 21 2017 Dominic Cleal <dominic@cleal.org> 0.2.3-1
- Update dynflow to 0.8.21 (me@daniellobato.me)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.2.0-4
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.2.0-3
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Jan 05 2016 Dominic Cleal <dcleal@redhat.com> 0.2.0-2
- Add foremandist to plugin dependencies (dcleal@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- Update concurrent-ruby-edge to 0.2.0 (stbenjam@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-5
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-4
- Package concurrent-ruby for non-SCL el7 (stbenjam@redhat.com)

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
