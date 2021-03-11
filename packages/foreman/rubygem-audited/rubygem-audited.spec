# Generated from audited-4.9.0.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name audited

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.9.0
Release: 4%{?dist}
Summary: Log all changes to your models
Group: Development/Languages
License: MIT
URL: https://github.com/collectiveidea/audited
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.3.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(activerecord) >= 4.2
Requires: %{?scl_prefix}rubygem(activerecord) < 6.1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.3.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Log all changes to your models.


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
%{gem_libdir}
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Appraisals
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/gemfiles
%{gem_instdir}/spec
%{gem_instdir}/test

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.9.0-4
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.9.0-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.9.0-2
- Update spec to remove the ror scl

* Wed Aug 28 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.9.0-1
- Update to 4.9.0-1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 4.7.1-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon Jun 04 2018 Michael Moll <mmoll@mmoll.at> 4.7.1-1
- Update to 4.7.1

* Tue Mar 27 2018 Tomer Brisker <tbrisker@gmail.com> 4.7.0-1
- Update to 4.7.0

* Tue Jan 16 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.6.0-1
- Bump rubygem-audited to 4.6.0 (ewoud@kohlvanwijngaarden.nl)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.4.1-2
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Mar 30 2017 Dominic Cleal <dominic@cleal.org> 4.4.1-1
- Update audited to 4.4.1 (dominic@cleal.org)

* Tue Jan 24 2017 Dominic Cleal <dominic@cleal.org> 4.3.0-1
- Update audited to 4.3.0 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 4.2.0-1
- Update audited to 4.2.0 (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 3.0.0-4
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 3.0.0-2
- new package built with tito

* Tue Nov 27 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.0-1
- Initial package
