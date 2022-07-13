# template: default
%global gem_name pulp_ansible_client

Name: rubygem-%{gem_name}
Version: 0.13.2
Release: 1%{?dist}
Summary: Pulp 3 API Ruby Gem
License: GPL-2.0+
URL: https://openapi-generator.tech
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.9
BuildRequires: ruby >= 1.9
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Fetch, Upload, Organize, and Distribute Software Packages.


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

%files
%dir %{gem_instdir}
%{gem_instdir}/git_push.sh
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%{gem_instdir}/pulp_ansible_client.gemspec
%{gem_instdir}/spec

%changelog
* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.13.2-1
- Update to 0.13.2

* Thu Jun 16 2022 ianballou <ianballou67@gmail.com> 0.13.1-1
- Update to 0.13.1

* Tue Apr 12 2022 ianballou <ianballou67@gmail.com> 0.12.1-1
- Update to 0.12.1

* Wed Oct 06 2021 Justin Sherrill <jsherril@redhat.com> 0.10.1-1
- Update to 0.10.1

* Fri Aug 27 2021 Justin Sherrill <jsherril@redhat.com> 0.9.1-1
- Update to 0.9.1

* Tue Jul 06 2021 James Jeffers <jjeffers@redhat.com> 0.8.0-1
- Update to 0.8.0

* Fri Jun 11 2021 Justin Sherrill <jsherril@redhat.com> 0.7.3-1
- Update to 0.7.3

* Tue Mar 30 2021 Justin Sherrill <jsherril@redhat.com> 0.7.1-1
- Update to 0.7.1

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.6.0-2
- Rebuild for Ruby 2.7

* Mon Jan 11 2021 ianballou <ianballou67@gmail.com> 0.6.0-1
- Update to 0.6.0

* Thu Oct 15 2020 ianballou <ianballou67@gmail.com> 0.4.2-1
- Update to 0.4.2

* Fri Sep 11 2020 Justin Sherrill <jsherril@redhat.com> 0.3.0-1
- Update to 0.3.0

* Thu Aug 20 2020 Justin Sherrill <jsherril@redhat.com> 0.2.0-1
- Update to 0.2.0

* Mon May 04 2020 Justin Sherrill <jsherril@redhat.com> 0.2.0b13.dev01588546902-1
- Update to 0.2.0b13.dev01588546902

* Thu Mar 26 2020 Samir Jha <sjha4@ncsu.edu> 0.2.0b11-1
- Update rubygem-pulp_ansible_client to 0.2.0.b11

* Tue Jun 25 2019 Justin Sherrill <jlsherrill@gmail.com> - 0.2.0b1.dev0.1560866833-1
- initial build
