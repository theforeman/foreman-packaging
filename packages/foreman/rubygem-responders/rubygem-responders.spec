# template: default
%global gem_name responders

Name: rubygem-%{gem_name}
Version: 3.1.1
Release: 1%{?dist}
Summary: A set of Rails responders to dry up your application
License: MIT
URL: https://github.com/heartcombo/responders
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A set of Rails responders to dry up your application.


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
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Sun Oct 15 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.1.1-1
- Update to 3.1.1

* Sun Feb 12 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.1.0-1
- Update to 3.1.0

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.0.1-1
- Update to 3.0.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.0.0-4
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.0-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.0-2
- Update spec to remove the ror scl

* Thu Oct 03 2019 Michael Moll <mmoll@mmoll.at> - 3.0.0-1
- Update responders to 3.0.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.4.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Jan 04 2018 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-1
- Bump rubygem-responders to 2.4.0 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Aug 17 2016 Dominic Cleal <dominic@cleal.org> 2.3.0-1
- Update responders to 2.3.0 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 2.1.1-1
- new package built with tito

