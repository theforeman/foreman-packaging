# template: default
%global gem_name rails-html-sanitizer

Name: rubygem-%{gem_name}
Version: 1.6.0
Release: 1%{?dist}
Summary: This gem is responsible to sanitize HTML fragments in Rails applications
License: MIT
URL: https://github.com/rails/rails-html-sanitizer
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7.0
BuildRequires: ruby >= 2.7.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
HTML sanitization for Rails applications.


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
%{gem_instdir}/test

%changelog
* Thu Jun 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.6.0-1
- Update to 1.6.0

* Sun Jan 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.5.0-1
- Update to 1.5.0

* Sun Jan 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.4.4-1
- Update to 1.4.4

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.4.3-1
- Update to 1.4.3

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.3.0-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.3.0-1
- Release rubygem-rails-html-sanitizer 1.3.0

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.4-5
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.4-4
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 1.0.4-3
- Bump for moving over to foreman-packaging

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.4-2
- rebuilt

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.4-1
- Initial package
