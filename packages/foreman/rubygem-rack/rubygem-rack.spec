# template: default
%global gem_name rack

Name: rubygem-%{gem_name}
Version: 2.2.12
Release: 1%{?dist}
Summary: A modular Ruby webserver interface
License: MIT
URL: https://github.com/rack/rack
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3.0
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Rack provides a minimal, modular and adaptable interface for developing
web applications in Ruby. By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.


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

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/rackup
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/bin
%{gem_instdir}/contrib
%{gem_instdir}/example
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/SPEC.rdoc
%{gem_instdir}/rack.gemspec

%changelog
* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.2.12-1
- Update to 2.2.12

* Sun Nov 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.2.10-1
- Update to 2.2.10

* Tue Apr 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.2.9-1
- Update to 2.2.9

* Sun Mar 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.2.8.1-1
- Update to 2.2.8.1

* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.2.8-1
- Update to 2.2.8

* Thu May 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.2.7-1
- Update to 2.2.7

* Sun Apr 02 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.2.6.4-1
- Update to 2.2.6.4

* Wed Mar 08 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.2.6.3-1
- Update to 2.2.6.3

* Mon Jan 23 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.2.6.2-1
- Update to 2.2.6.2

* Wed Jan 04 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.2.5-1
- Update to 2.2.5

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.2.4-1
- Update to 2.2.4

* Sun May 29 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.2.3.1-1
- Release rubygem-rack 2.2.3.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.2.3-2
- Rebuild against rh-ruby27

* Thu Jun 25 2020 Tomer Brisker <tbrisker@gmail.com> - 2.2.3-1
- Release rubygem-rack 2.2.3

* Thu Apr 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 2.2.2-1
- Update to 2.2.2

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.1.1-1
- Release rubygem-rack 2.1.1

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.6-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.6-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 2.0.6-2
- Bump for moving over to foreman-packaging

* Mon Mar 11 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.0.6-1
- Release tfm-ror52-rubygem-rack 2.0.6

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.5-2
- rebuilt

* Mon Aug 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.5-1
- Initial package
