# Generated from rest-client-2.0.2.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rest-client

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.2
Release: 4%{?dist}
Summary: Simple HTTP and REST client for Ruby, inspired by microframework syntax for specifying actions
Group: Development/Languages
License: MIT
URL: https://github.com/rest-client/rest-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.0.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(http-cookie) >= 1.0.2
Requires: %{?scl_prefix}rubygem(http-cookie) < 2.0
Requires: %{?scl_prefix}rubygem(mime-types) >= 1.16
Requires: %{?scl_prefix}rubygem(mime-types) < 4.0
Requires: %{?scl_prefix}rubygem(netrc) >= 0.8
Requires: %{?scl_prefix}rubygem(netrc) < 1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.0.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
A simple HTTP and REST client for Ruby, inspired by the Sinatra microframework
style of specifying actions: get, put, post, delete.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/restclient
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop-disables.yml
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/AUTHORS
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/history.md
%{gem_instdir}/rest-client.gemspec
%exclude %{gem_instdir}/rest-client.windows.gemspec
%{gem_instdir}/spec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.2-4
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.2-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.2-2
- Update spec to remove the ror scl

* Fri Apr 26 2019 Evgeni Golov 2.0.2-1
- Update to 2.0.2-1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.1-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.1-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri Apr 07 2017 Dominic Cleal <dominic@cleal.org> 2.0.1-1
- Update rest-client to 2.0.1 (dominic@cleal.org)

* Wed May 25 2016 Dominic Cleal <dominic@cleal.org> 1.8.0-1
- Update rest-client to 1.8.0

* Wed May 25 2016 Dominic Cleal <dominic@cleal.org> 1.6.7-6
- Modernise and add -doc subpackage (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.6.7-5
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.6.7-4
- Fix build errors and modernise specs (dcleal@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.6.7-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Tue May 27 2014 Dominic Cleal <dcleal@redhat.com> 1.6.7-2
- Remove specific ABI version (dcleal@redhat.com)

* Tue May 27 2014 Dominic Cleal <dcleal@redhat.com> 1.6.7-1
- Update to 1.6.7, support RHEL 7

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.6.1-4
- BR rubygems-devel (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.6.1-3
- new package built with tito

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 1.6.1-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 1.6.1-1
- Initial package
