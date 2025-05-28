# template: default
%global gem_name fog-vsphere

Name: rubygem-%{gem_name}
Version: 3.7.1
Release: 1%{?dist}
Summary: Module for the 'fog' gem to support VMware vSphere
License: MIT
URL: https://github.com/fog/fog-vsphere
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7
BuildRequires: ruby >= 2.7
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
This library can be used as a module for `fog` or as standalone provider to
use vSphere in applications.


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
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/tests

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fog-vsphere.gemspec

%changelog
* Tue May 06 2025 Chris Roberts <chrobert@redhat.com> - 3.7.1-1
- Update to 3.7.1

* Wed Jul 31 2024 Chris Roberts <chrobert@redhat.com> - 3.7.0-1
- Update to 3.7.0

* Mon Jul 15 2024 Chris Roberts <chrobert@redhat.com> - 3.6.7-1
- Update to 3.6.7

* Thu Apr 11 2024 Chris Roberts <chrobert@redhat.com> - 3.6.5-1
- Update to 3.6.5

* Mon Mar 04 2024 Chris Roberts <chrobert@redhat.com> - 3.6.4-1
- Update to 3.6.4

* Tue Jan 16 2024 Chris Roberts <chrobert@redhat.com> - 3.6.3-1
- Update to 3.6.3

* Sun Jul 02 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.6.2-1
- Update to 3.6.2

* Wed Jan 04 2023 Chris Roberts <chrobert@redhat.com> 3.6.0-1
- Update to 3.6.0

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.5.2-1
- Update to 3.5.2

* Mon May 16 2022 Chris Roberts <chrobert@redhat.com> 3.5.1-1
- Update to 3.5.1

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
