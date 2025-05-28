# template: default
%global gem_name autoprefixer-rails

Name: rubygem-%{gem_name}
Version: 10.4.21.0
Release: 1%{?dist}
Summary: Parse CSS and add vendor prefixes to CSS rules using values from the Can I Use website
License: MIT
URL: https://github.com/ai/autoprefixer-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.4
BuildRequires: ruby >= 2.4
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Parse CSS and add vendor prefixes to CSS rules using values from the Can I Use
website.


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
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Apr 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 10.4.21.0-1
- Update to 10.4.21.0

* Sun Aug 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 10.4.19.0-1
- Update to 10.4.19.0

* Sun Dec 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 10.4.16.0-1
- Update to 10.4.16.0

* Wed Sep 13 2023 Foreman Packaging Automation <packaging@theforeman.org> 10.4.15.0-1
- Update to 10.4.15.0

* Mon Mar 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 10.4.13.0-1
- Update to 10.4.13.0

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 10.4.7.0-1
- Update to 10.4.7.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 5.2.1.3-7
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.1.3-6
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.1.3-5
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.1.3-4
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.2.1.3-3
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 5.2.1.3-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Jan 05 2016 Daniel Lobato <elobatocs@gmail.com> 5.2.1.3-1
- Initial package
