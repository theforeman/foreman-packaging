# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_hooks

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d

Summary:    Run custom hook scripts on Foreman events
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.3.14
Release:    2%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/theforeman/foreman_hooks
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.4.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-hooks
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Plugin engine for Foreman that enables running custom hook scripts on Foreman
events.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Requires:   %{?scl_prefix}rubygem(jgrep)
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

mkdir -p %{buildroot}%{foreman_dir}/config/hooks
ln -s %{gem_instdir} %{buildroot}%{foreman_dir}/%{gem_name}

# debug script
%{__mkdir_p} %{buildroot}%{foreman_dir}/script/foreman-debug.d
ln -s %{gem_instdir}/extra/foreman-debug.sh %{buildroot}%{foreman_dir}/script/foreman-debug.d/50-foreman_hooks

%files
%dir %{gem_instdir}
%{gem_libdir}
%attr(0755,-,-) %{gem_instdir}/extra/foreman-debug.sh
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%{foreman_dir}/config/hooks
%{foreman_dir}/%{gem_name}
%{foreman_dir}/script/foreman-debug.d/50-foreman_hooks

%exclude %{gem_instdir}/test
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/TODO
%{gem_instdir}/Rakefile

%changelog
* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.3.14-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed May 17 2017 Dominic Cleal <dominic@cleal.org> 0.3.14-1
- Update foreman_hooks to 0.3.14 (dominic@cleal.org)

* Tue Mar 07 2017 Dominic Cleal <dominic@cleal.org> 0.3.13-2
- Added debug hook script (lzap+git@redhat.com)

* Mon Mar 06 2017 Dominic Cleal <dominic@cleal.org> 0.3.13-1
- Update foreman_hooks to 0.3.13 (dominic@cleal.org)

* Mon Sep 05 2016 Dominic Cleal <dominic@cleal.org> 0.3.12-1
- Update foreman_hooks to 0.3.12 (dominic@cleal.org)

* Mon Jun 20 2016 Dominic Cleal <dominic@cleal.org> 0.3.11-1
- Update foreman_hooks to 0.3.11 (dominic@cleal.org)

* Mon May 16 2016 Dominic Cleal <dominic@cleal.org> 0.3.10-1
- Update foreman_hooks to 0.3.10 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.3.9-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Add foremandist to more plugins (dcleal@redhat.com)

* Wed Sep 16 2015 Dominic Cleal <dcleal@redhat.com> 0.3.9-1
- Update foreman_hooks to 0.3.9 (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.3.8-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Jul 30 2015 Dominic Cleal <dcleal@redhat.com> 0.3.8-1
- Update to foreman_hooks 0.3.8 (dcleal@redhat.com)

* Wed Jan 07 2015 Dominic Cleal <dcleal@redhat.com> 0.3.7-3
- Add jgrep dependency to -doc for example helper (dcleal@redhat.com)

* Wed Apr 02 2014 Dominic Cleal <dcleal@redhat.com> 0.3.7-2
- Add /usr/share/foreman/foreman_hooks symlink to gem dir (dcleal@redhat.com)

* Wed Feb 26 2014 Dominic Cleal <dcleal@redhat.com> 0.3.7-1
- Update to foreman_hooks 0.3.7 (dcleal@redhat.com)

* Fri Feb 14 2014 Dominic Cleal <dcleal@redhat.com> 0.3.6-1
- Update to foreman_hooks 0.3.6 (dcleal@redhat.com)

* Mon Jan 27 2014 Dominic Cleal <dcleal@redhat.com> 0.3.5-1
- Update to foreman_hooks 0.3.5 (dcleal@redhat.com)

* Wed Jan 22 2014 Dominic Cleal <dcleal@redhat.com> 0.3.4-1
- Update to foreman_hooks 0.3.4 (dcleal@redhat.com)

* Thu Aug 29 2013 Dominic Cleal <dcleal@redhat.com> 0.3.3-1
- new package built with tito
