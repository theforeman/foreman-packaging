# template: default
%global gem_name locale

Name: rubygem-%{gem_name}
Version: 2.1.4
Release: 1%{?dist}
Summary: Pure ruby library which provides basic APIs for localization
License: Ruby and LGPLv3+
URL: https://github.com/ruby-gettext/locale
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Ruby-Locale is the pure ruby library which provides basic APIs for
localization.


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
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%exclude %{gem_instdir}/locale.gemspec
%{gem_instdir}/samples
%{gem_instdir}/test

%changelog
* Sun May 26 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.1.4-1
- Update to 2.1.4

* Tue Jul 26 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.1.3-1
- Update to 2.1.3

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.9-15
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.9-14
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.9-13
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.9-12
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)
- Remove unused non-SCL awesome_print, locale gems (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 2.0.9-11
- Remove touch from prep to not touch root-owned files (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 2.0.9-10
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 2.0.9-9
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)
- Add full rubygems.org source URL (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 2.0.9-8
- Modernise and update for EL7 (dcleal@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-7
- new package built with tito

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-6
- further rpm spec file fixes (jmontleo@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-5
- fix provides in rpm spec (jmontleo@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-4
- more rpm spec file fixes (jmontleo@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-3
- disable checks for now (jmontleo@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-2
- fix (build)requires (jmontleo@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-1
- make corrections to rpm spec file (jmontleo@redhat.com)

* Thu Sep 12 2013 Jason Montleon <jmontleo@redhat.com> 2.0.8-4
- new package built with tito

* Wed May 08 2013 Dominic Cleal <dcleal@redhat.com> 2.0.8-3
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Tue Mar 12 2013 Lukas Zapletal <lzap+git@redhat.com> 2.0.8-2
- new package built with tito

* Tue Sep 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.0.8-1
- 2.0.8

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.5-5
- Fix conditionals for F17 to work for RHEL 7 as well.

* Sun Jan 29 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.0.5-4
- F-17: rebuild against ruby 1.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 12 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- gems.rubyforge.org gem file seems old, changing Source0 URL for now

* Wed Nov 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.5-1
- 2.0.5
- Fix the license tag

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.4-2
- F-12: Mass rebuild

* Wed May 27 2009  Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.4-1
- 2.0.4

* Mon May 11 2009  Mamoru Tasaka <mtasaka@ios.s.u-tokyo.ac.jp> - 2.0.3-1
- 2.0.3

* Tue Apr 21 2009  Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.1-1
- 2.0.1

* Thu Mar 26 2009  Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-1
- Initial package
