# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name unicode
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.4.4
Release: 4%{?dist}
Summary: Unicode normalization library
Group: Development/Languages
License: Ruby
URL: http://www.yoshidam.net/Ruby.html#unicode
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://www.ruby-lang.org/en/about/license.txt

# This is a C extension linked against MRI, it's not compatible with other
# interpreters. So we require MRI specifically instead of ruby(release).
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby-devel
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Unicode normalization library.


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
cp -p %{SOURCE1} .
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

mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}

%check
%{?scl:scl enable %{scl} - << \EOF}
# Ideally, this would be something like this:
# GEM_PATH="%{buildroot}%{gem_dir}:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
# But that fails to find native extensions on EL8, so we fake the structure that ruby expects
mkdir gem_ext_test
cp -a %{buildroot}%{gem_dir} gem_ext_test/
mkdir -p gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
cp -a %{buildroot}%{gem_extdir_mri} gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
GEM_PATH="./gem_ext_test/gems:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
rm -rf gem_ext_test
%{?scl:EOF}

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/ext
%{gem_extdir_mri}
%{gem_libdir}
%{gem_instdir}/tools
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/unicode.gemspec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.4.4.4-4
- Rebuild against rh-ruby27

* Thu Apr 16 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.4.4.4-3
- Add check section to test native library

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.4.4.4-2
- Bump to release for EL8

* Tue Sep 24 2019 Eric D. Helms <ericdhelms@gmail.com> 0.4.4.4-1
- Update to 0.4.4.4-1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.4.4.1-5
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.4.4.1-4
- Final set of rebuilds (ericdhelms@gmail.com)

* Wed Sep 27 2017 Eric D. Helms <ericdhelms@gmail.com> 0.4.4.1-3
- rubygem-unicode: Fix provides & native extensions
  (ewoud@kohlvanwijngaarden.nl)

* Tue Sep 26 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.4.4.1-2
- new package built with tito

* Mon Jul 14 2014 Dan Callaghan <dcallagh@redhat.com> - 0.4.4.1-2
- run test program in %%check
- use HTTPS for Ruby license source URL

* Thu Jun 05 2014 Dan Callaghan <dcallagh@redhat.com> - 0.4.4.1-1
- updated to upstream release 0.4.4.1
- fixed spec for rubygem changes in F21+

* Tue Jan 28 2014 Dan Callaghan <dcallagh@redhat.com> - 0.4.4-1
- Initial package
