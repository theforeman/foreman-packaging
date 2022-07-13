# template: default
%global gem_name daemons

Name: rubygem-%{gem_name}
Version: 1.4.1
Release: 1%{?dist}
Summary: A toolkit to create and control daemons in different ways
License: MIT
URL: https://github.com/thuehlinger/daemons
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Daemons provides an easy way to wrap existing ruby scripts (for example a
self-written server)  to be run as a daemon and to be controlled by simple
start/stop/restart commands.
You can also call blocks as daemons and control them from the parent or just
daemonize the current process.
Besides this basic functionality, daemons offers many advanced features like
exception backtracing and logging (in case your ruby script crashes) and
monitoring and automatic restarting of your processes if they crash.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Releases
%{gem_instdir}/examples

%changelog
* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.4.1-1
- Update to 1.4.1

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
