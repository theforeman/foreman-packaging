%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%if !("%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16)
%global gem_dir /usr/lib/ruby/gems/1.8
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_libdir %{gem_instdir}/lib
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%endif

%global gem_name strong_parameters

Summary: Permitted and required parameters for Action Pack
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.2.1
Release: 9%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/rails/strong_parameters
Source0: %{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: rubygem-actionpack => 3.0
Requires: rubygem-actionpack < 4
Requires: rubygem-activemodel => 3.0
Requires: rubygem-activemodel < 4
Requires: rubygem-railties => 3.0
Requires: rubygem-railties < 4

%if 0%{?fedora} > 18
Requires: ruby(release) = 2.0.0
Requires: rubygems
BuildRequires: ruby(release) = 2.0.0
BuildRequires: rubygems-devel
%else
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires:  %{?scl_prefix}rubygems-devel
%else
Requires: ruby(abi) = 1.8
Requires: rubygems
BuildRequires: ruby(abi) = 1.8
BuildRequires: rubygems
%endif
%endif

BuildArch: noarch
Provides: rubygem(strong_parameters) = %{version}

%description
Permitted and required parameters for Action Pack

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -q -T -c
mkdir -p ./%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir ./%{gem_dir} -V --force --rdoc %{SOURCE0}
%{?scl:"}
pushd .%{gem_instdir}
popd

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -va ./%{gem_dir}/* %{buildroot}%{gem_dir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{gem_instdir}
%{gem_instdir}/MIT-LICENSE
%{gem_instdir}/Rakefile
%{gem_instdir}/lib/
%{gem_instdir}/test/
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/README.md
%{gem_instdir}/test/

%changelog
* Thu Dec 19 2013 Jason Montleon <jmontleo@redhat.com> 0.2.1-9
- fix fedora version for ruby abi/release version (jmontleo@redhat.com)

* Thu Dec 19 2013 Jason Montleon <jmontleo@redhat.com> 0.2.1-8
- remove ruby-wrapper dependency for now (jmontleo@redhat.com)

* Wed Dec 18 2013 Jason Montleon <jmontleo@redhat.com> 0.2.1-7
- add unpackaged files (jmontleo@redhat.com)
- Automatic commit of package [rubygem-strong_parameters] minor release
  [0.2.1-6-sat]. (jmontleo@redhat.com)
- more file section fixes (jmontleo@redhat.com)
- more file section fixes (jmontleo@redhat.com)
- file section fixes (jmontleo@redhat.com)
- Automatic commit of package [rubygem-strong_parameters] minor release
  [0.2.1-5-sat]. (jmontleo@redhat.com)
- remove template errors (jmontleo@redhat.com)
- Automatic commit of package [rubygem-strong_parameters] minor release
  [0.2.1-4-sat]. (jmontleo@redhat.com)
- more scl build fixes (jmontleo@redhat.com)
- Automatic commit of package [rubygem-strong_parameters] minor release
  [0.2.1-3-sat]. (jmontleo@redhat.com)
- more scl build fixes (jmontleo@redhat.com)
- Automatic commit of package [rubygem-strong_parameters] minor release
  [0.2.1-2-sat]. (jmontleo@redhat.com)
- scl build fixes (jmontleo@redhat.com)
- Automatic commit of package [rubygem-strong_parameters] minor release
  [0.2.1-1-sat]. (jmontleo@redhat.com)
- add rubygem-strong_parameters (jmontleo@redhat.com)

* Wed Dec 18 2013 Jason Montleon <jmontleo@redhat.com> 0.2.1-6
- more file section fixes (jmontleo@redhat.com)
- more file section fixes (jmontleo@redhat.com)
- file section fixes (jmontleo@redhat.com)

* Wed Dec 18 2013 Jason Montleon <jmontleo@redhat.com> 0.2.1-5
- remove template errors (jmontleo@redhat.com)

* Wed Dec 18 2013 Jason Montleon <jmontleo@redhat.com> 0.2.1-4
- more scl build fixes (jmontleo@redhat.com)

* Wed Dec 18 2013 Jason Montleon <jmontleo@redhat.com> 0.2.1-3
- more scl build fixes (jmontleo@redhat.com)

* Wed Dec 18 2013 Jason Montleon <jmontleo@redhat.com> 0.2.1-2
- scl build fixes (jmontleo@redhat.com)

* Wed Dec 18 2013 Jason Montleon <jmontleo@redhat.com> 0.2.1-1
- new package built with tito

