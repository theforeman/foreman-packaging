# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name jquery-ui-rails

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 6.0.1
Release: 2%{?dist}
Summary: jQuery UI packaged for the Rails asset pipeline
Group: Development/Languages
License: MIT
URL: https://github.com/joliss/jquery-ui-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems) >= 1.3.6
Requires: %{?scl_prefix}rubygem(railties) >= 3.2.16
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 1.3.6
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
jQuery UI's JavaScript, CSS, and image files packaged for the Rails 3.1+ asset
pipeline.


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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.gitmodules
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/License.txt
%{gem_instdir}/app
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/VERSIONS.md
%{gem_instdir}/Rakefile

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 6.0.1-2
- Rebuild against rh-ruby27

* Tue Apr 14 2020 Ondřej Ezr <oezr@redhat.com> 6.0.1-1
- Update to 6.0.1-1

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.1.2-9
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.1.2-8
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 4.1.2-7
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.1.2-6
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri May 27 2016 Dominic Cleal <dominic@cleal.org> 4.1.2-5
- Rebuild and modernise for F24 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 4.1.2-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 4.1.2-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 4.1.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Nov 18 2014 Dominic Cleal <dcleal@redhat.com> 4.1.2-1
- Update jquery-ui-rails to 4.1.2 (dcleal@redhat.com)

* Thu Jun 27 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-7
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-5
- fix files section (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-4
- fix files section (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-3
- new package built with tito

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-2
- new package built with tito

* Thu Mar 28 2013 msuchy@redhat.com - 4.0.2-1
- Initial package
