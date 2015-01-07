%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global commit 6a96698f42475975375b027b4d3bf5d8511b4a8f
%global gem_name jgrep

Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.3.3
Release:        5%{?dist}
Summary:        Query JSON structure with a matching language

Group:          Development/Tools
License:        ASL 2.0
URL:            http://jgrep.org/
Source0:        https://github.com/ploubser/JSON-Grep/archive/%{commit}/JSON-Grep-%{commit}.tar.gz
Patch0:         0001-Fix-test-run.patch
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}rubygems-devel
BuildRequires:  %{?scl_prefix}rubygem(rspec)
BuildRequires:  %{?scl_prefix}rubygem(mocha)
BuildRequires:  %{?scl_prefix}rubygem(json)
%if 0%{?fedora} > 18
Requires:       %{?scl_prefix}ruby(release) >= 1.8
%else
Requires:       %{?scl_prefix}ruby(abi) >= 1.8
%endif
Requires:       %{?scl_prefix}rubygems
Requires:       %{?scl_prefix}rubygem(json)
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}

%description
JGrep is  Ruby-based CLI tool and API for parsing and displaying JSON data
using a logical expression syntax. It allows you to search a list of JSON
documents and return specific documents or values based on logical truths.


%package doc
Summary:        Documentation for %{pkg_name}
Group:          Documentation
Requires:       %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}


%prep
%setup -qn JSON-Grep-%{commit}
%patch0 -p1


%build
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{gem_name}-%{version}.gem
%{?scl:"}


%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}


%check
%{?scl:scl enable %{scl} "}
rspec -Ilib spec
%{?scl:"}


%files
%{_bindir}/*
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/*.gemspec
%{gem_spec}
%doc COPYING README.markdown


%files doc
%{gem_docdir}


%changelog
* Wed Jan 07 2015 Dominic Cleal <dcleal@redhat.com> 1.3.3-5
- Import from Fedora and SCLise (dcleal@redhat.com)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.3.3-3
- Disable tests on rhel

* Tue Apr 29 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.3.3-2
- Run tests (Lukas Bezdicka, #1092000)
- Fix issue with tests. (Guess adding the run was a good idea...)

* Mon Apr 28 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.3.3-1
- Initial packaging
