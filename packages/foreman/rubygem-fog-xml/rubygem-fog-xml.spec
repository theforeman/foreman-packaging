# template: default
%global gem_name fog-xml

Name: rubygem-%{gem_name}
Version: 0.1.4
Release: 1%{?dist}
Summary: XML parsing for fog providers
License: MIT
URL: https://github.com/fog/fog-xml
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.0.0
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Extraction of the XML parsing tools shared between a
number of providers in the 'fog' gem.


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
%exclude %{gem_instdir}/.ruby-gemset
%license %{gem_instdir}/LICENSE.md
%exclude %{gem_instdir}/gemfiles
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/fog-xml.gemspec
%{gem_instdir}/spec

%changelog
* Fri Jul 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.1.4-1
- Update to 0.1.4

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.1.2-9
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.2-8
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.2-7
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.2-6
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.2-5
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.1.2-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Apr 08 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- Update fog-xml to 0.1.2 (dcleal@redhat.com)
- Fixes #9703 - change %%{dist} to %%{?dist} (jmontleo@redhat.com)

* Thu Nov 20 2014 Dominic Cleal <dcleal@redhat.com> 0.1.1-1
- Update fog-xml to 0.1.1 (dcleal@redhat.com)

* Mon Oct 13 2014 Dominic Cleal <dcleal@redhat.com> 0.1.0-1
- new package built with tito
