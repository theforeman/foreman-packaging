# template: default
%global gem_name unf_ext
%global gem_require_name %{gem_name}

Name: rubygem-%{gem_name}
Version: 0.0.8.2
Release: 1%{?dist}
Summary: Unicode Normalization Form support library for CRuby
License: MIT
URL: https://github.com/knu/ruby-unf_ext
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.2
BuildRequires: ruby-devel >= 2.2
BuildRequires: rubygems-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies

%description
Unicode Normalization Form support library for CRuby.


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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
# Ideally, this would be something like this:
# GEM_PATH="%{buildroot}%{gem_dir}:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
# But that fails to find native extensions on EL8, so we fake the structure that ruby expects
mkdir gem_ext_test
cp -a %{buildroot}%{gem_dir} gem_ext_test/
mkdir -p gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
cp -a %{buildroot}%{gem_extdir_mri} gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
GEM_PATH="./gem_ext_test/gems:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
rm -rf gem_ext_test

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.document
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%exclude %{gem_instdir}/unf_ext.gemspec

%changelog
* Wed Jul 27 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.8.2-1
- Update to 0.0.8.2

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.7.2-4
- Rebuild against rh-ruby27

* Mon Apr 20 2020 Evgeni Golov 0.0.7.2-3
* Revert to 0.0.7.2 as that's what ms_rest_azure requires

* Wed Apr 15 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.7.6-1
- Update to 0.0.7.6-1

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.0.7.2-2
- Bump to release for EL8

* Fri Oct 18 2019 Aditi Puntambekar <apuntamb@redhat.com> 0.0.7.2-1
- Update to 0.0.7.2

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.0.6-8
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.6-7
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed May 25 2016 Dominic Cleal <dominic@cleal.org> 0.0.6-6
- Re-introduce unf_ext, modernise spec (dominic@cleal.org)
- Add full rubygems.org source URL (dcleal@redhat.com)

* Fri May 30 2014 Dominic Cleal <dcleal@redhat.com> 0.0.6-5
- Modernise spec for EL7 (dcleal@redhat.com)

* Tue Nov 12 2013 Sam Kottler <shk@redhat.com> 0.0.6-4
- Actually fix the rubygems-devel issue (shk@redhat.com)

* Tue Nov 12 2013 Sam Kottler <shk@redhat.com> 0.0.6-3
- Make sure rubygems-devel is required during build for SCL (shk@redhat.com)

* Tue Nov 12 2013 Sam Kottler <shk@redhat.com> 0.0.6-2
- Initial build with support for SCL

* Tue Nov 12 2013 Sam Kottler <skottler@redhat.com> - 0.0.6-1
- Initial package
