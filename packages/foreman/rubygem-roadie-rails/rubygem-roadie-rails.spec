# template: default
%global gem_name roadie-rails

Name: rubygem-%{gem_name}
Version: 3.1.0
Release: 1%{?dist}
Summary: Making HTML emails comfortable for the Rails rockstars
License: MIT
URL: https://github.com/Mange/roadie-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6
BuildRequires: ruby >= 2.6
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Hooks Roadie into your Rails application to help with email generation.


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
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/codecov.yml
%{gem_libdir}
%exclude %{gem_instdir}/setup.sh
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Upgrading.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/roadie-rails.gemspec

%changelog
* Wed Oct 25 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.1.0-1
- Update to 3.1.0

* Mon Aug 29 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.0.0-1
- Update to 3.0.0

* Tue May 24 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-1
- Release rubygem-roadie-rails 2.3.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.1.1-3
- Rebuild against rh-ruby27

* Thu Apr 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 2.1.1-2
- Update requirements for a newer railties

* Thu Apr 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 2.1.1-1
- Update to 2.1.1

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.0-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.0-2
- Update spec to remove the ror scl

* Fri Feb 15 2019 Michael Moll <mmoll@mmoll.at> - 2.0.0-1
- Bump rubygem-roadie-rails to 2.0.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.3.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Aug 15 2018 Eric D. Helms <ericdhelms@gmail.com> 1.3.0-1
- Bump to 1.3.0

* Thu Jan 04 2018 Eric D. Helms <ericdhelms@gmail.com> 1.2.1-1
- Bump roadie-rails to 1.2.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Thu Jun 02 2016 Dominic Cleal <dominic@cleal.org> 1.1.1-1
- new package built with tito
