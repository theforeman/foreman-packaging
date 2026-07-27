# template: default
%global gem_name crass

Name: rubygem-%{gem_name}
Version: 1.0.7
Release: 2%{?dist}
Summary: CSS parser based on the CSS Syntax Level 3 spec
License: MIT
URL: https://github.com/rgrove/crass/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.9.2
BuildRequires: ruby >= 1.9.2
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Crass is a pure Ruby CSS parser based on the CSS Syntax Level 3 spec.


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
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/crass.gemspec

%changelog
* Mon Jul 27 2026 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.7-2
- Rebuild for EL10

* Mon Jun 29 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1.0.7-1
- Update to 1.0.7

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.6-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.6-1
- Release rubygem-crass 1.0.6

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.4-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.4-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 1.0.4-2
- Bump for moving over to foreman-packaging

* Thu Jul 26 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.4-1
- Initial package
