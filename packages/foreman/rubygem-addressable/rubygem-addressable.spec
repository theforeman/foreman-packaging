# template: default
%global gem_name addressable

Name: rubygem-%{gem_name}
Version: 2.8.7
Release: 1%{?dist}
Summary: URI Implementation
License: Apache-2.0
URL: https://github.com/sporkmonger/addressable
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.2
BuildRequires: ruby >= 2.2
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Addressable is an alternative implementation to the URI implementation that is
part of Ruby's standard library. It is flexible, offers heuristic parsing, and
additionally provides extensive support for IRIs and URI templates.


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
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/data
%{gem_libdir}
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%exclude %{gem_instdir}/addressable.gemspec

%changelog
* Sun Jul 07 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.8.7-1
- Update to 2.8.7

* Fri Jan 26 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.8.6-1
- Update to 2.8.6

* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.8.5-1
- Update to 2.8.5

* Mon Apr 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.8.4-1
- Update to 2.8.4

* Sun Sep 04 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.8.1-1
- Update to 2.8.1

* Thu Jul 08 2021 Eric D. Helms <ericdhelms@gmail.com> 2.8.0-1
- Update to 2.8.0-1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.6.0-3
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.6.0-2
- Bump to release for EL8

* Wed Mar 13 2019 kgaikwad <kavitagaikwad103@gmail.com> 2.6.0-1
- Update to 2.6.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.3.6-6
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.3.6-5
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Feb 09 2017 Dominic Cleal <dominic@cleal.org> 2.3.6-4
- Modernise spec file (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 2.3.6-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 2.3.6-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 2.3.6-1
- Update addressable to 2.3.6 (dcleal@redhat.com)

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 2.3.5-1
- Rebase to addressable 2.3.5 (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Fri Mar 29 2013 Marek Hulan <ares@igloonet.cz> 2.2.6-4
- fix for SCL

* Wed Mar 27 2013 Marek Hulan <ares@igloonet.cz> 2.2.6-3
- new package built with tito

* Mon Nov 05 2012 Miroslav Suchý <msuchy@redhat.com> 2.2.6-2
- add rubygem-addressable (msuchy@redhat.com)

* Wed Aug 10 2011 John Eckersberg <jeckersb@redhat.com> - 2.2.6-1
- Initial package
