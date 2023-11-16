# template: default
%global gem_name domain_name

Name: rubygem-%{gem_name}
Version: 0.6.20231109
Release: 1%{?dist}
Summary: Domain Name manipulation library for Ruby
License: BSD-2-Clause and BSD-3-Clause and MPL-2.0
URL: https://github.com/knu/ruby-domain_name
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7.0
BuildRequires: ruby >= 2.7.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
This is a Domain Name manipulation library for Ruby.
It can also be used for cookie domain validation based on the Public
Suffix List.


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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_instdir}/tool
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.document
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/domain_name.gemspec
%{gem_instdir}/test

%changelog
* Thu Nov 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.6.20231109-1
- Update to 0.6.20231109

* Fri Jul 22 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.5.20190701-1
- Update to 0.5.20190701

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.5.20160310-5
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.5.20160310-4
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.5.20160310-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.5.20160310-2
- Rebuild packages for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed May 25 2016 Dominic Cleal <dominic@cleal.org> 0.5.20160310-1
- new package built with tito

