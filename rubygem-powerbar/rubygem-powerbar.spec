
%{?scl:%scl_package rubygems-%{gem_name}}
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
Release:   7%{?dist}
Summary:   %{_summary}
Group:     Development/Languages
License:   %{_license}
URL:       %{_url}
Source0:   http://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}

Requires:  %{?scl_prefix}rubygem(ansi) >= 1.4.0
Requires:  %{?scl_prefix}rubygem(ansi) <  1.5.0
Requires:  %{?scl_prefix}rubygem(hashie) >= 1.1.0

%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && 0%{!?scl:1})
Requires:  %{?scl_prefix}ruby(abi)
BuildRequires: %{?scl_prefix}ruby(abi)
%else
Requires:  %{?scl_prefix}ruby(release)
BuildRequires: %{?scl_prefix}ruby(release)
%endif
Requires:  %{?scl_prefix}rubygems

BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

%description
%{desc}

%package   doc
BuildArch: noarch
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
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

%if 0%{?fedora} > 18
%gem_install
%else
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install -V --local --install-dir .%{gem_dir} --force --rdoc \
    %{gem_name}-%{version}.gem
%{?scl:"}
%endif

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

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

%if 0%{?rhel} == 6 || 0%{?fedora} < 19
%{gem_dir}/bin/powerbar-demo
%endif

%files doc
%doc %{gem_instdir}/README.rdoc
%doc %{gem_docdir}/rdoc
%doc %{gem_docdir}/ri

%changelog
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

