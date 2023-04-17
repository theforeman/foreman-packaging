# template: default
%global gem_name activerecord-nulldb-adapter

Name: rubygem-%{gem_name}
Version: 0.9.0
Release: 1%{?dist}
Summary: The Null Object pattern as applied to ActiveRecord database adapters
License: MIT
URL: https://github.com/nulldb/nulldb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A database backend that translates database interactions into no-ops. Using
NullDB enables you to test your model business logic - including after_save
hooks - without ever touching a real database.


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
%exclude %{gem_instdir}/Appraisals
%doc %{gem_instdir}/CHANGES.md
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/gemfiles
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/activerecord-nulldb-adapter.gemspec
%{gem_instdir}/spec

%changelog
* Mon Apr 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.9.0-1
- Update to 0.9.0

* Thu May 26 2022 Odilon Sousa <osousa@redhat.com> - 0.8.0-1
- Release rubygem-activerecord-nulldb-adapter 0.8.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.4.0-2
- Rebuild against rh-ruby27

* Sun Apr 19 2020 Eric D. Helms <ericdhelms@gmail.com> 0.4.0-1
- Add rubygem-activerecord-nulldb-adapter generated by gem2rpm using the scl template
