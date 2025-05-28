# template: default
%global gem_name pulp_rpm_client

Name: rubygem-%{gem_name}
Version: 3.29.2
Release: 1%{?dist}
Summary: Pulp 3 RPM plugin API Ruby Gem
License: GPLv2+
URL: https://github.com/pulp/pulp_rpm
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

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
%exclude %{gem_instdir}/pulp_rpm_client.gemspec
%{gem_instdir}/spec

%changelog
* Wed Apr 23 2025 Ian Ballou <ianballou67@gmail.com> - 3.29.2-1
- Update to 3.29.2

* Wed Oct 30 2024 Ian Ballou <ianballou67@gmail.com> - 3.27.2-1
- Update to 3.27.2

* Wed Oct 23 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.26.3-1
- Update to 3.26.3

* Tue Jul 02 2024 Ian Ballou <ianballou67@gmail.com> - 3.26.1-1
- Update to 3.26.1

* Tue Jul 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.25.5-1
- Update to 3.25.5

* Sun Apr 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.25.3-1
- Update to 3.25.3

* Tue Apr 02 2024 sajha <sajha> - 3.25.2-1
- Update to 3.25.2

* Wed Mar 27 2024 sajha <sajha> - 3.25.1-1
- Update to 3.25.1

* Wed Jan 31 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.23.2-1
- Update to 3.23.2

* Wed Nov 08 2023 ianballou <ianballou67@gmail.com> 3.23.0-1
- Update to 3.23.0

* Fri Aug 04 2023 ianballou <ianballou67@gmail.com> 3.22.3-1
- Update to 3.22.3

* Sun Jul 09 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.19.8-1
- Update to 3.19.8

* Sun Jun 18 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.19.7-1
- Update to 3.19.7

* Sun May 07 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.19.6-1
- Update to 3.19.6

* Fri May 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.19.5-1
- Update to 3.19.5

* Sun Apr 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.19.4-1
- Update to 3.19.4

* Sun Apr 02 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.19.3-1
- Update to 3.19.3

* Sun Mar 26 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.19.2-1
- Update to 3.19.2

* Wed Mar 08 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.19.1-1
- Update to 3.19.1

* Wed Feb 15 2023 ianballou <ianballou67@gmail.com> 3.19.0-1
- Update to 3.19.0

* Wed Feb 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.18.10-1
- Update to 3.18.10

* Tue Nov 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.18.9-1
- Update to 3.18.9

* Thu Nov 10 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.18.8-1
- Update to 3.18.8

* Wed Oct 26 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.18.7-1
- Update to 3.18.7

* Wed Oct 26 2022 Samir Jha <sjha4@ncsu.edu> 3.18.5-1
- Update to 3.18.5

* Tue Oct 25 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.17.14-1
- Update to 3.17.14

* Sun Oct 02 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.17.13-1
- Update to 3.17.13

* Thu Aug 25 2022 Samir Jha <sjha4@ncsu.edu> 3.17.12-1
- Update to 3.17.12

* Thu Jul 14 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.17.7-1
- Update to 3.17.7

* Fri Feb 25 2022 ianballou <ianballou67@gmail.com> 3.17.4-1
- Update to 3.17.4

* Tue Nov 02 2021 ianballou <ianballou67@gmail.com> 3.16.1-1
- Update to 3.16.1

* Wed Oct 06 2021 Justin Sherrill <jsherril@redhat.com> 3.15.0-1
- Update to 3.15.0

* Thu Jul 08 2021 James Jeffers <jjeffers@redhat.com> 3.13.3-1
- Update to 3.13.3

* Fri Jul 02 2021 James Jeffers <jjeffers@redhat.com> 3.13.2-1
- Update to 3.13.2

* Fri Apr 09 2021 ianballou <ianballou67@gmail.com> 3.10.0-1
- Update to 3.10.0

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-2
- Rebuild for Ruby 2.7

* Wed Feb 24 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.9.0-1
- Update to 3.9.0

* Mon Jan 11 2021 ianballou <ianballou67@gmail.com> 3.8.0-1
- Update to 3.8.0

* Thu Oct 15 2020 ianballou <ianballou67@gmail.com> 3.7.0-1
- Update to 3.7.0

* Tue Sep 08 2020 Justin Sherrill <jsherril@redhat.com> 3.6.2-1
- Update to 3.6.2

* Thu Aug 20 2020 Justin Sherrill <jsherril@redhat.com> 3.6.1-1
- Update to 3.6.1

* Mon Aug 03 2020 Samir Jha <sjha4@ncsu.edu> 3.5.0-1
- Update to 3.5.0

* Fri Jul 17 2020 Justin Sherrill <jsherril@redhat.com> 3.4.2-1
- Update to 3.4.2

* Mon Jun 08 2020 James Jeffers 3.4.1-1
- Update to 3.4.1

* Mon May 04 2020 Justin Sherrill <jsherril@redhat.com> 3.3.0-1
- Update to 3.3.0

* Thu Mar 26 2020 Samir Jha <sjha4@ncsu.edu> 3.2.0-1
- Update to 3.2.0

* Mon Jan 06 2020 Justin Sherrill <jsherril@redhat.com> 3.0.0-1
- Update to 3.0.0

* Thu Oct 10 2019 <Justin Sherrill> 3.0.0b7.dev01570381057-1
- Initial build generated by gem2rpm using the scl template
