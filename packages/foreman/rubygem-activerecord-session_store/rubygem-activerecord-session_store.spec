%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name activerecord-session_store

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.1
Release: 5%{?dist}
Summary: An Action Dispatch session store backed by Active Record
Group: Development/Languages
License: MIT
URL: https://github.com/rails/activerecord-session_store
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(actionpack) >= 4.0
Requires: %{?scl_prefix}rubygem(activerecord) >= 4.0
Requires: %{?scl_prefix}rubygem(multi_json) >= 1.11.2
Requires: %{?scl_prefix}rubygem(multi_json) < 2.0
Requires: %{?scl_prefix}rubygem(rack) >= 1.5.2
Requires: %{?scl_prefix}rubygem(rack) < 3
Requires: %{?scl_prefix}rubygem(railties) >= 4.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
An Action Dispatch session store backed by an Active Record class.

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
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.1.1-5
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.1-4
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.1-3
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.1.1-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Aug 15 2018 Eric D. Helms <ericdhelms@gmail.com> 1.1.1-1
- Bump to 1.1.1

* Wed May 30 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.1.0-4
- Use multi_json from Rails SCL

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.1.0-3
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)

* Thu Sep 28 2017 Michael Moll <kvedulv@kvedulv.de> 1.1.0-2
- Refs #20960 - ar-session_store: multi_json is from tfm SCL now
  (kvedulv@kvedulv.de)

* Wed Sep 27 2017 Daniel Lobato Garcia <me@daniellobato.me> 1.1.0-1
- Fixes #20960 - update activerecord-session_store to 1.1.0
  (kvedulv@kvedulv.de)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.1.2-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- new package built with tito
