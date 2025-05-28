# template: default
%global gem_name activerecord-import

Name: rubygem-%{gem_name}
Version: 2.2.0
Release: 1%{?dist}
Summary: Bulk insert extension for ActiveRecord
License: MIT
URL: https://github.com/zdennis/activerecord-import
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.4.0
BuildRequires: ruby >= 2.4.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A library for bulk inserting data using ActiveRecord.


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
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%{gem_instdir}/Brewfile
%exclude %{gem_instdir}/Dockerfile
%exclude %{gem_instdir}/docker-compose.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/benchmarks
%exclude %{gem_instdir}/gemfiles
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/activerecord-import.gemspec
%{gem_instdir}/test

%changelog
* Wed May 28 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.2.0-1
- Update to 2.2.0

* Wed Feb 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.1.0-1
- Update to 2.1.0

* Wed Dec 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.0.0-1
- Update to 2.0.0

* Sun Sep 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.8.1-1
- Update to 1.8.1

* Wed Aug 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.8.0-1
- Update to 1.8.0

* Sun May 26 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.7.0-1
- Update to 1.7.0

* Tue Mar 19 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.6.0-1
- Update to 1.6.0

* Sun Dec 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.5.1-1
- Update to 1.5.1

* Sun Sep 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.5.0-1
- Update to 1.5.0

* Sun Oct 16 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.4.1-1
- Update to 1.4.1

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.4.0-1
- Update to 1.4.0

* Wed Jun 16 2021 Odilon Sousa <osousa@redhat.com> - 1.1.0-1
- Release rubygem-activerecord-import 1.1.0

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.0-3
- Rebuild for Ruby 2.7

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.0-2
- Update spec to remove the ror scl

* Mon Feb 04 2019 Justin Sherrill <jlsherrill@redhat.com> - 1.0.0-1
- Initial package

