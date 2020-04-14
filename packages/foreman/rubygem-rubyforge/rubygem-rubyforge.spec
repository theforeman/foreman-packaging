# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rubyforge

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.4
Release: 10%{?dist}
Summary: A script which automates a limited set of rubyforge operations
Group: Development/Languages
License: MIT
URL: http://codeforpeople.rubyforge.org/rubyforge/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby 
Requires: %{?scl_prefix_ruby}ruby(rubygems) 
Requires: %{?scl_prefix_ruby}rubygem(json) >= 1.1.7
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby 
BuildRequires: %{?scl_prefix_ruby}rubygems-devel 
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
A script which automates a limited set of rubyforge operations.
* Run 'rubyforge help' for complete usage.
* Setup: For first time users AND upgrades to 0.4.0:
* rubyforge setup (deletes your username and password, so run sparingly!)
* edit ~/.rubyforge/user-config.yml
* rubyforge config
* For all rubyforge upgrades, run 'rubyforge config' to ensure you have
latest.


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

# json_pure -> json
find . -name Rakefile -or -name \*.gemspec | \
	xargs sed -i -e 's|json_pure|json|g'

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
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/rubyforge
%{gem_instdir}/Manifest.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Tue Apr 14 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.4-10
- Change the scl_prefix for json requirement

* Thu Apr 09 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.4-9
- Bump release to build for el8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.4-8
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.4-7
- Final set of rebuilds (ericdhelms@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 2.0.4-6
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 2.0.4-5
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.4-3
- new package built with tito

* Mon Jul 02 2012 Lukas Zapletal <lzap+git@redhat.com> 2.0.4-2
- first build

* Thu Mar  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.4-1
- Update to 2.0.4
- Replace json_pure to json (bug 570252)

* Mon Feb 15 2010 Darryl L. Pierce <dpierce@redhat.com> - 2.0.3-1
- Added new dependency on rubygem-json >= 1.1.7.
- Release 2.0.3 of RubyForge.

* Tue Sep 15 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.0.5-1
- Release 1.0.5 of RubyForge.

* Sat Aug  8 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.0.4-1
- Release 1.0.4 of RubyForge.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Darryl Pierce <dpierce@redhat.com> - 1.0.3-1
- Release 1.0.3 of RubyForge.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Darryl Pierce <dpierce@redhat.com> - 1.0.2-2
- Provided the wrong gem as source.

* Tue Jan 06 2009 Darryl Pierce <dpierce@redhat.com> - 1.0.2-1
- Release 1.0.2 of Rubyforge.

* Thu Oct 23 2008 Darryl Pierce <dpierce@redhat.com> - 1.0.1-1
- Release 1.0.1 of Rubyforge.

* Mon Jun 09 2008 Darryl Pierce <dpierce@redhat.com> - 1.0.0-1
- New version of RubyForge released.

* Wed May 14 2008 Darryl Pierce <dpierce@redhat.com> - 0.4.5-2
- Figured out how to do a proper build.

* Mon May 12 2008 Darryl Pierce <dpierce@redhat.com> - 0.4.5-1
- New version of the gem released.

* Tue Apr 29 2008 Darryl Pierce <dpierce@redhat.com> - 0.4.4-3
- Fixed the executable attribute for rubyforge.rb.

* Mon Apr 28 2008 Darryl Pierce <dpierce@redhat.com> - 0.4.4-2
- Updated the spec to comply with Ruby packaging guidelines.

* Fri Apr 18 2008 Darryl Pierce <dpierce@redhat.com> - 0.4.4-1
- Initial package
