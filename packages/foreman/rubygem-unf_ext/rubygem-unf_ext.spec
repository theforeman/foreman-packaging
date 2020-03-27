# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name unf_ext

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.7.6
Release: 1%{?dist}
Summary: Unicode Normalization Form support library for CRuby
Group: Development/Languages
License: MIT
URL: https://github.com/knu/ruby-unf_ext
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

%description
Unicode Normalization Form support library for CRuby.


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

mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
%{?scl:scl enable %{scl} - << \EOF}
GEM_PATH="%{buildroot}%{gem_dir}:$GEM_PATH" ruby -e "require '%{gem_name}'"
%{?scl:EOF}

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
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
%{gem_instdir}/unf_ext.gemspec

%changelog
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
