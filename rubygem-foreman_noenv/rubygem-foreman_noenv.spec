# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_noenv

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir /etc/foreman/plugins

Summary:    Agent-specified Environment Plugin for Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.0.7
Release:    2%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/joshuabaird/foreman_noenv
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.8.0
Requires:   %{?scl_prefix}rubygem(deface) < 2.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-noenv
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Adds an 'agent-specified host' option to each host in Foreman that prevents
the ENC from outputting host's Puppet environment.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/%{gem_name}.rb
gem '%{gem_name}'
GEMFILE

mkdir -p %{buildroot}%{foreman_pluginconf_dir}
mv %{buildroot}%{gem_instdir}/config/%{gem_name}.yaml \
   %{buildroot}%{foreman_pluginconf_dir}/%{gem_name}.yaml

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/lib
%{gem_instdir}/db/migrate
%{gem_instdir}/locale

%exclude %{gem_cache}
%exclude %{gem_instdir}/test
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%config %{foreman_pluginconf_dir}/%{gem_name}.yaml
%doc %{gem_instdir}/LICENSE

%files doc
%{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%posttrans
/usr/sbin/foreman-rake db:migrate  >/dev/null 2>&1 || :
(/sbin/service foreman status && /sbin/service foreman restart) >/dev/null 2>&1
exit 0

%changelog
* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.7-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Nov 07 2016 Josh Baird <jbaird@follett.com> 0.0.7-1
- Support for Foreman 1.13.x

* Mon Aug 08 2016 Josh Baird <jbaird@follett.com> 0.0.6-1
- Fix whitelisting problem for noenv attribute

* Tue Apr 05 2016 Josh Baird <jbaird@follett.com> 0.0.5-1
- Support for Foreman 1.11.0/Ruby 2.2.4

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Add foremandist to more plugins (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 13 2015 Josh Baird <jbaird@follett.com> 0.0.4-1
- Run db:migrate in %posttrans

* Wed Aug 12 2015 Josh Baird <jbaird@follett.com> 0.0.3-1
- Fix typos and cleanup spec

* Tue Aug 11 2015 Josh Baird <jbaird@follett.com> 0.0.2-1
- Initial build of foreman_noenv 0.0.2-1
