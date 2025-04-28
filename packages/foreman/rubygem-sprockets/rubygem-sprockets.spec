# template: default
%global gem_name sprockets

Name: rubygem-%{gem_name}
Version: 4.2.2
Release: 1%{?dist}
Summary: Rack-based asset packaging system
License: MIT
URL: https://github.com/rails/sprockets
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

Requires: (rubygem(logger) or ruby-default-gems < 3.5)

%description
Sprockets is a Rack-based asset packaging system that concatenates and serves
JavaScript, CoffeeScript, CSS, Sass, and SCSS.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%gemspec_remove_dep -g logger

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

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/sprockets
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Sun Apr 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.2.2-1
- Update to 4.2.2

* Wed Sep 13 2023 Foreman Packaging Automation <packaging@theforeman.org> 4.2.1-1
- Update to 4.2.1

* Sun Jan 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 4.2.0-1
- Update to 4.2.0

* Fri Jul 01 2022 Eric D. Helms <ericdhelms@gmail.com> - 4.1.1-1
- Release rubygem-sprockets 4.1.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.0.2-2
- Rebuild against rh-ruby27

* Mon Jun 15 2020 Michael Moll <mmoll@mmoll.at> - 4.0.2-1
- Release rubygem-sprockets 4.0.2

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.7.2-6
- Bump packages to build for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.7.2-5
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 3.7.2-4
- Bump for moving over to foreman-packaging

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.7.2-3
- rebuilt

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.7.2-2
- Add missing gem_docdir

* Wed Aug 08 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.7.2-1
- Initial package
