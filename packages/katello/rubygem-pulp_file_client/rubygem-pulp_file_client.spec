# template: default
%global gem_name pulp_file_client

Name: rubygem-%{gem_name}
Version: 3.73.7
Release: 1%{?dist}
Summary: Pulp 3 API Ruby Gem
License: GPLv2+
URL: https://github.com/pulp/pulp_file
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
%exclude %{gem_instdir}/pulp_file_client.gemspec
%{gem_instdir}/spec

%changelog
* Wed Apr 23 2025 Ian Ballou <ianballou67@gmail.com> - 3.73.7-1
- Update to 3.73.7

* Wed Apr 09 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.14-1
- Update to 3.63.14

* Thu Apr 03 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.13-1
- Update to 3.63.13

* Wed Mar 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.12-1
- Update to 3.63.12

* Sun Mar 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.11-1
- Update to 3.63.11

* Thu Jan 30 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.9-1
- Update to 3.63.9

* Wed Jan 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.8-1
- Update to 3.63.8

* Wed Jan 15 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.7-1
- Update to 3.63.7

* Sun Dec 15 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.6-1
- Update to 3.63.6

* Fri Dec 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.5-1
- Update to 3.63.5

* Wed Nov 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.4-1
- Update to 3.63.4

* Sun Nov 24 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.3-1
- Update to 3.63.3

* Wed Nov 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.63.2-1
- Update to 3.63.2

* Wed Oct 30 2024 Ian Ballou <ianballou67@gmail.com> - 3.63.1-1
- Update to 3.63.1

* Sun Oct 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.22-1
- Update to 3.49.22

* Sun Oct 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.21-1
- Update to 3.49.21

* Sun Aug 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.17-1
- Update to 3.49.17

* Sun Aug 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.16-1
- Update to 3.49.16

* Mon May 06 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.6-1
- Update to 3.49.6

* Sun Apr 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.49.5-1
- Update to 3.49.5

* Wed Mar 27 2024 sajha <sajha> - 3.49.3-1
- Update to 3.49.3

* Wed Nov 08 2023 ianballou <ianballou67@gmail.com> 1.15.1-1
- Update to 1.15.1

* Fri Aug 04 2023 ianballou <ianballou67@gmail.com> 1.14.3-1
- Update to 1.14.3

* Wed Feb 15 2023 ianballou <ianballou67@gmail.com> 1.12.0-1
- Update to 1.12.0

* Wed Feb 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.11.3-1
- Update to 1.11.3

* Wed Oct 19 2022 Samir Jha <sjha4@ncsu.edu> 1.11.2-1
- Update to 1.11.2

* Thu Aug 25 2022 Samir Jha <sjha4@ncsu.edu> 1.10.5-1
- Update to 1.10.5

* Thu Jul 14 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.10.3-1
- Update to 1.10.3

* Wed Oct 06 2021 Justin Sherrill <jsherril@redhat.com> 1.10.0-1
- Update to 1.10.0

* Fri Jul 02 2021 James Jeffers <jjeffers@redhat.com> 1.8.1-1
- Update to 1.8.1

* Tue Mar 30 2021 Justin Sherrill <jsherril@redhat.com> 1.6.1-1
- Update to 1.6.1

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.5.0-2
- Rebuild for Ruby 2.7

* Mon Jan 11 2021 ianballou <ianballou67@gmail.com> 1.5.0-1
- Update to 1.5.0

* Thu Oct 15 2020 ianballou <ianballou67@gmail.com> 1.3.0-1
- Update to 1.3.0

* Thu Aug 20 2020 Justin Sherrill <jsherril@redhat.com> 1.2.0-1
- Update to 1.2.0

* Mon Jun 08 2020 James Jeffers 1.0.1-1
- Update to 1.0.1

* Mon May 04 2020 Justin Sherrill <jsherril@redhat.com> 0.3.0-1
- Update to 0.3.0

* Thu Mar 26 2020 Samir Jha <sjha4@ncsu.edu> 0.2.0-1
- Update to 0.2.0

* Mon Jan 06 2020 Justin Sherrill <jsherril@redhat.com> 0.1.0-1
- Update to 0.1.0

* Mon Nov 04 2019 Justin Sherrill <jsherril@redhat.com> 0.1.0b5.dev01571253617-1
- Update to a newer release

* Mon Jun 10 2019 Justin Sherrill <jlsherrill@gmail.com> 3.0.0rc2.dev.1558441126-1
- Update to a recent rc2 release

* Mon May 13 2019 Justin Sherrill <jlsherrill@gmail.com> 0.0.1b10.dev.1557779852-1
- Add rubygem-pulpcore_client generated by gem2rpm using the scl template
