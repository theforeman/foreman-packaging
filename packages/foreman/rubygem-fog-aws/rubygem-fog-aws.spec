# template: default
%global gem_name fog-aws

Name: rubygem-%{gem_name}
Version: 3.33.0
Release: 1%{?dist}
Summary: Module for the 'fog' gem to support Amazon Web Services
License: MIT
URL: https://github.com/fog/fog-aws
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.0.0
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

Requires: (rubygem(base64) or ruby-default-gems < 3.4)

%description
This library can be used as a module for `fog` or as standalone provider
to use the Amazon Web Services in applications..


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%gemspec_remove_dep -g base64

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
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/fog-aws.gemspec

%changelog
* Sun Aug 10 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.33.0-1
- Update to 3.33.0

* Wed May 28 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.32.0-1
- Update to 3.32.0

* Wed Apr 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.31.0-1
- Update to 3.31.0

* Tue Mar 18 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.30.0-1
- Update to 3.30.0

* Sun Jul 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.24.0-1
- Update to 3.24.0

* Fri Jun 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.23.0-1
- Update to 3.23.0

* Tue Mar 19 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.22.0-1
- Update to 3.22.0

* Mon Mar 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.21.1-1
- Update to 3.21.1

* Sun Oct 08 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.21.0-1
- Update to 3.21.0

* Sun Oct 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.20.0-1
- Update to 3.20.0

* Sun May 21 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.19.0-1
- Update to 3.19.0

* Wed Feb 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.18.0-1
- Update to 3.18.0

* Sun Feb 12 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.17.0-1
- Update to 3.17.0

* Sun Jan 29 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.16.0-1
- Update to 3.16.0

* Sun Oct 02 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.15.0-1
- Update to 3.15.0

* Fri Jul 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.14.0-1
- Update to 3.14.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.6.5-2
- Rebuild against rh-ruby27

* Wed May 27 2020 Aditi Puntambekar <apuntamb@redhat.com> 3.6.5-1
- Update to 3.6.5

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.5.0-2
- Bump to release for EL8

* Thu May 02 2019 Marek Hulan <mhulan@redhat.com> 3.5.0-1
- Update to 3.5.0

* Thu Mar 21 2019 Marek Hulan <mhulan@redhat.com> 3.4.0-1
- Update to 3.4.0

* Thu Feb 21 2019 Marek Hulan <mhulan@redhat.com> 3.3.0-1
- Update to 3.3.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.3.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.0-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri Mar 31 2017 Dominic Cleal <dominic@cleal.org> 1.3.0-1
- Update fog-aws to 1.3.0 (dominic@cleal.org)

* Tue Jan 24 2017 Dominic Cleal <dominic@cleal.org> 1.2.0-1
- Update fog-aws to 1.2.0 (dominic@cleal.org)

* Thu Dec 22 2016 Dominic Cleal <dominic@cleal.org> 0.13.0-1
- Update fog-aws to 0.13.0 (#17781, kvedulv@kvedulv.de)

* Tue Jul 19 2016 Dominic Cleal <dominic@cleal.org> 0.10.0-1
- Update fog-aws to 0.10.0 (dominic@cleal.org)

* Wed Mar 09 2016 Dominic Cleal <dominic@cleal.org> 0.9.1-1
- Update fog-aws to 0.9.1 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.7.4-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.7.4-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Aug 12 2015 Dominic Cleal <dcleal@redhat.com> 0.7.4-1
- Update fog-aws to 0.7.4 (dcleal@redhat.com)

* Wed Jul 08 2015 Dominic Cleal <dcleal@redhat.com> 0.7.0-1
- Update fog-aws to 0.7.0 (dcleal@redhat.com)

* Fri Jul 03 2015 Dominic Cleal <dcleal@redhat.com> 0.6.0-1
- Update fog-aws to 0.6.0 (dcleal@redhat.com)

* Tue Jun 23 2015 Dominic Cleal <dcleal@redhat.com> 0.5.0-1
- Update fog-aws to 0.5.0 (dcleal@redhat.com)

* Mon Jun 01 2015 Dominic Cleal <dcleal@redhat.com> 0.4.0-1
- Update fog-aws to 0.4.0 (dcleal@redhat.com)
- Fixes #9703 - change %%{dist} to %%{?dist} (jmontleo@redhat.com)

* Sun Feb 22 2015 Daniel Lobato <dlobatog@redhat.com> 0.1.0-1
- Update fog-aws to version 0.1.0

* Tue Feb 17 2015 Dominic Cleal <dcleal@redhat.com> 0.0.8-1
- new package built with tito
