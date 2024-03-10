# template: default
%global gem_name marcel

Name: rubygem-%{gem_name}
Version: 1.0.4
Release: 1%{?dist}
Summary: Simple mime type detection using magic numbers, filenames, and extensions
License: MIT and Apache-2.0
URL: https://github.com/rails/marcel
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3
BuildRequires: ruby >= 2.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Simple mime type detection using magic numbers, filenames, and extensions.


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
%license %{gem_instdir}/APACHE-LICENSE
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Sun Mar 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.0.4-1
- Update to 1.0.4

* Wed Jul 06 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.2-1
- Update to 1.0.2

* Tue May 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-1
- Release 1.0.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.3.3-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.3.3-1
- Release rubygem-marcel 0.3.3

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.3.2-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.3.2-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 0.3.2-2
- Bump for moving over to foreman-packaging

* Mon Aug 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.3.2-1
- Initial package
