# template: default
%global gem_name concurrent-ruby

Name: rubygem-%{gem_name}
Version: 1.1.10
Release: 1%{?dist}
Epoch: 1
Summary: Modern concurrency tools for Ruby
License: MIT
URL: https://www.concurrent-ruby.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.2
BuildRequires: ruby >= 2.2
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Modern concurrency tools including agents, futures, promises, thread pools,
actors, supervisors, and more. Inspired by Erlang, Clojure, Go, JavaScript,
actors, and classic concurrency patterns.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
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
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/ext
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Wed Jul 27 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.1.10-1
- Update to 1.1.10

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1:1.1.6-3
- Rebuild against rh-ruby27

* Thu Mar 12 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1:1.1.6-2
- Update all rails packages for el8

* Thu Mar 05 2020 Adam Ruzicka <aruzicka@redhat.com> 1:1.1.6-1
- Update to 1.1.6

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1:1.1.4-4
- Update spec to include Obsoletes of rails-packaging version

* Wed Jan 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1:1.1.4-3
- Bump for moving from rails-packaging to foreman-packging

* Tue Jan 08 2019 Eric D. Helms <ericdhelms@gmail.com> - 1:1.1.4-2
- Drop foremandist

* Fri Jan 04 2019 Ivan Nečas <inecas@redhat.com> 1:1.1.4-1
- Update to 1.1.4

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
