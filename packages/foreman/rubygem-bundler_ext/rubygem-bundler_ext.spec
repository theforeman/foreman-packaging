%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from bundler_ext-0.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bundler_ext

Summary: Load system gems via Bundler DSL
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.1
Release: 6%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/bundlerext/bundler_ext
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?el6} && 0%{!?scl:1}
Requires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}rubygem(bundler)
%if 0%{?el6} && 0%{!?scl:1}
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}ruby
# BuildRequires: %{?scl_prefix}rubygem(rspec)
# BuildRequires: %{?scl_prefix_ruby}rubygem(bundler)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Simple library leveraging the Bundler Gemfile DSL to load gems already on the
system and managed by the systems package manager (like yum/apt)


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
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec/

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.4.1-6
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.4.1-5
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.4.1-4
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.4.1-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.4.1-2
- Rebuild packages for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri Jun 03 2016 Dominic Cleal <dominic@cleal.org> 0.4.1-1
- Update bundler_ext to 0.4.1 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.3.0-9
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.3.0-8
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.3.0-7
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Wed May 28 2014 Dominic Cleal <dcleal@redhat.com> 0.3.0-6
- Update for EL7

* Thu Jun 06 2013 Miroslav Suchý <msuchy@redhat.com> 0.3.0-5
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.3.0-3
- new package built with tito

* Thu Jan 17 2013 Lukas Zapletal <lzap+git@redhat.com> 0.3.0-2
- bundler_ext 0.3.0

* Tue Jan 15 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.3.0-1
- version bump (new namespace)

* Wed Nov 28 2012 Lukas Zapletal <lzap+git@redhat.com> 0.2.0-2
- bundler_ext 0.2.0 version bump

* Wed Nov 28 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.2.0-1
- bumping version to 0.2.0

* Wed Nov 28 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.0-7
- build require rubygems-devel on F17 (msuchy@redhat.com)

* Thu Nov 22 2012 Lukas Zapletal <lzap+git@redhat.com> 0.1.0-6
- bundler_ext - missing libdir and extra test lib

* Thu Nov 22 2012 Lukas Zapletal <lzap+git@redhat.com> 0.1.0-5
- bundler_ext - rubygems require for EL6

* Thu Nov 22 2012 Lukas Zapletal <lzap+git@redhat.com> 0.1.0-4
- removing %check section from bundler_ext

* Thu Nov 22 2012 Lukas Zapletal <lzap+git@redhat.com> 0.1.0-3
- new package built with tito

* Thu Nov 22 2012 Vít Ondruch <vondruch@redhat.com> - 0.1.0-2
- Add RHEL6 and Fedora 16 compatibility.

* Tue Nov 20 2012 Vít Ondruch <vondruch@redhat.com> - 0.1.0-1
- Initial package
