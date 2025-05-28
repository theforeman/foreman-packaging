# template: foreman_plugin
%global gem_name foreman_vault
%global plugin_name vault
%global foreman_min_version 3.13

Name: rubygem-%{gem_name}
Version: 3.0.0
Release: 1%{?foremandist}%{?dist}
Summary: Adds support for using credentials from Hashicorp Vault
License: GPLv3
URL: https://github.com/dm-drogeriemarkt/foreman_vault
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.5
Requires: ruby < 4
BuildRequires: ruby >= 2.5
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Adds support for using credentials from Hashicorp Vault.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

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
* Sun May 18 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.0-1
- Update to 3.0.0

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
