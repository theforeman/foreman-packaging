# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name get_process_mem
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.2.7
Release: 2%{?dist}
Summary: Use GetProcessMem to find out the amount of RAM used by any process
Group: Development/Languages
License: MIT
URL: https://github.com/schneems/get_process_mem
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(ffi) >= 1.0
Requires: %{?scl_prefix}rubygem(ffi) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Get memory usage of a process in Ruby .


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
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
%{gem_instdir}/get_process_mem.gemspec
%{gem_instdir}/test

%changelog
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

