# template: default
%global gem_name websocket-extensions

Name: rubygem-%{gem_name}
Version: 0.2.0
Release: 1%{?dist}
Summary: Generic extension manager for WebSocket connections
License: Apache-2.0
URL: https://github.com/faye/websocket-extensions-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Generic extension manager for WebSocket connections.


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
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Nov 18 04:15:30 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 0.2.0-1
- Update to 0.2.0

* Mon Jul 27 2026 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.5-3
- rebuilt

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.1.5-2
- Rebuild against rh-ruby27

* Fri Jul 31 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.1.5-1
- Release rubygem-websocket-extensions 0.1.5

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.4-1
- Release rubygem-websocket-extensions 0.1.4

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.3-4
- Bump packages to build for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.3-3
- Update spec to include Obsoletes of rails-packaging version
* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 0.1.3-2
- Bump for moving over to foreman-packaging

* Thu Jul 26 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.3-1
- Initial package
