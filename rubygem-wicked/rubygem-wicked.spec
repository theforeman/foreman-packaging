%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name wicked

%define _version 1.0.2
%define _summary Wicked is a Rails engine for producing easy wizard controllers
%define _url https://github.com/schneems/wicked
%define _license MIT

%define desc Wicked is a Rails engine for producing easy wizard controllers

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   %{_version}
Release:   3%{?dist}
Summary:   %{_summary}
Group:     Development/Languages
License:   %{_license}
URL:       %{_url}
Source0:   http://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && 0%{!?scl:1})
Requires:  %{?scl_prefix}ruby(abi)
BuildRequires: %{?scl_prefix}ruby(abi)
%else
Requires:  %{?scl_prefix}ruby(release)
BuildRequires: %{?scl_prefix}ruby(release)
%endif
Requires:  %{?scl_prefix}rubygems
Requires:  %{?scl_prefix}rubygem(rails) >= 3.0.7

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
%dir %{gem_instdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.rvmrc
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/wicked.gemspec
%{gem_spec}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/VERSION
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/CHANGELOG.md

%files doc
%doc %{gem_instdir}/test
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}/rdoc
%doc %{gem_docdir}/ri

%changelog
* Fri Jun 06 2014 Dominic Cleal <dcleal@redhat.com> 1.0.2-3
- Modernise and update for EL7 (dcleal@redhat.com)

* Tue Apr 08 2014 Marek Hulan <mhulan@redhat.com> 1.0.2-2
- Fixing wicked-doc dependency (mhulan@redhat.com)

* Wed Apr 02 2014 Marek Hulan <mhulan@redhat.com> 1.0.2-1
- new package built with tito


