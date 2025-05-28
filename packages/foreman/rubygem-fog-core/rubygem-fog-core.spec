# template: default
%global gem_name fog-core

Name: rubygem-%{gem_name}
Version: 2.6.0
Release: 1%{?dist}
Summary: Shared classes and tests for fog providers and services
License: MIT
URL: https://github.com/fog/fog-core
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.0
BuildRequires: ruby >= 2.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Shared classes and tests for fog providers and services.


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
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/SECURITY.md
%exclude %{gem_instdir}/fog-core.gemspec
%doc %{gem_instdir}/changelog.md

%changelog
* Tue Mar 18 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.6.0-1
- Update to 2.6.0

* Mon Jan 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.4.0-1
- Update to 2.4.0

* Sun Nov 06 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.3.0-1
- Update to 2.3.0

* Wed Jul 13 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.2.4-1
- Update to 2.2.4

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-4
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.1.0-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.1.0-2
- Update spec to remove the ror scl

* Thu Feb 21 2019 Marek Hulan <mhulan@redhat.com> 2.1.0-1
- Update to 2.1.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.45.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.45.0-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Aug 24 2017 Eric D. Helms <ericdhelms@gmail.com> 1.45.0-1
- Update fog-core to 1.45.0 (me@daniellobato.me)

* Mon May 22 2017 Dominic Cleal <dominic@cleal.org> 1.44.2-1
- Update fog-core to 1.44.2 (dominic@cleal.org)

* Tue Jul 19 2016 Dominic Cleal <dominic@cleal.org> 1.42.0-1
- Update fog-core to 1.42.0 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.36.0-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Mar 31 2016 Dominic Cleal <dominic@cleal.org> 1.36.0-1
- Update fog-core to 1.36.0 (dominic@cleal.org)

* Tue Jan 19 2016 Dominic Cleal <dcleal@redhat.com> 1.35.0-1
- Update fog-core to 1.35.0 (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.34.0-2
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Fri Nov 20 2015 Dominic Cleal <dcleal@redhat.com> 1.34.0-1
- Update fog-core to 1.34.0 (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.32.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Aug 18 2015 Dominic Cleal <dcleal@redhat.com> 1.32.1-1
- Update fog-core to 1.32.1 (dcleal@redhat.com)

* Fri Jul 03 2015 Dominic Cleal <dcleal@redhat.com> 1.32.0-1
- Update fog-core to 1.32.0 (dcleal@redhat.com)
- Fixes #9703 - change %%{dist} to %%{?dist} (jmontleo@redhat.com)

* Sun Feb 22 2015 Daniel Lobato <dlobatog@redhat.com> 1.29.0-1
- Update fog-core to 1.29.0 (dlobatog@redhat.com)

* Tue Feb 17 2015 Dominic Cleal <dcleal@redhat.com> 1.27.4-1
- Update fog-core to 1.27.4 (dcleal@redhat.com)

* Wed Nov 26 2014 Dominic Cleal <dcleal@redhat.com> 1.25.0-1
- Update fog-core to 1.25.0 (dcleal@redhat.com)

* Mon Oct 13 2014 Dominic Cleal <dcleal@redhat.com> 1.24.0-1
- refs #7879 - update fog to v1.24.0 (dcleal@redhat.com)

* Tue Jul 22 2014 Dominic Cleal <dcleal@redhat.com> 1.23.0-1
- Update to v1.23.0 (dcleal@redhat.com)

* Tue Mar 25 2014 Dominic Cleal <dcleal@redhat.com> 1.21.1-2
- Fix Provides for correct gem name (dcleal@redhat.com)

* Wed Mar 19 2014 Dominic Cleal <dcleal@redhat.com> 1.21.1-1
- new package built with tito
