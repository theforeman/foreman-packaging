# template: default
%global gem_name erubi

Name: rubygem-%{gem_name}
Version: 1.13.0
Release: 1%{?dist}
Summary: Small ERB Implementation
License: MIT
URL: https://github.com/jeremyevans/erubi
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Erubi is a ERB template engine for ruby. It is a simplified fork of Erubis.


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
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile

%changelog
* Sun Jul 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.13.0-1
- Update to 1.13.0

* Tue Jan 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.12.0-1
- Update to 1.12.0

* Sun Aug 28 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.11.0-1
- Update to 1.11.0

* Wed Jul 06 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.10.0-1
- Update to 1.10.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.9.0-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.9.0-1
- Release rubygem-erubi 1.9.0

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.7.1-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.7.1-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 1.7.1-2
- Bump for moving over to foreman-packaging

* Thu Jul 26 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.7.1-1
- Initial package
