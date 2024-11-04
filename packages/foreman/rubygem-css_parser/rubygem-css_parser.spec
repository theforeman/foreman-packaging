# template: default
%global gem_name css_parser

Name: rubygem-%{gem_name}
Version: 1.17.1
Release: 1%{?dist}
Summary: Ruby CSS parser
License: MIT
URL: https://github.com/premailer/css_parser
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7
BuildRequires: ruby >= 2.7
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A set of classes for parsing CSS in Ruby.


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


%changelog
* Sun Apr 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.17.1-1
- Update to 1.17.1

* Sun Sep 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.16.0-1
- Update to 1.16.0

* Sun Jan 15 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.14.0-1
- Update to 1.14.0

* Tue Jan 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.13.0-1
- Update to 1.13.0

* Sun Sep 25 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.12.0-1
- Update to 1.12.0

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.11.0-1
- Update to 1.11.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.4.7-5
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.7-4
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.4.7-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.4.7-2
- Rebuild packages for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Thu Jan 05 2017 Dominic Cleal <dominic@cleal.org> 1.4.7-1
- Update css_parser to 1.4.7 (dominic@cleal.org)

* Thu Jun 02 2016 Dominic Cleal <dominic@cleal.org> 1.3.7-1
- new package built with tito

