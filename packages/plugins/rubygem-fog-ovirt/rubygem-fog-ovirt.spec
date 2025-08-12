# template: default
%global gem_name fog-ovirt

Name: rubygem-%{gem_name}
Version: 2.0.3
Release: 2%{?dist}
Summary: Module for the 'fog' gem to support Ovirt
License: MIT
URL: https://github.com/fog/fog-ovirt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.0.0
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
This library can be used as a module for `fog`.


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

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Tue Aug 12 2025 Evgeni Golov - 2.0.3-2
- Rebuild for plugins

* Wed Oct 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.0.3-1
- Update to 2.0.3

* Tue Jun 07 2022 Ron Lavi <1ronlavi@gmail.com> 2.0.2-1
- Update to 2.0.2

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.1-2
- Rebuild against rh-ruby27

* Wed Jan 20 2021 Shira Maximov <shiramaximov@gmail.com> 2.0.1-1
- Update to 2.0.1

* Tue Dec 22 2020 Evgeni Golov 2.0.0-1
- Update to 2.0.0-1

* Tue May 26 2020 Shira Maximov <shiramaximov@gmail.com> 1.2.5-1
- Update to 1.2.5

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.2.4-2
- Bump to release for EL8

* Tue Dec 17 2019 Shira Maximov <shiramaximov@gmail.com> 1.2.4-1
- Update to 1.2.4

* Sun Dec 01 2019 Shira Maximov <shiramaximov@gmail.com> 1.2.3-1
- Update to 1.2.3

* Sun Nov 10 2019 Shira Maximov <shiramaximov@gmail.com> 1.2.2-1
- Update to 1.2.2

* Wed May 22 2019 Shira Maximov <shiramaximov@gmail.com> 1.2.0-1
- Update to 1.2.0

* Wed Feb 06 2019 Ori Rabin <orabin@redhat.com> 1.1.5-1
- Update to 1.1.5

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.1.2-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Aug 30 2018 Ori Rabin <orrabin@gmail.com> 1.1.2-1
- Update to 1.1.2

* Thu Jul 12 2018 Ivan Nečas <inecas@redhat.com> 1.1.1-1
- Update to 1.1.1

* Thu Jun 14 2018 Ori Rabin <orrabin@gmail.com> 1.0.4-1
- Update to 1.0.4

* Wed Apr 11 2018 Ori Rabin <orabin@redhat.com> 1.0.3-1
- Update to 1.0.3

* Thu Apr 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.2-1
- Update to 1.0.2

* Tue Apr 03 2018 Michael Moll <mmoll@mmoll.at> 1.0.1-1
- Update fog-ovirt to 1.0.1

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.2-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)

* Wed Dec 13 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.1.2-1
- new package built with tito

