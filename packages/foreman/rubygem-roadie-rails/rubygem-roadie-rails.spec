# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name roadie-rails
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.3.0
Release: 1%{?dist}
Summary: Making HTML emails comfortable for the Rails rockstars
Group: Development/Languages
License: MIT
URL: https://github.com/Mange/roadie-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.5
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(railties) >= 5.1
Requires: %{?scl_prefix}rubygem(railties) < 7.1
Requires: %{?scl_prefix}rubygem(roadie) >= 3.1
Requires: %{?scl_prefix}rubygem(roadie) < 5.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.5
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Hooks Roadie into your Rails application to help with email generation.


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
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/Upgrading.md
%{gem_instdir}/codecov.yml
%{gem_libdir}
%{gem_instdir}/setup.sh
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/roadie-rails.gemspec

%changelog
* Tue May 24 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-1
- Release rubygem-roadie-rails 2.3.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.1.1-3
- Rebuild against rh-ruby27

* Thu Apr 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 2.1.1-2
- Update requirements for a newer railties

* Thu Apr 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 2.1.1-1
- Update to 2.1.1

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.0-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.0-2
- Update spec to remove the ror scl

* Fri Feb 15 2019 Michael Moll <mmoll@mmoll.at> - 2.0.0-1
- Bump rubygem-roadie-rails to 2.0.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.3.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Aug 15 2018 Eric D. Helms <ericdhelms@gmail.com> 1.3.0-1
- Bump to 1.3.0

* Thu Jan 04 2018 Eric D. Helms <ericdhelms@gmail.com> 1.2.1-1
- Bump roadie-rails to 1.2.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Thu Jun 02 2016 Dominic Cleal <dominic@cleal.org> 1.1.1-1
- new package built with tito
