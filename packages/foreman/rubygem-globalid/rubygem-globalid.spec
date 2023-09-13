# template: default
%global gem_name globalid

Name: rubygem-%{gem_name}
Version: 1.2.1
Release: 1%{?dist}
Summary: Refer to any model with a URI: gid://app/class/id
License: MIT
URL: https://www.rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
URIs for your models makes it easy to pass references around.


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

%changelog
* Wed Sep 13 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.2.1-1
- Update to 1.2.1

* Sun Jan 29 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.1.0-1
- Update to 1.1.0

* Sun Jan 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.0.1-1
- Update to 1.0.1

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.0.0-1
- Update to 1.0.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.4.2-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.4.2-1
- Release rubygem-globalid 0.4.2

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.4.1-6
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.4.1-5
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 0.4.1-4
- Bump for moving over to foreman-packaging

* Wed Aug 15 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.4.1-3
- Drop activesupport version lock

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.4.1-2
- rebuilt

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.4.1-1
- Initial package
