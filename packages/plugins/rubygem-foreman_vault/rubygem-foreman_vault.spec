# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name foreman_vault
%global plugin_name vault
%global foreman_min_version 2.3

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.0
Release: 1%{?foremandist}%{?dist}
Summary: Adds support for using credentials from Hashicorp Vault
Group: Applications/Systems
License: GPLv3
URL: https://github.com/dm-drogeriemarkt/foreman_vault
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(vault) >= 0.1
Requires: %{?scl_prefix}rubygem(vault) < 1
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(vault) >= 0.1
BuildRequires: %{?scl_prefix}rubygem(vault) < 1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Adds support for using credentials from Hashicorp Vault.


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
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Tue May 14 2024 Manuel Laug <laugmanuel@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Thu Aug 18 2022 Manuel Laug <laugmanuel@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Mon May 09 2022 Evgeni Golov - 1.1.0-3
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.1.0-2
- Stop generaing apipie cache

* Thu Oct 21 2021 Manuel Laug <laugmanuel@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.0-2
- Rebuild plugins for Ruby 2.7

* Mon Jan 11 2021 Manuel Laug <laugmanuel@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Mon Jan 04 2021 Manuel Laug <laugmanuel@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Wed Jun 10 2020 Manuel Laug <laugmanuel@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Wed Jun 03 2020 Manuel Laug <laugmanuel@gmail.com> - 0.2.0-1
- Update to 0.2.0

* Mon Mar 16 2020  0.1.0-1
- Update to 0.1.0

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.0.1-2
- Drop migrate, seed and restart posttans

* Sat Mar 09 2019 Timo Goebel <mail@timogoebel.name> - 0.0.1-1
- Add foreman_vault plugin
