# Generated from little-plugger-1.1.4.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name little-plugger

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.4
Release: 3%{?dist}
Summary: LittlePlugger is a module that provides Gem based plugin management
Group: Development/Languages
License: MIT
URL: https://rubygems.org/gems/little-plugger
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
LittlePlugger is a module that provides Gem based plugin management.
By extending your own class or module with LittlePlugger you can easily
manage the loading and initializing of plugins provided by other gems.


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

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
# contains licensing information
%doc %{gem_instdir}/README.rdoc

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.1.4-3
- Rebuild against rh-ruby27

* Thu Mar 26 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.1.4-2
- Rebuild for EL8

* Fri Apr 26 2019 Evgeni Golov 1.1.4-1
- Update to 1.1.4-1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.1.3-23
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.1.3-22
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.1.3-21
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.1.3-20
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.1.3-19
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 1.1.3-18
- Modernise and update for EL7 (dcleal@redhat.com)

* Wed Aug 28 2013 Dominic Cleal <dcleal@redhat.com> 1.1.3-17
- Don't override gem macros when building under SCL (dcleal@redhat.com)

* Wed Aug 21 2013 Dominic Cleal <dcleal@redhat.com> 1.1.3-16
- Remove timestamps from gemspec dates (dcleal@redhat.com)

* Tue Aug 20 2013 Dominic Cleal <dcleal@redhat.com> 1.1.3-15
- fix dependency on ruby(abi) for ruby193 SCL builds (dcleal@redhat.com)

* Fri Aug 16 2013 Sam Kottler <shk@redhat.com> 1.1.3-14
- Use updated logic for ruby-abi and ruby-release (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.1.3-13
- Fix logic and add whitelist (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.1.3-12
- Grumble grumble (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.1.3-11
- Weird logic change (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.1.3-10
- Fix some broken logic (shk@redhat.com)
- Untwisted the little-plugger spec (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.1.3-9
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.1.3-6
- fixing ruby193 scl package (lzap+git@redhat.com)

* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.1.3-5
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.3-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.3-1
- Update to 1.1.3 version (migrates tests to rspec 2, thanks Vit Ondruch for patch for upstream).

* Wed Nov 02 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.2-3
- Introduced doc subpackage.
- Introduced check section.
- Removed rspec from Requires and moved it to BuildRequires, as it is only needed for running specs.

* Sat Apr 02 2011 Chris Lalancette <clalance@redhat.com> - 1.1.2-2
- Use the gem from rubygems.org instead of from git

* Wed Mar 16 2011 Chris Lalancette <clalance@redhat.com> - 1.1.2-1
- Initial package
