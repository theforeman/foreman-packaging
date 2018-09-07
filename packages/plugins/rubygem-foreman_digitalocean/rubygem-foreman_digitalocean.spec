# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_digitalocean
%global plugin_name digitalocean
%global foreman_min_version 1.16.0

Summary:    Provision and manage DigitalOcean droplets from Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    1.3.0
Release:    3%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman-digitalocean
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(fog-digitalocean) >= 0.3
Requires: %{?scl_prefix}rubygem(fog-digitalocean) < 1
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
Provides: foreman-%{plugin_name}
# end generated dependencies
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Provision and manage DigitalOcean droplets from Foreman.


%package doc
BuildArch:  noarch
Group:      Documentation
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
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
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%posttrans
%{foreman_restart}
exit 0

%changelog
* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.3.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Sun May 27 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.3.0-2
- Regenerate spec file based on the current template

* Fri Feb 16 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.0-1
- update foreman_digitalocean to 1.3.0 (kvedulv@kvedulv.de)
- Restructure plugin packages to prepare for obal (pcreech@redhat.com)

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.0-5
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Tue Jan 03 2017 Dominic Cleal <dominic@cleal.org> 1.2.0-1
- Update foreman_digitalocean to 1.2.0 (mail@timogoebel.name)

* Mon Oct 03 2016 Dominic Cleal <dominic@cleal.org> 1.1.0-1
- Update foreman-digitalocean to 1.1 (me@daniellobato.me)
- Use gem_install macro (dominic@cleal.org)

* Mon Apr 18 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- plugins:foreman_digitalocean - 1.0.0 (elobatocs@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.2.1-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Oct 28 2015 Dominic Cleal <dcleal@redhat.com> 0.2.1-1
- plugins:foreman_digitalocean - Release 0.2.1 (elobatocs@gmail.com)
- Add foremandist (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Apr 28 2015 Tommy McNeely <tommy@lark-it.com> 0.2.0-1
- Version 0.2.0 (tommy@lark-it.com)
- #10242 - Changed template name to _base for Foreman 1.8

* Fri Feb 13 2015 Tommy McNeely <tommy@lark-it.com> 0.1.0-1
- Version 0.1.0 (tommy@lark-it.com)
- #8617 - add SSH key pair integration
- #8650 - show region name in VM details

* Wed Dec 10 2014 Daniel Lobato <dlobatog@redhat.com> 0.0.3-1
- Version 0.0.3 (dlobatog@redhat.com)

* Tue Dec 02 2014 Daniel Lobato <dlobatog@redhat.com> 0.0.2-1
- Initial version 0.0.2-1 (dlobatog@redhat.com)
