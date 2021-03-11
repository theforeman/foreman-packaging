%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name patternfly-sass

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.59.4
Release: 2%{?dist}
Summary: Red Hat's Patternfly, converted to Sass and ready to drop into Rails
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/Patternfly/patternfly
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(bootstrap-sass) >= 3.4.0
Requires: %{?scl_prefix}rubygem(bootstrap-sass) < 3.5.0
Requires: %{?scl_prefix}rubygem(font-awesome-sass) >= 4.6.2
Requires: %{?scl_prefix}rubygem(font-awesome-sass) < 4.7.0
Requires: %{?scl_prefix}rubygem(sass) >= 3.4.15
Requires: %{?scl_prefix}rubygem(sass) < 3.5.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Red Hat's Patternfly, converted to Sass and ready to drop into Rails.


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
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/CODE_OF_CONDUCT.md
%license %{gem_instdir}/LICENSE.txt
%license %{gem_instdir}/OPEN_SOURCE_LICENCES.txt
%{gem_instdir}/QUICKSTART.md
%{gem_instdir}/dist
%{gem_libdir}
%exclude %{gem_instdir}/patternfly-sass.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.59.4-2
- Rebuild against rh-ruby27

* Thu Apr 23 2020 Ondřej Ezr <oezr@redhat.com> 3.59.4-1
- Update patternfly-sass to 3.59.4

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.37.0-4
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.37.0-3
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.37.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 16 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.37.0-1
- Bump rubygem-patternfly-sass to 3.37.0 (ewoud@kohlvanwijngaarden.nl)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.23.0-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Mar 23 2017 Dominic Cleal <dominic@cleal.org> 3.23.0-1
- Update patternfly-sass to 3.23.0 (dominic@cleal.org)

* Tue Jan 03 2017 Dominic Cleal <dominic@cleal.org> 3.15.0-1
- Update patternfly-sass to 3.15.0 (dominic@cleal.org)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 3.11.0-1
- Update patternfly-sass to 3.11.0 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 2.10.1-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 2.10.1-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Wed Feb 24 2016 Dominic Cleal <dominic@cleal.org> 2.10.1-1
- Update patternfly-sass to 2.10.1 (dominic@cleal.org)

* Thu Dec 31 2015 Daniel Lobato <elobatocs@gmail.com> 2.8.0-1
- Initial package
