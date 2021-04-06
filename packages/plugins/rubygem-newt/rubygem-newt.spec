# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name newt
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.9.7
Release: 3%{?dist}
Summary: Ruby bindings for newt
Group: Development/Languages
License: MIT
URL: https://github.com/theforeman/ruby-newt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby-devel
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

Requires: newt
BuildRequires: newt-devel

%description
Ruby bindings for newt TUI library.


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

mkdir -p %{buildroot}%{gem_extdir_mri}/ruby_newt
cp -a .%{gem_instdir}/ext/ruby_newt/*.so %{buildroot}%{gem_extdir_mri}/ruby_newt/
touch %{buildroot}%{gem_extdir_mri}/gem.build_complete

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/{ext,tmp,.require_paths}

%check
%{?scl:scl enable %{scl} - << \EOF}
%if 0%{?rhel} == 8
# Workaround for: Ignoring newt-0.9.7 because its extensions are not built. Try: gem pristine newt --version 0.9.7
mkdir gem_ext_test
cp -a %{buildroot}%{gem_dir} gem_ext_test/
mkdir -p gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
cp -a %{buildroot}%{gem_extdir_mri} gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
GEM_PATH="./gem_ext_test/gems:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
rm -rf gem_ext_test
%else
echo "Checking with %{buildroot}%{gem_dir}"
GEM_PATH="%{buildroot}%{gem_dir}:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
%endif
%{?scl:EOF}

%files
%dir %{gem_instdir}
%exclude %{gem_libdir}/ruby_newt
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/examples

%changelog
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

