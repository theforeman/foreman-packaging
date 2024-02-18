# template: default
%global gem_name ruby-libvirt
%global gem_require_name libvirt

Name: rubygem-%{gem_name}
Version: 0.8.2
Release: 1%{?dist}
Summary: Ruby bindings for LIBVIRT
License: LGPLv2+
URL: https://libvirt.org/ruby/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.8.1
BuildRequires: ruby-devel >= 1.8.1
BuildRequires: rubygems-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies

BuildRequires: libvirt-devel

%description
Ruby bindings for libvirt.


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

# remove shebangs from test files
find %{buildroot}%{gem_instdir}/tests -type f -name '*.rb' -print | xargs sed -i '/#!\/usr\/bin\/ruby/d'

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
%license %{gem_instdir}/COPYING
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/README
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/tests

%changelog
* Sun Feb 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.8.2-1
- Update to 0.8.2

* Wed Jul 27 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.8.0-1
- Update to 0.8.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.7.1-2
- Rebuild against rh-ruby27

* Tue Apr 21 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.7.1-1
- Update to 0.7.1-1

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.7.0-4
- Bump to release for EL8

* Thu Sep 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.7.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.7.0-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue May 16 2017 Dominic Cleal <dominic@cleal.org> 0.7.0-1
- Update ruby-libvirt to 0.7.0 (dominic@cleal.org)

* Thu Mar 03 2016 Dominic Cleal <dominic@cleal.org> 0.5.2-4
- Fix missing gem.build_complete file (#13948, dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.5.2-3
- Fix build errors and modernise specs (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.5.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Dec 05 2014 Dominic Cleal <dcleal@redhat.com> 0.5.2-1
- Update ruby-libvirt to 0.5.2 (dcleal@redhat.com)

* Mon Dec 16 2013 Dominic Cleal <dcleal@redhat.com> 0.5.1-1
- Update to ruby-libvirt 0.5.1 (dcleal@redhat.com)

* Fri Oct 04 2013 Sam Kottler <shk@redhat.com> 0.4.0-9
- Remove requires: libvirt (shk@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.0-4
- fix BR (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.0-3
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.0-1
- Initial package
