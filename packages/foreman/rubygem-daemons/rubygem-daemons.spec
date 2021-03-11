%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name daemons

Summary: A toolkit to create and control daemons in different ways
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.3
Release: 7%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://daemons.rubyforge.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel

%description
Daemons provides an easy way to wrap existing ruby scripts (for example a
self-written server)  to be run as a daemon and to be controlled by simple
start/stop/restart commands.  You can also call blocks as daemons and control
them from the parent or just daemonize the current process.  Besides this
basic functionality, daemons offers many advanced features like exception
backtracing and logging (in case your ruby script crashes) and monitoring and
automatic restarting of your processes if they crash.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T -n  %{gem_name}-%{version}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/Releases
%doc %{gem_instdir}/README.md

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.2.3-7
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.2.3-6
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.2.3-5
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.3-4
- Rebuild packages for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.2.3-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.2.3-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 07 2015 Dominic Cleal <dcleal@redhat.com> 1.2.3-1
- Update daemons to 1.2.3 (dcleal@redhat.com)

* Tue May 12 2015 Dominic Cleal <dcleal@redhat.com> 1.2.2-1
- Fixes #10362 - Update daemons to 1.2.2 (inecas@redhat.com)

* Tue Mar 17 2015 Dominic Cleal <dcleal@redhat.com> 1.2.1-1
- Update daemons to 1.2.1 (dcleal@redhat.com)
- Split docs into separate subpackage

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.4-7
- BR rubygems-devel (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.4-6
- do not regenerate gemspec (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.4-5
- wrap up generating gemspec in SC environment (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.4-4
- new package built with tito

* Mon Jul 16 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.4-3
- edit spec for fedora (msuchy@redhat.com)

* Mon Jul 11 2011 Mike McCune <mmccune@redhat.com> 1.1.4-2
- fixed new-lines in daemon.spec (dmitri@redhat.com)

* Wed Jul 06 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.1.4-1
- new package built with tito

* Wed Jul 06 2011  <wb@killing-time.appliedlogic.ca> - 1.1.4-1
- Initial package
