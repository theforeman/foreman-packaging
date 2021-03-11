%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ancestry

Summary: Organise ActiveRecord model into a tree structure
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 3.0.7
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/stefankroes/ancestry
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(activerecord) >= 3.2.2
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(ancestry) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Ancestry allows the records of a ActiveRecord model to be organised in a tree
structure, using a single, intuitively formatted database column. It exposes
all the standard tree structure relations (ancestors, parent, root, children,
siblings, descendants) and all of them can be fetched in a single sql query.
Additional features are named_scopes, integrity checking, integrity
restoration, arrangement of (sub)tree into hashes and different strategies
for dealing with orphaned records.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p .%{gem_dir}

# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} - << EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
mv %{buildroot}%{gem_instdir}/{MIT-LICENSE,README.md} ./

%files
%license MIT-LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%exclude %{gem_instdir}/init.rb
%exclude %{gem_instdir}/install.rb

%files doc
%doc %{gem_docdir}
%doc README.md
%{gem_instdir}/ancestry.gemspec

%changelog
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
