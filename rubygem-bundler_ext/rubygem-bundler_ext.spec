%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from bundler_ext-0.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bundler_ext

Summary: Load system gems via Bundler DSL
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.0
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/aeolus-incubator/bundler_ext
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
Requires: %{?scl_prefix}ruby(abi)
%else
Requires: %{?scl_prefix}ruby(release)
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(bundler)
%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
BuildRequires: %{?scl_prefix}ruby(abi)
%else
BuildRequires: %{?scl_prefix}ruby(release)
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}ruby
# BuildRequires: %{?scl_prefix}rubygem(rspec)
# BuildRequires: %{?scl_prefix}rubygem(bundler)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Simple library leveraging the Bundler Gemfile DSL to load gems already on the
system and managed by the systems package manager (like yum/apt)


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/CHANGELOG
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec/

%changelog
* Mon Jun 09 2014 Lukas Zapletal <lzap+git@redhat.com> 0.4.0-1
- Updating bundler_ext to 0.4.0 (lzap+git@redhat.com)

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

* Thu Nov 28 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.2.0-1
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
