# template: default
%global gem_name pulp_certguard_client

Name: rubygem-%{gem_name}
Version: 3.49.21
Release: 1%{?dist}
Summary: Pulp 3 API Ruby Gem
License: GPLv2+
URL: https://github.com/pulp/pulp-certguard
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
%exclude %{gem_instdir}/pulp_certguard_client.gemspec
%{gem_instdir}/spec

%changelog
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

* Sun May 14 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.6.5-1
- Update to 1.6.5

* Thu May 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.6.4-1
- Update to 1.6.4

* Mon Mar 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.5.8-1
- Update to 1.5.8

* Sun Feb 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.5.7-1
- Update to 1.5.7

* Thu Aug 25 2022 Samir Jha <sjha4@ncsu.edu> 1.5.5-1
- Update to 1.5.5

* Thu Jul 14 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.5.3-1
- Update to 1.5.3

* Wed Oct 06 2021 Justin Sherrill <jsherril@redhat.com> 1.5.0-1
- Update to 1.5.0

* Fri Jul 02 2021 James Jeffers <jjeffers@redhat.com> 1.4.0-1
- Update to 1.4.0

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.3-2
- Rebuild for Ruby 2.7

* Thu Oct 15 2020 ianballou <ianballou67@gmail.com> 1.0.3-1
- Update to 1.0.3

* Thu Aug 20 2020 Justin Sherrill <jsherril@redhat.com> 1.0.2-1
- Update to 1.0.2

* Fri May 29 2020 Justin Sherrill <jsherril@redhat.com> 0.1.0rc5-1
- Initial build
