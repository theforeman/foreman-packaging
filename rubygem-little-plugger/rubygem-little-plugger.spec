%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name little-plugger

Summary: LittlePlugger is a module that provides Gem based plugin management
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.3
Release: 19%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/little-plugger
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(rubygems)

%if "%{?scl_ruby}" == "ruby193" || (0%{?el6} && 0%{!?scl:1})
Requires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
%endif

BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
#BuildRequires: %{?scl_prefix_ruby}rubygem(rspec)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
LittlePlugger is a module that provides Gem based plugin management.
By extending your own class or module with LittlePlugger you can easily
manage the loading and initializing of plugins provided by other gems.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# Workaround for rubygems being able to parse a timestamp in a date
find %{buildroot}/%{gem_spec} -name %{gem_name}-%{version}.gemspec -exec sed -i 's/ 00:00:00.000000000Z//' {} +

%check

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%{gem_instdir}/lib
%{gem_instdir}/spec
%exclude %{gem_cache}
%{gem_spec}
# contains licensing information
%doc %{gem_instdir}/README.rdoc

%files doc
%{gem_instdir}/spec
%{gem_instdir}/Rakefile
%doc %{gem_docdir}/ri
%doc %{gem_docdir}/rdoc
%doc %{gem_instdir}/History.txt

%changelog
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
