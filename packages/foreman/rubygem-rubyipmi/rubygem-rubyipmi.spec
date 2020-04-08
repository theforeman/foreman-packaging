# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rubyipmi

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.10.0
Release: 6%{?dist}
Summary: A ruby wrapper for ipmi command line tools that supports ipmitool and freeipmi
Group: Development/Languages
License: LGPLv2
URL: https://github.com/logicminds/rubyipmi
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: ipmitool

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
Provides a library for controlling IPMI devices using pure ruby code.


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
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/VERSION
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/RELEASE_NOTES.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rubyipmi.gemspec
%{gem_instdir}/spec

%changelog
* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.10.0-6
- Bump to release for EL8

* Tue Oct 01 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.10.0-5
- Update and rebuild into SCL

* Tue Sep 17 2019 Eric D. Helms <ericdhelms@gmail.com> 0.10.0-4
- Update to handle building for SCL

* Thu Sep 13 2018 Bryan Kearney <bryan.kearney@gmail.com> - 0.10.0-3
- Use LGPLv2 for versions 2 and 2.1 of the license

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.10.0-2
- Use gem_install macro (dominic@cleal.org)
- Converted spec files (dcleal@redhat.com)

* Mon Apr 13 2015 Dominic Cleal <dcleal@redhat.com> 0.10.0-1
- Update rubyipmi to 0.10.0 (dcleal@redhat.com)

* Fri Mar 20 2015 Dominic Cleal <dcleal@redhat.com> 0.9.2-1
- Update rubyipmi to 0.9.2 (dcleal@redhat.com)

* Wed Mar 11 2015 Dominic Cleal <dcleal@redhat.com> 0.9.1-1
- Update rubyipmi to 0.9.1 (dcleal@redhat.com)

* Tue Mar 10 2015 Dominic Cleal <dcleal@redhat.com> 0.9.0-1
- Update rubyipmi to 0.9.0 (dcleal@redhat.com)

* Tue Oct 28 2014 Michael Moll <mmoll@mmoll.at> 0.8.1-1
- Update to rubyipmi 0.8.1
- Reflect license change

* Mon May 19 2014 Dominic Cleal <dcleal@redhat.com> 0.7.0-2
- Modernise and update for EL7

* Thu Oct 17 2013 Dominic Cleal <dcleal@redhat.com> 0.7.0-1
- Rebase to rubyipmi 0.7.0 (dcleal@redhat.com)

* Mon Jul 08 2013 Dominic Cleal <dcleal@redhat.com> 0.6.0-2
- Add ipmitool dependency (dcleal@redhat.com)

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 0.6.0-1
- Rebase to rubyipmi 0.6.0 (dcleal@redhat.com)

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 0.5.1-1
- new package built with tito
