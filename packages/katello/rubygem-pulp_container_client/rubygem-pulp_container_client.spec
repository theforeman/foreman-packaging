# template: default
%global gem_name pulp_container_client

Name: rubygem-%{gem_name}
Version: 2.24.1
Release: 1%{?dist}
Summary: Pulp container plugin for Pulp3 API Ruby Gem
License: GPLv2+
URL: https://github.com/pulp/pulp_container
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Obsoletes: rubygem-pulp_docker_client

# start specfile generated dependencies
Requires: ruby >= 2.7
BuildRequires: ruby >= 2.7
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
%exclude %{gem_instdir}/git_push.sh
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%exclude %{gem_instdir}/pulp_container_client.gemspec
%{gem_instdir}/spec

%changelog
* Mon Apr 14 2025 Ian Ballou <ianballou67@gmail.com> - 2.24.1-1
- Update to 2.24.1

* Sun Apr 06 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.22.2-1
- Update to 2.22.2

* Sun Jan 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.22.1-1
- Update to 2.22.1

* Mon Nov 04 2024 Ian Ballou <ianballou67@gmail.com> - 2.22.0-1
- Update to 2.22.0

* Wed Oct 30 2024 Ian Ballou <ianballou67@gmail.com> - 2.21.1-1
- Update to 2.21.1

* Sun Oct 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.20.4-1
- Update to 2.20.4

* Sun Oct 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.20.3-1
- Update to 2.20.3

* Sun Aug 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.20.2-1
- Update to 2.20.2

* Tue May 07 2024 Ian Ballou <ianballou67@gmail.com> - 2.20.0-1
- Update to 2.20.0

* Sun Apr 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.19.3-1
- Update to 2.19.3

* Wed Mar 27 2024 sajha <sajha> - 2.19.2-1
- Update to 2.19.2

* Sun Jan 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.16.4-1
- Update to 2.16.4

* Sun Dec 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.16.3-1
- Update to 2.16.3

* Wed Nov 08 2023 ianballou <ianballou67@gmail.com> 2.16.2-1
- Update to 2.16.2

* Fri Aug 04 2023 ianballou <ianballou67@gmail.com> 2.15.2-1
- Update to 2.15.2

* Sun Jun 18 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.14.6-1
- Update to 2.14.6

* Sun Apr 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.14.5-1
- Update to 2.14.5

* Sun Apr 02 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.14.4-1
- Update to 2.14.4

* Sun Dec 04 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.14.3-1
- Update to 2.14.3

* Wed Oct 26 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.14.2-1
- Update to 2.14.2

* Wed Oct 19 2022 Samir Jha <sjha4@ncsu.edu> 2.14.0-1
- Update to 2.14.0

* Sun Sep 18 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.10.9-1
- Update to 2.10.9

* Sun Sep 04 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.10.8-1
- Update to 2.10.8

* Thu Aug 25 2022 Samir Jha <sjha4@ncsu.edu> 2.10.7-1
- Update to 2.10.7

* Thu Jul 14 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.10.4-1
- Update to 2.10.4

* Thu Apr 07 2022 ianballou <ianballou67@gmail.com> 2.10.3-1
- Update to 2.10.3

* Wed Oct 06 2021 Justin Sherrill <jsherril@redhat.com> 2.9.0-1
- Update to 2.9.0

* Fri Jul 02 2021 James Jeffers <jjeffers@redhat.com> 2.7.0-1
- Update to 2.7.0

* Tue Mar 30 2021 Justin Sherrill <jsherril@redhat.com> 2.4.0-1
- Update to 2.4.0

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.2.0-2
- Rebuild for Ruby 2.7

* Mon Jan 11 2021 ianballou <ianballou67@gmail.com> 2.2.0-1
- Update to 2.2.0

* Thu Oct 15 2020 ianballou <ianballou67@gmail.com> 2.1.0-1
- Update to 2.1.0

* Thu Aug 20 2020 Justin Sherrill <jsherril@redhat.com> 2.0.0-1
- Update to 2.0.0

* Mon Jun 08 2020 James Jeffers 1.4.1-1
- Update to 1.4.1

* Mon May 04 2020 Justin Sherrill <jsherril@redhat.com> 1.3.0-1
- Update to 1.3.0

* Thu Mar 26 2020 Samir Jha <sjha4@ncsu.edu> 1.2.0-1
- Update to 1.2.0

* Mon Dec 02 2019 Justin Sherrill <jlsherrill@gmail.com> 1.0.0-1
- 1.0.0 build

* Mon Dec 02 2019 Justin Sherrill <jlsherrill@gmail.com> 1.0.0-0.1.rc1
- Initial build
