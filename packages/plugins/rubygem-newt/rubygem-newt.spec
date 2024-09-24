# template: default
%global gem_name newt
%global gem_require_name %{gem_name}

Name: rubygem-%{gem_name}
Version: 1.0.1
Release: 1%{?dist}
Summary: Ruby bindings for newt
License: MIT
URL: https://github.com/theforeman/ruby-newt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby-devel
BuildRequires: rubygems-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies
BuildRequires: newt-devel

%description
Ruby bindings for newt TUI library.


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

mkdir -p %{buildroot}%{gem_extdir_mri}/ruby_newt
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_instdir}/ext/ruby_newt/*.so %{buildroot}%{gem_extdir_mri}/ruby_newt/

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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/examples

%changelog
* Tue Sep 24 2024 Leos Stejskal <lstejska@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.9.7-3
- Rebuild for Ruby 2.7

* Fri Aug 21 2020 Lukas Zapletal <lzap+rpm@redhat.com> 0.9.7-2
- Release bump - moved into SCL for EL7

* Fri Mar 27 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.9.7-1
- Update to 0.9.7-1
- Regenerate spec file

* Tue May 31 2016 Dominic Cleal <dominic@cleal.org> 0.9.6-3
- Replace gem install with macro (dominic@cleal.org)

* Tue Jan 05 2016 Dominic Cleal <dcleal@redhat.com> 0.9.6-2
- Retrieve .so from ext/ rather than lib/ for F21 compatibility
  (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.9.6-1
- Updated rubygem-newt to 0.9.6 (lzap+git@redhat.com)

* Tue Aug 04 2015 Lukas Zapletal <lzap+rpm@redhat.com> 0.9.5-1
- bumped version

* Tue Jun 30 2015 Dominic Cleal <dcleal@redhat.com> 0.9.4-1
- new package built with tito
