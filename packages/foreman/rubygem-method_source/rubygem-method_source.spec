# template: default
%global gem_name method_source

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 1%{?dist}
Summary: retrieve the sourcecode for a method
License: MIT
URL: https://banisterfiend.wordpress.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
retrieve the sourcecode for a method.


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
%exclude %{gem_instdir}/.circleci
%exclude %{gem_instdir}/.gemtest
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/method_source.gemspec
%{gem_instdir}/spec

%changelog
* Sun Apr 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.1.0-1
- Update to 1.1.0

* Tue Jul 26 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.0.0-1
- Update to 1.0.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.9.2-3
- Rebuild against rh-ruby27

* Thu Sep 17 2020 Patrick Creech <pcreech@redhat.com> - 0.9.2-2
- Add appropriate license, from https://github.com/banister/method_source/blob/master/LICENSE

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.9.2-1
- Release rubygem-method_source 0.9.2

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.9.0-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.9.0-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 0.9.0-2
- Bump for moving over to foreman-packaging

* Thu Jul 26 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.9.0-1
- Initial package
