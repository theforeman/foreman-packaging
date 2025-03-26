# template: default
%global gem_name pulpcore_client

Name: rubygem-%{gem_name}
Version: 3.63.12
Release: 1%{?dist}
Epoch: 1
Summary: Pulp 3 API Ruby Gem
License: GPLv2+
URL: https://github.com/pulp/pulpcore
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
Requires: %{name} = %{epoch}:%{version}-%{release}
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
%exclude %{gem_instdir}/pulpcore_client.gemspec
%{gem_instdir}/spec

%changelog
* Wed Mar 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.63.12-1
- Update to 3.63.12

* Sun Mar 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.63.11-1
- Update to 3.63.11

* Thu Jan 30 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.63.9-1
- Update to 3.63.9

* Wed Jan 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.63.8-1
- Update to 3.63.8

* Wed Jan 15 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.63.7-1
- Update to 3.63.7

* Sun Dec 15 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.63.6-1
- Update to 3.63.6

* Fri Dec 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.63.5-1
- Update to 3.63.5

* Wed Nov 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.63.4-1
- Update to 3.63.4

* Sun Nov 24 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.63.3-1
- Update to 3.63.3

* Wed Nov 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.63.2-1
- Update to 3.63.2

* Wed Oct 30 2024 Ian Ballou <ianballou67@gmail.com> - 1:3.63.1-1
- Update to 3.63.1

* Sun Oct 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.49.22-1
- Update to 3.49.22

* Sun Oct 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.49.21-1
- Update to 3.49.21

* Sun Aug 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.49.17-1
- Update to 3.49.17

* Sun Aug 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.49.16-1
- Update to 3.49.16

* Mon May 06 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.49.6-1
- Update to 3.49.6

* Sun Apr 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.49.5-1
- Update to 3.49.5

* Wed Mar 27 2024 sajha <sajha> - 1:3.49.3-1
- Update to 3.49.3

* Wed Jan 31 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.39.9-1
- Update to 3.39.9

* Sun Jan 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.39.8-1
- Update to 3.39.8

* Thu Jan 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.39.6-1
- Update to 3.39.6

* Wed Jan 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:3.39.5-1
- Update to 3.39.5

* Sun Dec 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:3.39.4-1
- Update to 3.39.4

* Sun Dec 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:3.39.3-1
- Update to 3.39.3

* Wed Nov 08 2023 ianballou <ianballou67@gmail.com> 1:3.39.2-1
- Update to 3.39.2

* Sun Oct 15 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:3.28.17-1
- Update to 3.28.17

* Sun Aug 20 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:3.28.11-1
- Update to 3.28.11

* Fri Aug 04 2023 ianballou <ianballou67@gmail.com> 1:3.28.5-1
- Update to 3.28.5

* Thu Jun 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:3.22.7-1
- Update to 3.22.7

* Sun Apr 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:3.22.4-1
- Update to 3.22.4

* Wed Mar 08 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:3.22.3-1
- Update to 3.22.3

* Wed Feb 15 2023 ianballou <ianballou67@gmail.com> 1:3.22.2-1
- Update to 3.22.2

* Sun Feb 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:3.21.5-1
- Update to 3.21.5

* Thu Jan 26 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:3.21.4-1
- Update to 3.21.4

* Fri Nov 18 2022 Foreman Packaging Automation <packaging@theforeman.org> 1:3.21.3-1
- Update to 3.21.3

* Wed Oct 26 2022 Foreman Packaging Automation <packaging@theforeman.org> 1:3.21.2-1
- Update to 3.21.2

* Wed Oct 19 2022 Samir Jha <sjha4@ncsu.edu> 1:3.21.0-1
- Update to 3.21.0

* Sun Sep 18 2022 Foreman Packaging Automation <packaging@theforeman.org> 1:3.18.10-1
- Update to 3.18.10

* Sun Sep 04 2022 Foreman Packaging Automation <packaging@theforeman.org> 1:3.18.9-1
- Update to 3.18.9

* Thu Aug 25 2022 Samir Jha <sjha4@ncsu.edu> 1:3.18.8-1
- Update to 3.18.8

* Thu Jul 14 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:3.18.5-2
- Allow faraday 1.x
- Regenerate template

* Wed May 18 2022 ianballou <ianballou67@gmail.com> 1:3.18.5-1
- Update to 3.18.5

* Thu Apr 21 2022 ianballou <ianballou67@gmail.com> 1:3.17.7-1
- Update to 3.17.7

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
