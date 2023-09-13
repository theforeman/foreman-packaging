# template: default
%global gem_name pulp_deb_client

Name: rubygem-%{gem_name}
Version: 2.21.2
Release: 1%{?dist}
Summary: Pulp 3 DEB plugin API Ruby Gem
License: GPLv2+
URL: https://github.com/pulp/pulp_deb
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
%exclude %{gem_instdir}/pulp_deb_client.gemspec
%{gem_instdir}/spec

%changelog
* Wed Sep 13 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.21.2-1
- Update to 2.21.2

* Fri Aug 04 2023 ianballou <ianballou67@gmail.com> 2.21.1-1
- Update to 2.21.1

* Sun Apr 30 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.20.2-1
- Update to 2.20.2

* Sun Dec 11 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.20.1-1
- Update to 2.20.1

* Wed Oct 26 2022 Samir Jha <sjha4@ncsu.edu> 2.20.0-1
- Update to 2.20.0

* Tue Oct 25 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.18.2-1
- Update to 2.18.2

* Thu Aug 25 2022 Samir Jha <sjha4@ncsu.edu> 2.18.1-1
- Update to 2.18.1

* Thu Jul 14 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.18.0-2
- Allow faraday 1.x
- Regenerate spec

* Wed Apr 27 2022 Quirin Pamp <pamp@atix.de> 2.18.0-1
- Update to 2.18.0

* Thu Apr 21 2022 ianballou <ianballou67@gmail.com> 2.17.1-1
- Update to 2.17.1

* Tue Nov 02 2021 ianballou <ianballou67@gmail.com> 2.16.0-1
- Update to 2.16.0

* Wed Oct 06 2021 Justin Sherrill <jsherril@redhat.com> 2.15.0-1
- Update to 2.15.0

* Tue Sep 14 2021 Justin Sherrill <jsherril@redhat.com> 2.13.1-1
- Update to 2.13.1

* Tue Jul 06 2021 James Jeffers <jjeffers@redhat.com> 2.13.0-1
- Update to 2.13.0

* Tue Apr 27 2021 Quirin Pamp <pamp@atix.de> 2.11.1-1
- Update to 2.11.1

* Mon Apr 12 2021 Justin Sherrill <jsherril@redhat.com> 2.10.0-1
- Update to 2.10.0

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.8.0-2
- Rebuild for Ruby 2.7

* Mon Jan 11 2021 ianballou <ianballou67@gmail.com> 2.8.0-1
- Update to 2.8.0

* Thu Oct 15 2020 Justin Sherrill <jsherril@redhat.com> 2.7.0-1
- Update to 2.7.0

* Wed May 13 2020 Markus Bucher <bucher@atix.de> - 2.3.0-0.1.b1
- Add rubygem-pulp_deb_client generated by gem2rpm using the scl template
