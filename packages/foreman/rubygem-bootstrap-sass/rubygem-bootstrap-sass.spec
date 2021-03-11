%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name bootstrap-sass

Summary: bootstrap-sass is a Sass-powered version of Bootstrap 3
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.4.1
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/twbs/bootstrap-sass
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(autoprefixer-rails) >= 5.2.1
Requires: %{?scl_prefix}rubygem(sassc) >= 2.0.0

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
bootstrap-sass is a Sass-powered version of Bootstrap, ready to drop right into
your Sass powered applications.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/eyeglass-exports.js
%{gem_instdir}/tasks
%{gem_instdir}/templates
%{gem_instdir}/assets
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/*.gemspec
%exclude %{gem_instdir}/*.json
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/*.md
%{gem_instdir}/Rakefile

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.4.1-2
- Rebuild against rh-ruby27

* Thu Apr 23 2020 Ondřej Ezr <oezr@redhat.com> 3.4.1-1
- Update bootstrap-sass to 3.4.1

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.3.7-5
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.3.7-4
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.3.7-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.3.7-2
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Mon Oct 10 2016 Dominic Cleal <dominic@cleal.org> 3.3.7-1
- Update bootstrap-sass to 3.3.7 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 3.3.6-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 3.3.6-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Mon Jan 18 2016 Dominic Cleal <dcleal@redhat.com> 3.3.6-1
- Update bootstrap-sass to 3.3.6 for Patternfly (elobatocs@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 3.0.3.0-3
- Replace tfm-rubygem-sass with ror41-rubygem-sass (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 3.0.3.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Sun Dec 29 2013 Dominic Cleal <dcleal@redhat.com> 3.0.3.0-1
- new package built with tito
