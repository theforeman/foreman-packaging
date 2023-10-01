# template: default
%global gem_name zeitwerk

Name: rubygem-%{gem_name}
Version: 2.6.12
Release: 1%{?dist}
Summary: Efficient and thread-safe constant autoloader
License: MIT
URL: https://github.com/fxn/zeitwerk
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Zeitwerk implements constant autoloading with Ruby semantics. Each gem
and application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading,
reloading, and eager loading.


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
* Sun Oct 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.6.12-1
- Update to 2.6.12

* Sun Aug 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.6.11-1
- Update to 2.6.11

* Sun Jul 30 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.6.9-1
- Update to 2.6.9

* Fri May 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.6.8-1
- Update to 2.6.8

* Sun Feb 12 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.6.7-1
- Update to 2.6.7

* Thu Nov 10 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.6.6-1
- Update to 2.6.6

* Thu Nov 03 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.6.4-1
- Update to 2.6.4

* Sun Oct 09 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.6.1-1
- Update to 2.6.1

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.6.0-1
- Update to 2.6.0

* Mon May 16 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.5.4-1
- Release rubygem-zeitwerk 2.5.4

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-2
- Rebuild against rh-ruby27

* Sun Jan 26 2020 Zach Huntington-Meath <zhunting@redhat.com> 2.2.2-1
- Add rubygem-zeitwerk generated by gem2rpm using the scl template
