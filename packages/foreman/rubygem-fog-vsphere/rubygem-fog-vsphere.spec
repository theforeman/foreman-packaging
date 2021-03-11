# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-vsphere
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.5.0
Release: 2%{?dist}
Summary: Module for the 'fog' gem to support VMware vSphere
Group: Development/Languages
License: MIT
URL: https://github.com/fog/fog-vsphere
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Autoreq: 0

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.0.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(fog-core)
Requires: %{?scl_prefix}rubygem(rbvmomi) >= 1.9
Requires: %{?scl_prefix}rubygem(rbvmomi) < 3
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.0.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
This library can be used as a module for `fog` or as standalone provider to
use vSphere in applications.


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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/Jenkinsfile
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fog-vsphere.gemspec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.5.0-2
- Rebuild against rh-ruby27

* Wed Dec 09 2020 Ondřej Ezr <oezr@redhat.com> 3.5.0-1
- Update to 3.5.0

* Wed Jul 22 2020 Ondřej Ezr <oezr@redhat.com> 3.4.0-1
- Update to 3.4.0-1

* Wed May 13 2020 Ondřej Ezr <oezr@redhat.com> 3.3.1-1
- Update to 3.3.1

* Sat Apr 11 2020 Koen Torfs <koen@fwd.be> 3.3.0-1
- Update to 3.3.0 for EL8

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.5-2
- Bump to release for EL8

* Mon Mar 09 2020 Ondřej Ezr <oezr@redhat.com> 3.2.5-1
- Update to 3.2.5

* Wed Feb 05 2020 Chris Roberts <chrobert@redhat.com> 3.2.3-1
- Update to 3.2.3

* Fri Jan 24 2020 Chris Roberts <chrobert@redhat.com> 3.2.2-1
- Update to 3.2.2

* Thu Aug 29 2019 Ondřej Ezr <oezr@redhat.com> 3.2.1-1
- Update to 3.2.1

* Thu Jul 18 2019 Ondřej Ezr <oezr@redhat.com> 3.2.0-1
- Update to 3.2.0

* Mon Jun 10 2019 Ondřej Ezr <oezr@redhat.com> 3.1.1-1
- Update to 3.1.1

* Thu Mar 28 2019 Marek Hulan <mhulan@redhat.com> 3.0.0-2
- Update dependencies

* Thu Mar 21 2019 Marek Hulan <mhulan@redhat.com> 3.0.0-1
- Update to 3.0.0

* Mon Nov 19 2018 Chris Roberts <chrobert@redhat.com> - 2.5.0-1
- Update fog-vsphere to 2.5.0

* Tue Oct 16 2018 Timo Goebel <mail@timogoebel.name> - 2.4.0-1
- Update fog-vsphere to 2.4.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon Jul 09 2018 Chris Roberts <chrobert@redhat.com> 2.3.0-1
- Update to 2.3.0

* Fri Apr 06 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.1.0-1
- Update to 2.1.0

* Tue Jan 16 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.13.1-1
- Bump rubygem-fog-vsphere to 1.13.1 (ewoud@kohlvanwijngaarden.nl)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.11.3-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)

* Wed Dec 27 2017 Daniel Lobato Garcia <me@daniellobato.me> 1.11.3-1
- Update fog-vsphere to 1.11.3 (me@daniellobato.me)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri May 12 2017 Dominic Cleal <dominic@cleal.org> 1.9.2-1
- Update fog-vsphere to 1.9.2 (mhulan@redhat.com)

* Mon Apr 03 2017 Dominic Cleal <dominic@cleal.org> 1.9.0-1
- Update fog-vsphere to 1.9.0 (dominic@cleal.org)

* Tue Jan 31 2017 Dominic Cleal <dominic@cleal.org> 1.7.0-1
- Update fog-vsphere to 1.7.0 (dominic@cleal.org)

* Tue Jan 03 2017 Dominic Cleal <dominic@cleal.org> 1.6.0-1
- Update fog-vsphere to 1.6.0 (dominic@cleal.org)

* Wed Oct 19 2016 Dominic Cleal <dominic@cleal.org> 1.4.0-1
- Update fog-vsphere to 1.4.0 (dominic@cleal.org)

* Fri Jul 29 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- Update fog-vsphere to 1.0.0 (dominic@cleal.org)

* Thu Jun 16 2016 Dominic Cleal <dominic@cleal.org> 0.8.0-1
- Update fog-vsphere to 0.8.0 (dominic@cleal.org)

* Tue May 17 2016 Dominic Cleal <dominic@cleal.org> 0.7.0-1
- Update fog-vsphere to 0.7.0 (dominic@cleal.org)

* Wed Mar 09 2016 Dominic Cleal <dominic@cleal.org> 0.6.3-1
- Update fog-vsphere to 0.6.3 (dominic@cleal.org)

* Fri Mar 04 2016 Dominic Cleal <dominic@cleal.org> 0.6.1-1
- Update fog-vsphere to 0.6.1 (dominic@cleal.org)

* Mon Feb 01 2016 Dominic Cleal <dcleal@redhat.com> 0.6.0-1
- Update fog-vsphere to 0.6.0 (dcleal@redhat.com)

* Tue Jan 19 2016 Dominic Cleal <dcleal@redhat.com> 0.5.0-1
- new package built with tito
