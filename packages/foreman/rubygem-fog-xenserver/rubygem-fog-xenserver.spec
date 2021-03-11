# Generated from fog-xenserver-1.0.0.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-xenserver

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.0
Release: 3%{?dist}
Summary: Module for the 'fog' gem to support XENSERVER
Group: Development/Languages
License: MIT
URL: https://github.com/fog/fog-xenserver
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(fog-xml)
Requires: %{?scl_prefix}rubygem(fog-core)
Requires: %{?scl_prefix}rubygem(xmlrpc)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Module for the 'fog' gem to support XENSERVER.


%package doc
Summary: Documentation for %{pkg_name}
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
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
%{gem_instdir}/gemfiles
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE.md
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fog-xenserver.gemspec
%{gem_instdir}/spec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.0-3
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.0-2
- Bump to release for EL8

* Thu Dec 06 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.0-1
- Update to 1.0.0-1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.2.3-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.2.3-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Mon Feb 29 2016 Dominic Cleal <dominic@cleal.org> 0.2.3-1
- update fog-xenserver to 0.2.3 (kvedulv@kvedulv.de)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.2.2-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Fri Nov 20 2015 Dominic Cleal <dcleal@redhat.com> 0.2.2-1
- new package built with tito

