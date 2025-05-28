# template: default
%global gem_name secure_headers

Name: rubygem-%{gem_name}
Version: 7.1.0
Release: 1%{?dist}
Summary: Manages application of security headers with many safe defaults.
License: MIT
URL: https://github.com/twitter/secureheaders
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Add easily configured security headers to responses including content-security-policy, x-frame-options, strict-transport-security, etc


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
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/secure_headers.gemspec

%changelog
* Sun Apr 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 7.1.0-1
- Update to 7.1.0

* Sun Aug 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.7.0-1
- Update to 6.7.0

* Tue Oct 25 2022 Foreman Packaging Automation <packaging@theforeman.org> 6.5.0-1
- Update to 6.5.0

* Sun Aug 28 2022 Foreman Packaging Automation <packaging@theforeman.org> 6.4.0-1
- Update to 6.4.0

* Tue Jul 26 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 6.3.4-1
- Update to 6.3.4

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 6.3.0-3
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 6.3.0-2
- Bump to release for EL8

* Tue Jan 28 2020 Michael Moll <mmoll@mmoll.at> 6.3.0-1
- Update secure_headers to 6.3.0

* Mon Sep 10 2018 Michael Moll <mmoll@mmoll.at> 6.0.0-1
- Update secure_headers to 6.0.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.0.5-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon Apr 30 2018 Michael Moll <mmoll@mmoll.at> 5.0.5-1
- Update secure_headers to 5.0.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.4.1-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Mon Sep 12 2016 Dominic Cleal <dominic@cleal.org> 3.4.1-1
- Update secure_headers to 3.4.1 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 1.4.1-4
- Use gem_install macro (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.4.1-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.4.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Dec 15 2014 Dominic Cleal <dcleal@redhat.com> 1.4.1-1
- Update secure_headers to 1.4.1 (dcleal@redhat.com)

* Mon Oct 13 2014 Dominic Cleal <dcleal@redhat.com> 1.3.3-1
- new package built with tito
