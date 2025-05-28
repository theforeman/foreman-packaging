# template: default
%global gem_name get_process_mem

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 1%{?dist}
Summary: Use GetProcessMem to find out the amount of RAM used by any process
License: MIT
URL: https://github.com/schneems/get_process_mem
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6
BuildRequires: ruby >= 2.6
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Get memory usage of a process in Ruby .


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
%exclude %{gem_instdir}/.standard.yml
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/appveyor.yml
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/get_process_mem.gemspec
%{gem_instdir}/test

%changelog
* Fri Jul 26 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.0.0-1
- Update to 1.0.0

* Mon Apr 05 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.2.7-2
- Rebuild Ruby 2.7

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> 0.2.7-1
- Update to 0.2.7-1

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.2.1-4
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.2.1-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.2.1-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Mon Jun 19 2017 Eric D. Helms <ericdhelms@gmail.com> 0.2.1-1
- new package built with tito

