# Generated from powerbar-2.0.1.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name powerbar

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.1
Release: 3%{?dist}
Summary: The last progressbar-library you'll ever need
Group: Development/Languages
License: MIT
URL: https://github.com/busyloop/powerbar
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby > 1.9.3
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hashie) >= 1.1.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby > 1.9.3
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
The last progressbar-library you'll ever need.


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

%setup -q -D -T -n %{gem_name}-%{version}

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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.ruby-version
%exclude %{gem_instdir}/bin/powerbar-demo
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.MD
%{gem_instdir}/Rakefile
%{gem_instdir}/powerbar.gemspec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.1-3
- Rebuild against rh-ruby27

* Thu Mar 26 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.0.1-2
- Rebuild for EL8

* Thu Sep 13 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.1-1
- Update to 2.0.1-1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.17-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.17-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Fri Apr 29 2016 Dominic Cleal <dominic@cleal.org> 1.0.17-1
- Update powerbar to 1.0.17 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.0.11-11
- Fix build errors and modernise specs (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.0.11-10
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 1.0.11-9
- Fix typo in -doc requires on main package (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 1.0.11-8
- Modernise and update for EL7 (dcleal@redhat.com)
- Fix location of binary (dcleal@redhat.com)

* Fri Sep 27 2013 Marek Hulan <mhulan@redhat.com> 1.0.11-7
- Powerbar fixes (mhulan@redhat.com)

* Mon Sep 16 2013 Marek Hulan <mhulan@redhat.com> 1.0.11-6
- Different versions (mhulan@redhat.com)

* Mon Sep 16 2013 Marek Hulan <mhulan@redhat.com> 1.0.11-5
- Demo script (mhulan@redhat.com)

* Mon Sep 16 2013 Marek Hulan <mhulan@redhat.com> 1.0.11-4
- Make bin a dir (mhulan@redhat.com)

* Mon Sep 16 2013 Marek Hulan <mhulan@redhat.com> 1.0.11-3
- Yet another F19 fix (mhulan@redhat.com)

* Mon Sep 16 2013 Marek Hulan <mhulan@redhat.com> 1.0.11-2
- Another fix for F19 (mhulan@redhat.com)

* Mon Sep 16 2013 Marek Hulan <mhulan@redhat.com> 1.0.11-1
- Fixed spec for F19 (mhulan@redhat.com)

* Fri Sep 06 2013 Marek Hulan <mhulan@redhat.com> 1.0.11-0
- new package built with tito
