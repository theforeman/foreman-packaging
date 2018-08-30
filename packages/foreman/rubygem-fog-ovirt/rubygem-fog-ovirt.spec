%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-ovirt

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.2
Release: 1%{?dist}
Summary: Module for the 'fog' gem to support Ovirt
Group: Development/Languages
License: MIT
URL: https://github.com/fog/fog-ovirt
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(fog-core)
Requires: %{?scl_prefix}rubygem(fog-core)
Requires: %{?scl_prefix}rubygem(fog-json)
Requires: %{?scl_prefix}rubygem(fog-xml)
Requires: %{?scl_prefix}rubygem(fog-xml)
Requires: %{?scl_prefix}rubygem(ovirt-engine-sdk) >= 4.1.3
Requires: %{?scl_prefix}rubygem(rbovirt) >= 0.1.5
Requires: %{?scl_prefix}rubygem(rbovirt) < 0.2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This library can be used as a module for `fog`.


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
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.md
%exclude %{gem_instdir}/%{gem_name}.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/tests

%changelog
* Thu Aug 30 2018 Ori Rabin <orrabin@gmail.com> 1.1.2-1
- Update to 1.1.2

* Thu Jul 12 2018 Ivan Nečas <inecas@redhat.com> 1.1.1-1
- Update to 1.1.1

* Thu Jun 14 2018 Ori Rabin <orrabin@gmail.com> 1.0.4-1
- Update to 1.0.4

* Wed Apr 11 2018 Ori Rabin <orabin@redhat.com> 1.0.3-1
- Update to 1.0.3

* Thu Apr 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.2-1
- Update to 1.0.2

* Tue Apr 03 2018 Michael Moll <mmoll@mmoll.at> 1.0.1-1
- Update fog-ovirt to 1.0.1

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.2-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)

* Wed Dec 13 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.1.2-1
- new package built with tito

