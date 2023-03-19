# template: default
%global gem_name ancestry

Name: rubygem-%{gem_name}
Version: 4.3.0
Release: 1%{?dist}
Summary: Organize ActiveRecord model into a tree structure
License: MIT
URL: https://github.com/stefankroes/ancestry
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Ancestry allows the records of a ActiveRecord model to be organized in a tree
structure, using the materialized path pattern. It exposes the standard
relations (ancestors, parent, root, children, siblings, descendants)
and allows them to be fetched in a single query. Additional features include
named scopes, integrity checking, integrity restoration, arrangement
of (sub)tree into hashes and different strategies for dealing with orphaned
records.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

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
* Sun Mar 19 2023 Foreman Packaging Automation <packaging@theforeman.org> 4.3.0-1
- Update to 4.3.0

* Wed Aug 24 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.2.0-1
- Update to 4.2.0

* Fri Jul 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.2.1-1
- Update to 3.2.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.0.7-2
- Rebuild against rh-ruby27

* Fri May 01 2020 Michael Moll <mmoll@mmoll.at> - 3.0.7-1
- Update ancestry to 3.0.7

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.0-5
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.0-4
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.0.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.0.0-2
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Thu May 25 2017 Dominic Cleal <dominic@cleal.org> 3.0.0-1
- Update ancestry to 3.0.0 (dominic@cleal.org)

* Wed Oct 26 2016 Dominic Cleal <dominic@cleal.org> 2.2.1-1
- Update ancestry to 2.2.1 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 2.0.0-5
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 2.0.0-4
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 2.0.0-3
- Converted to tfm SCL (dcleal@redhat.com)
- Fixes #9703 - change %%{dist} to %%{?dist} (jmontleo@redhat.com)

* Fri Sep 27 2013 Lukas Zapletal <lzap+git@redhat.com> 2.0.0-2
- bumping ancestry (lzap+git@redhat.com)

* Fri Sep 27 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 2.0.0-1
- bump to 2.0.0 because this is in Fedora 19 now

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 1.3.0-4
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.0-2
- new package built with tito

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.3.0-1
- new package built with tito
