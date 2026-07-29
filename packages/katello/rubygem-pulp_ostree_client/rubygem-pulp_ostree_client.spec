# template: default
%global gem_name pulp_ostree_client

Name: rubygem-%{gem_name}
Version: 2.6.1
Release: 1%{?dist}
Epoch: 1
Summary: Pulp 3 API Ruby Gem
License: GPL-2.0+
URL: https://github.com/pulp/pulp_ostree
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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%exclude %{gem_instdir}/pulp_ostree_client.gemspec
%{gem_instdir}/spec

%changelog
* Wed Jul 29 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1:2.6.1-1
- Update to 2.6.1

* Wed Apr 22 2026 Samir Jha <samirjha1525@gmail.com> - 1:2.6.0-1
- Update to 2.6.0

* Sun Feb 15 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1:2.5.3-1
- Update to 2.5.3

* Mon Feb 02 2026 Zach Huntington-Meath <zhunting@redhat.com> - 1:2.5.0-3
- Bumping to rebuild for COPR after being reverted.

* Wed Dec 10 2025 ianballou <ianballou67@gmail.com> - 1:2.5.0-2
- Add Epoch of 1 for https://projects.theforeman.org/issues/38832

* Fri Dec 05 2025 ianballou <ianballou67@gmail.com> - 2.5.0-2
- Decrement to 2.5.0 temporarily for https://projects.theforeman.org/issues/38832

* Mon Nov 03 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.5.3-1
- Update to 2.5.3

* Wed Oct 29 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.5.1-1
- Update to 2.5.1

* Thu Oct 02 2025 ianballou <ianballou67@gmail.com> - 2.5.0-1
- Update to 2.5.0

* Wed Apr 23 2025 Ian Ballou <ianballou67@gmail.com> - 2.4.8-1
- Update to 2.4.8

* Wed Feb 12 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.4.5-1
- Update to 2.4.5

* Wed Oct 30 2024 Ian Ballou <ianballou67@gmail.com> - 2.4.4-1
- Update to 2.4.4

* Tue Jul 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.3.2-1
- Update to 2.3.2

* Sun Jun 23 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.3.1-1
- Update to 2.3.1

* Wed Mar 27 2024 sajha <sajha> - 2.3.0-1
- Update to 2.3.0

* Wed Nov 08 2023 ianballou <ianballou67@gmail.com> 2.1.3-1
- Update to 2.1.3

* Fri Aug 04 2023 ianballou <ianballou67@gmail.com> 2.1.1-1
- Update to 2.1.1

* Thu Jun 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.1.0-1
- Update to 2.1.0

* Mon Apr 17 2023 Evgeni Golov 2.0.0-1
- Update to 2.0.0

* Tue Oct 05 2021 Justin Sherrill <jsherril@redhat.com> 2.0.0-0.1.a1
- initial build

