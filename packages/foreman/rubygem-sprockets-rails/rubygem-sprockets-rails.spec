# template: default
%global gem_name sprockets-rails

Name: rubygem-%{gem_name}
Version: 3.5.2
Release: 1%{?dist}
Summary: Sprockets Rails integration
License: MIT
URL: https://github.com/rails/sprockets-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Sprockets Rails integration.


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
* Sun Aug 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.5.2-1
- Update to 3.5.2

* Wed Jun 12 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.5.1-1
- Update to 3.5.1

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.4.2-1
- Update to 3.4.2

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.2.1-7
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.1-6
- Bump to release for EL8

* Fri Feb 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.2.1-5
- Fix Obsoletes of tfm-ror52

* Mon Jan 20 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.1-3
- Update spec to remove the ror scl

* Wed Jan 15 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.2.1-2
- Revert sprockets rails back to using ROR SCL dependencies

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.2.1-1
- Initial package
