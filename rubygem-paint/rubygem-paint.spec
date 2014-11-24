%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name paint

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.8.7
Release: 3%{?dist}
Summary: Terminal painter
Group: Development/Languages
License: MIT
URL: https://github.com/janlelis/paint
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi)
Requires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}ruby(abi)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
#tests
BuildRequires: %{?scl_prefix}rubygem(rspec)

%description
Paint manages terminal colors and effects for you. It combines the strengths
of term-ansicolor, rainbow and other similar projects into a simple to use,
however still flexible terminal colorization gem with no core extensions by
default.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} "}
gem install \
  --local \
  --install-dir .%{gem_dir} \
  --force \
  --rdoc \
  -V \
  %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd ./%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
rspec spec
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/LICENSE.txt

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/spec

%changelog
* Mon Nov 24 2014 Dominic Cleal <dcleal@redhat.com> 0.8.7-3
- Convert to SCL

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Miroslav Suchý <miroslav@suchy.cz> 0.8.7-1
- rebase paint-0.8.7.gem

* Mon Aug 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.8.6-3
- 998459 - move README and LICENSE to main package
- 998459 - remove excessive cp
- 998459 - use virtual requires
- 998459 - remove ruby mri requires

* Mon Aug 19 2013 Miroslav Suchý <msuchy@redhat.com> 0.8.6-2
- enable tests
- fix files section

* Mon Aug 19 2013 Miroslav Suchý <msuchy@redhat.com> 0.8.6-1
- initial package
