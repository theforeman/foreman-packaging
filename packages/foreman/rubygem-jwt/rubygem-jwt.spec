# template: default
%global gem_name jwt

Name: rubygem-%{gem_name}
Version: 2.7.1
Release: 1%{?dist}
Summary: JSON Web Token implementation in Ruby
License: MIT
URL: https://github.com/jwt/ruby-jwt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A pure ruby implementation of the RFC 7519 OAuth JSON Web Token (JWT)
standard.


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
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/AUTHORS
%doc %{gem_instdir}/CHANGELOG.md
%exclude %{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/ruby-jwt.gemspec

%changelog
* Wed Jul 19 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.7.1-1
- Update to 2.7.1

* Tue Feb 21 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.7.0-1
- Update to 2.7.0

* Thu Jan 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.6.0-1
- Update to 2.6.0

* Tue Oct 25 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.5.0-1
- Update to 2.5.0

* Sun Jul 24 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.2.3-1
- Update to 2.2.3

* Mon Apr 05 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-2
- Rebuild against rh-ruby27

* Thu Mar 18 2021 Rahul Bajaj <rahulrb0509@gmail.com> 2.2.2-1
- Update jwt to 2.2.2

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.1-2
- Bump to release for EL8

* Tue Oct 08 2019 Rahul Bajaj <rahulrb0509@gmail.com> 2.2.1-1
- Update to 2.2.1

* Sat Feb 23 2019 Timo Goebel <mail@timogoebel.name> 2.1.0-1
- Update jwt to 2.1.0

* Thu Sep 13 2018 Timo Goebel <mail@timogoebel.name> 1.2.1-1
- Update jwt to 1.2.1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.2.0-6
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.0-5
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 1.2.0-4
- Use gem_install macro (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.2.0-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.2.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 1.2.0-1
- Update jwt to 1.2.0 (dcleal@redhat.com)

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 0.1.8-1
- new package built with tito
