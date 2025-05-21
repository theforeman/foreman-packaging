# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_host_extra_validator
%global plugin_name host_extra_validator
%global foreman_min_version 3.0.0

Summary:    This plugin adds extra validations to a host
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.2.2
Release:    2%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_host_extra_validator
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
This plugin adds extra validations to a host.


%package doc
BuildArch:  noarch
Group:      Documentation
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for %{pkg_name}

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

%foreman_bundlerd_file

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
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
* Wed May 21 2025 Zach Huntington-Meath <zhunting@redhat.com> - 0.2.2-2
- Removed unversioned obsoletes

* Sun Jan 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.2.2-1
- Update to 0.2.2

* Fri Nov 04 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.2.1-1
- Update to 0.2.1

* Mon Oct 24 2022 Marek Hulan <mhulan@redhat.com> 0.2.0-1
- Update to 0.2.0

* Mon May 09 2022 Evgeni Golov - 0.1.0-5
- log plugin installation in posttrans

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.1.0-4
- Rebuild plugins for Ruby 2.7

* Tue Jul 21 2020 Evgeni Golov - 0.1.0-3
- Drop posttrans macros

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Aug 02 2018 Timo Goebel <mail@timogoebel.name> - 0.1.0-1
- Update foreman_host_extra_validator to 0.1.0

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.4-3
- Regenerate spec file based on the current template

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.4-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Jul 20 2016 Timo Goebel <mail@timogoebel.name> 0.0.4-1
- initial packaging
