%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# check files-sections at the end of this file and

%global gem_name powerbar

%define _version 1.0.11
%define _summary The last progressbar-library you'll ever need
%define _url https://github.com/busyloop/powerbar
%define _license MIT

%define desc The last progressbar-library you'll ever need

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   %{_version}
Release:   10%{?dist}
Summary:   %{_summary}
Group:     Development/Languages
License:   %{_license}
URL:       %{_url}
Source0:   http://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

Requires:  %{?scl_prefix}rubygem(ansi) >= 1.4.0
Requires:  %{?scl_prefix}rubygem(ansi) <  1.5.0
Requires:  %{?scl_prefix}rubygem(hashie) >= 1.1.0

%if "%{?scl_ruby}" == "ruby193" || (0%{?el6} && 0%{!?scl:1})
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

%if "%{?scl_ruby}" == "ruby193" || (0%{?el6} && 0%{!?scl:1})
mkdir -p .%{_bindir}
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install -V --local --install-dir .%{gem_dir} --force --rdoc \
    --bindir .%{_bindir} %{gem_name}-%{version}.gem
%{?scl:"}
%else
%gem_install
%endif

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* %{buildroot}%{_bindir}/

%files
%exclude %{gem_instdir}/.gitignore
%exclude %dir %{gem_instdir}/ass
%exclude %{gem_instdir}/ass/screenshot.png
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
%doc %{gem_instdir}/README.rdoc
%doc %{gem_docdir}/rdoc
%doc %{gem_docdir}/ri

%changelog
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
