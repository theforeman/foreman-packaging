# template: default
%global gem_name roadie

Name: rubygem-%{gem_name}
Version: 5.2.1
Release: 1%{?dist}
Summary: Making HTML emails comfortable for the Ruby rockstars
License: MIT
URL: https://github.com/Mange/roadie
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7
BuildRequires: ruby >= 2.7
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Roadie tries to make sending HTML emails a little less painful by inlining
stylesheets and rewriting relative URLs for you.


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
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.solargraph.yml
%exclude %{gem_instdir}/.standard.yml
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/roadie.gemspec
%{gem_instdir}/spec

%changelog
* Wed Feb 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.2.1-1
- Update to 5.2.1

* Sun Dec 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.2.0-1
- Update to 5.2.0

* Tue Nov 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 5.1.0-1
- Update to 5.1.0

* Mon Aug 29 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.0.1-1
- Update to 5.0.1

* Fri Jul 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 4.0.0-1
- Update to 4.0.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.4.0-4
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.4.0-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.4.0-2
- Update spec to remove the ror scl

* Fri Feb 15 2019 Michael Moll <mmoll@mmoll.at> - 3.4.0-1
- Bump rubygem-roadie to 3.4.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.2.2-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.2.2-1
- Bump rubygem-roadie to 3.2.2 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Jan 09 2017 Dominic Cleal <dominic@cleal.org> 3.2.1-1
- Update roadie to 3.2.1 (dominic@cleal.org)

* Thu Jan 05 2017 Dominic Cleal <dominic@cleal.org> 3.2.0-1
- Update roadie to 3.2.0 (dominic@cleal.org)

* Thu Jun 02 2016 Dominic Cleal <dominic@cleal.org> 3.1.1-1
- new package built with tito

