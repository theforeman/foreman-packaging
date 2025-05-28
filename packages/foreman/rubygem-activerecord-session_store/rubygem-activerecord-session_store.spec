# template: default
%global gem_name activerecord-session_store

Name: rubygem-%{gem_name}
Version: 2.2.0
Release: 1%{?dist}
Summary: An Action Dispatch session store backed by an Active Record class
License: MIT
URL: https://github.com/rails/activerecord-session_store
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: (rubygem(cgi) or ruby-default-gems < 3.4)

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
An Action Dispatch session store backed by an Active Record class.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%gemspec_remove_dep -g cgi

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

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Thu Mar 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.2.0-1
- Update to 2.2.0

* Tue Aug 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.1.0-1
- Update to 2.1.0

* Wed Apr 28 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.0-1
- Release 2.0.0

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
