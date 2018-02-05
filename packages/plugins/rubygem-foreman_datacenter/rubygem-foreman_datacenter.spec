%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_datacenter
%global plugin_name datacenter

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.45
Release: 1%{?foremandist}%{?dist}
Summary: A plugin that lets you document your servers in a datacenter
Group: Applications/Systems
License: GPLv3
URL: https://github.com/theforeman/foreman_datacenter
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: foreman >= 1.16
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(prawn) >= 2.1
Requires: %{?scl_prefix}rubygem(prawn) < 3
Requires: %{?scl_prefix}rubygem(rqrcode) >= 0.10.1
Requires: %{?scl_prefix}rubygem(rqrcode) < 0.11
BuildRequires: foreman-assets
BuildRequires: foreman-plugin >= 1.16
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem(prawn) >= 2.1
BuildRequires: %{?scl_prefix}rubygem(prawn) < 3
BuildRequires: %{?scl_prefix}rubygem(rqrcode) >= 0.10.1
BuildRequires: %{?scl_prefix}rubygem(rqrcode) < 0.11
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}

%description
A plugin that lets you document your servers in a datacenter.


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

%foreman_bundlerd_file
%foreman_precompile_plugin -s

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
%{foreman_assets_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_db_migrate}
%{foreman_restart}
exit 0

%changelog
