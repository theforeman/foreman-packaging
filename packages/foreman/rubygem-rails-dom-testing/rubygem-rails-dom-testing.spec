# template: default
%global gem_name rails-dom-testing

Name: rubygem-%{gem_name}
Version: 2.3.0
Release: 1%{?dist}
Summary: Dom and Selector assertions for Rails applications
License: MIT
URL: https://github.com/rails/rails-dom-testing
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
This gem can compare doms and assert certain elements exists in doms using
Nokogiri. .


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
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%changelog
* Wed May 21 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.3.0-1
- Update to 2.3.0

* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.2.0-1
- Update to 2.2.0

* Sun Jul 09 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.1.1-1
- Update to 2.1.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.3-7
- Rebuild against rh-ruby27

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.3-6
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.3-5
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 2.0.3-4
- Bump for moving over to foreman-packaging

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.3-3
- rebuilt

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.3-2
- Fix activesupport version

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.3-1
- Initial package
