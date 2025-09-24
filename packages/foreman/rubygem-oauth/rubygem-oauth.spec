# template: default
%global gem_name oauth

Name: rubygem-%{gem_name}
Version: 1.1.2
Release: 1%{?dist}
Summary: OAuth Core Ruby implementation
License: MIT
URL: https://github.com/oauth-xx/oauth-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3
BuildRequires: ruby >= 2.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
OAuth Core Ruby implementation.


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
%exclude %{gem_instdir}/CODE_OF_CONDUCT.md
%exclude %{gem_instdir}/CITATION.cff
%exclude %{gem_instdir}/FUNDING.md
%exclude %{gem_instdir}/REEK
%exclude %{gem_instdir}/RUBOCOP.md
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/SECURITY.md

%changelog
* Wed Sep 24 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.1.2-1
- Update to 1.1.2

* Mon Oct 31 2022 Eric D. Helms <ericdhelms@gmail.com> 1.1.0-1
- Update to 1.1.0-1

* Thu Aug 25 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.0-1
- Update to 1.0.0

* Fri Jul 22 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.5.10-1
- Update to 0.5.10

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.5.4-5
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.5.4-4
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.5.4-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.5.4-2
- Final set of rebuilds (ericdhelms@gmail.com)

* Mon Dec 11 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.5.4-1
- Update oauth to 0.5.4 (oprazak@redhat.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Feb 09 2017 Dominic Cleal <dominic@cleal.org> 0.5.1-1
- Update oauth to 0.5.1 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.4.7-8
- Fix build errors and modernise specs (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.4.7-7
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 0.4.7-6
- Modernise and update for EL7 (dcleal@redhat.com)

* Wed Jul 03 2013 Lukas Zapletal <lzap+git@redhat.com> 0.4.7-5
- rubygem-oauth works for non-SCL as well (lzap+git@redhat.com)
- remove empty tito.props and definition which are duplicate with default from
  rel-eng/tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.7-3
- new package built with tito

* Thu Nov 08 2012 Miroslav Suchý <msuchy@redhat.com> 0.4.7-2
- fixing requires and buildrequires for F17 (msuchy@redhat.com)

* Tue Nov 06 2012 Ivan Necas <inecas@redhat.com> 0.4.7-1
- rebase so 0.4.7

* Fri Jan 14 2011 Shannon Hughes <shughes@redhat.com> 0.4.4-1
- new package built with tito

* Fri Jan 14 2011 Shannon Hughes <shughes@redhat.com> - 0.4.4-1
- Initial package
