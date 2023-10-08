# template: default
%global gem_name audited

Name: rubygem-%{gem_name}
Version: 5.4.0
Release: 1%{?dist}
Summary: Log all changes to your models
License: MIT
URL: https://github.com/collectiveidea/audited
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3.0
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Log all changes to your models.


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
%exclude %{gem_instdir}/.standard.yml
%exclude %{gem_instdir}/.yardopts
%exclude %{gem_instdir}/Appraisals
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/gemfiles
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/test

%changelog
* Sun Oct 08 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.4.0-1
- Update to 5.4.0

* Thu May 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.3.3-1
- Update to 5.3.3

* Thu Feb 23 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.3.2-1
- Update to 5.3.2

* Wed Feb 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.3.1-1
- Update to 5.3.1

* Sun Feb 19 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.3.0-1
- Update to 5.3.0

* Thu Jan 26 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.2.0-1
- Update to 5.2.0

* Wed Aug 24 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.0.2-1
- Update to 5.0.2

* Tue May 24 2022 Eric D. Helms <ericdhelms@gmail.com> - 4.10.0-1
- Release rubygem-audited 4.10.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.9.0-4
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.9.0-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.9.0-2
- Update spec to remove the ror scl

* Wed Aug 28 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.9.0-1
- Update to 4.9.0-1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 4.7.1-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon Jun 04 2018 Michael Moll <mmoll@mmoll.at> 4.7.1-1
- Update to 4.7.1

* Tue Mar 27 2018 Tomer Brisker <tbrisker@gmail.com> 4.7.0-1
- Update to 4.7.0

* Tue Jan 16 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.6.0-1
- Bump rubygem-audited to 4.6.0 (ewoud@kohlvanwijngaarden.nl)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.4.1-2
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Mar 30 2017 Dominic Cleal <dominic@cleal.org> 4.4.1-1
- Update audited to 4.4.1 (dominic@cleal.org)

* Tue Jan 24 2017 Dominic Cleal <dominic@cleal.org> 4.3.0-1
- Update audited to 4.3.0 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 4.2.0-1
- Update audited to 4.2.0 (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 3.0.0-4
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 3.0.0-2
- new package built with tito

* Tue Nov 27 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.0-1
- Initial package
