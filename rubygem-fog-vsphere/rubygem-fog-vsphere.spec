%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-vsphere

Summary: Module for the 'fog' gem to support VMware vSphere
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 2.1.1
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/fog/fog-vsphere
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.0.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(fog-core)
Requires: %{?scl_prefix}rubygem(rbvmomi) >= 1.9
Requires: %{?scl_prefix}rubygem(rbvmomi) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.0.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This library can be used as a module for `fog` or as standalone provider to
use vSphere in applications.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

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
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.md
%exclude %{gem_instdir}/fog-vsphere.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/tests

%changelog
* Sun May 27 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.1.1-1
- Bump version to 2.1.1 (suttner@atix.de)

* Thu May 24 2018 Bernhard Suttner <suttner@atix.de> 2.1.1-1
- update fog-vsphere to 2.1.1 (mail@timogoebel.name)

* Wed Dec 27 2017 Daniel Lobato Garcia <me@daniellobato.me> 1.11.3-1
- Update fog-vsphere to 1.11.3 (me@daniellobato.me)

* Fri May 12 2017 Dominic Cleal <dominic@cleal.org> 1.9.2-1
- Update fog-vsphere to 1.9.2 (mhulan@redhat.com)

* Mon Apr 03 2017 Dominic Cleal <dominic@cleal.org> 1.9.0-1
- Update fog-vsphere to 1.9.0 (dominic@cleal.org)

* Tue Jan 31 2017 Dominic Cleal <dominic@cleal.org> 1.7.0-1
- Update fog-vsphere to 1.7.0 (dominic@cleal.org)

* Tue Jan 03 2017 Dominic Cleal <dominic@cleal.org> 1.6.0-1
- Update fog-vsphere to 1.6.0 (dominic@cleal.org)

* Wed Oct 19 2016 Dominic Cleal <dominic@cleal.org> 1.4.0-1
- Update fog-vsphere to 1.4.0 (dominic@cleal.org)

* Fri Jul 29 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- Update fog-vsphere to 1.0.0 (dominic@cleal.org)

* Thu Jun 16 2016 Dominic Cleal <dominic@cleal.org> 0.8.0-1
- Update fog-vsphere to 0.8.0 (dominic@cleal.org)

* Tue May 17 2016 Dominic Cleal <dominic@cleal.org> 0.7.0-1
- Update fog-vsphere to 0.7.0 (dominic@cleal.org)

* Wed Mar 09 2016 Dominic Cleal <dominic@cleal.org> 0.6.3-1
- Update fog-vsphere to 0.6.3 (dominic@cleal.org)

* Fri Mar 04 2016 Dominic Cleal <dominic@cleal.org> 0.6.1-1
- Update fog-vsphere to 0.6.1 (dominic@cleal.org)

* Mon Feb 01 2016 Dominic Cleal <dcleal@redhat.com> 0.6.0-1
- Update fog-vsphere to 0.6.0 (dcleal@redhat.com)

* Tue Jan 19 2016 Dominic Cleal <dcleal@redhat.com> 0.5.0-1
- new package built with tito

