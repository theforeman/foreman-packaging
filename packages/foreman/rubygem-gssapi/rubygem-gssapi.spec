# template: default
%global gem_name gssapi

Name: rubygem-%{gem_name}
Version: 1.3.1
Release: 1%{?dist}
Summary: A FFI wrapper around the system GSSAPI library
License: MIT
URL: https://github.com/zenchild/gssapi
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.8.7
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A FFI wrapper around the system GSSAPI library. Please make sure and read
the
Yard docs or standard GSSAPI documentation if you have any questions.
There is also a class called GSSAPI::Simple that wraps many of the common
features
used for GSSAPI.


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
%license %{gem_instdir}/COPYING
%{gem_instdir}/VERSION
%{gem_libdir}
%exclude %{gem_instdir}/preamble
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%exclude %{gem_instdir}/gssapi.gemspec
%{gem_instdir}/test

%changelog
* Sun Aug 28 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.3.1-1
- Update to 1.3.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.2.0-8
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.2.0-7
- Bump to release for EL8

* Tue Oct 01 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.2.0-6
- Update and rebuild into SCL

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.2.0-5
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.2.0-4
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)

* Fri Sep 29 2017 Michael Moll <kvedulv@kvedulv.de> 1.2.0-3
- Use ffi from tfm SCL (eric.d.helms@gmail.com)

* Fri Sep 29 2017 Eric D. Helms <ericdhelms@gmail.com> 1.2.0-2
- Get rubygem-ffi from the ror SCL (ewoud@kohlvanwijngaarden.nl)

* Fri Sep 29 2017 Eric D. Helms <ericdhelms@gmail.com>
- Get rubygem-ffi from the ror SCL (ewoud@kohlvanwijngaarden.nl)

* Mon Sep 25 2017 Daniel Lobato Garcia <me@daniellobato.me> 1.2.0-1
- new package built with tito

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 22 2014 <jpazdziora@redhat.com> - 1.2.0-1
- 1145033 - rebased to gssapi-1.2.0.gem.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 Jan Pazdziora <jpazdziora@redhat.com> - 1.1.2-2
- 981119 - adding dependence on krb5-libs which provides the .so.

* Mon Jun 24 2013 Jan Pazdziora <jpazdziora@redhat.com> - 1.1.2-1
- Initial package
