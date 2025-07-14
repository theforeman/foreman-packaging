# template: default
%global gem_name formatador

Name: rubygem-%{gem_name}
Version: 1.1.1
Release: 1%{?dist}
Summary: Ruby STDOUT text formatting
License: MIT
URL: https://github.com/geemus/formatador
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
STDOUT text formatting.


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
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/changelog.txt
%{gem_instdir}/formatador.gemspec
%{gem_instdir}/tests

%changelog
* Sun Jul 13 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.1.1-1
- Update to 1.1.1

* Sun Nov 06 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.1.0-1
- Update to 1.1.0

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.3.0-1
- Update to 0.3.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.2.1-13
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.2.1-12
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.2.1-11
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.2.1-10
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.2.1-9
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.2.1-8
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.1-6
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.1-4
- Set %%bootstrap to 0 to allow tests.

* Wed Jan 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.1-3
- Rebuilt for Ruby 1.9.3.
- Added %%bootstrap macro for tests.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.1-1
- Update to 0.2.1
- Added check section
- Introduced doc subpackage
- Added tests patch for the case when output is redirected to a file (would fail in mock and koji)

* Thu Jul 21 2011 Chris Lalancette <clalance@redhat.com> - 0.1.4-2
- Remove bogus shindo and rake dependencies

* Tue Jul 05 2011 Chris Lalancette <clalance@redhat.com> - 0.1.4-1
- Initial package
