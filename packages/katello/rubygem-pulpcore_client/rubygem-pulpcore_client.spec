# Generated from pulpcore_client-3.0.0rc2.dev.1557772471.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name pulpcore_client

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.16.7
Release: 1%{?dist}
Epoch: 1
Summary: Pulp 3 API Ruby Gem
Group: Development/Languages
License: GPLv2
URL: https://openapi-generator.tech
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 1.9
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(faraday) >= 0.17
Requires: %{?scl_prefix}rubygem(faraday) < 1
Requires: %{?scl_prefix}rubygem(faraday) < 1.9.0
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.1.0
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.1
Requires: %{?scl_prefix_ruby}rubygem(json) < 3
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Pulp3 api library for core functionality.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}
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
%{gem_instdir}/git_push.sh
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

#workaround for https://pulp.plan.io/issues/8950
%exclude %{gem_instdir}/dist
%exclude %{gem_instdir}/build
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/pulpcore
%exclude %{gem_instdir}/pulp_rpm_client.egg-info
%exclude %{gem_instdir}/*.txt
%exclude %{gem_instdir}/*.cfg
%exclude %{gem_instdir}/*.ini
%exclude %{gem_instdir}/setup.py*

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%{gem_instdir}/pulpcore_client.gemspec
%{gem_instdir}/spec

%changelog
* Fri May 06 2022 ianballou <ianballou67@gmail.com> 1:3.16.7-1
- Update to 3.16.7

* Tue Nov 02 2021 ianballou <ianballou67@gmail.com> 1:3.16.0-1
- Update to 3.16.0

* Wed Oct 20 2021 Justin Sherrill <jsherril@redhat.com> 1:3.15.2-1
- Update to 3.15.2

* Wed Jul 07 2021 James Jeffers <jjeffers@redhat.com> 1:3.14.1-1
- Update to 3.14.1

* Tue Jul 06 2021 James Jeffers <jjeffers@redhat.com> 1:3.14.0-1
- Update to 3.14.0

* Tue Mar 30 2021 Justin Sherrill <jsherril@redhat.com> 1:3.11.0-1
- Update to 3.11.0

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 1:3.9.0-2
- Rebuild for Ruby 2.7

* Mon Jan 11 2021 ianballou <ianballou67@gmail.com> 1:3.9.0-1
- Update to 3.9.0

* Thu Oct 15 2020 ianballou <ianballou67@gmail.com> 1:3.7.1-1
- Update to 3.7.1

* Thu Aug 20 2020 Justin Sherrill <jsherril@redhat.com> 1:3.6.0-1
- Update to 3.6.0

* Mon Jun 08 2020 James Jeffers 1:3.4.1-1
- Update to 3.4.1

* Mon May 04 2020 Justin Sherrill <jsherril@redhat.com> 1:3.3.0-1
- Update to 3.3.0

* Thu Mar 26 2020 Samir Jha <sjha4@ncsu.edu> 1:3.2.1-1
- Update to 3.2.1

* Thu Jan 30 2020 Justin Sherrill <jsherril@redhat.com> 1:3.0.0-3
- Handle epoch -doc requirement

* Thu Jan 30 2020 Justin Sherrill <jsherril@redhat.com> 1:3.0.0-2
- bump epoch, as rc2 has higher evr

* Mon Jan 06 2020 Justin Sherrill <jsherril@redhat.com> 3.0.0-1
- Update to 3.0.0


* Mon May 13 2019 Justin Sherrill <jlsherrill@gmail.com> 3.0.0rc2.dev.1557772471-1
- Add rubygem-pulpcore_client generated by gem2rpm using the scl template
