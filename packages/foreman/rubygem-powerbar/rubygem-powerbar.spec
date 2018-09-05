%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# check files-sections at the end of this file and

%global gem_name powerbar

%define _version 1.0.17
%define _summary The last progressbar-library you'll ever need
%define _url https://github.com/busyloop/powerbar
%define _license MIT

%define desc The last progressbar-library you'll ever need

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   %{_version}
Release:   3%{?dist}
Summary:   %{_summary}
Group:     Development/Languages
License:   %{_license}
URL:       %{_url}
Source0:   https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

Requires:  %{?scl_prefix}rubygem(hashie) >= 1.1.0

%if 0%{?el6} && 0%{!?scl:1}
Requires:  %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires:  %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif
Requires:  %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

%description
%{desc}

%package   doc
BuildArch: noarch
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:   Documentation for %{pkg_name}

%description doc
This package contains documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} - <<EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* %{buildroot}%{_bindir}/

%files
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_cache}

%dir %{gem_instdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/powerbar.gemspec
%{gem_spec}
%{gem_libdir}
%dir %{gem_instdir}/bin
%{gem_instdir}/bin/powerbar-demo
%{_bindir}/powerbar-demo

%files doc
%doc %{gem_instdir}/README.MD
%doc %{gem_docdir}/rdoc
%doc %{gem_docdir}/ri

%changelog
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
