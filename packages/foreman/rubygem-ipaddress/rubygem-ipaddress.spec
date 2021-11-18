%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from ipaddress-0.8.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ipaddress

Summary: IPv4/IPv6 addresses manipulation library
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.8.0
Release: 13%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/bluemonk/ipaddress
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-ipaddress-0.8.0-ruby2-conversion.patch
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(test-unit)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
IPAddress is a Ruby library designed to make manipulation
of IPv4 and IPv6 addresses both powerful and simple. It maintains
a layer of compatibility with Ruby's own IPAddr, while
addressing many of its issues.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

# Remove un-needed file
# See https://github.com/bluemonk/ipaddress/issues/23
rm .%{gem_instdir}/.document

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/README.rdoc
%{gem_instdir}/VERSION
%{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Rakefile

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.8.0-13
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.8.0-12
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.8.0-11
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.0-10
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.8.0-9
- Refresh ruby2 conversion patch to apply (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.8.0-8
- Fix build errors and modernise specs (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.8.0-7
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 22 2014 Dominic Cleal <dcleal@redhat.com> 0.8.0-6
- SCLize for EL6/7

* Fri Mar 15 2013 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-5
- Fix build breakage on >= F19 with new Ruby guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 29 2012 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-3
- Correct duplicate LICENSE file

* Thu Dec 27 2012 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-2
- Revised per review in bz#823340

* Mon Apr 30 2012 Jonas Courteau <rpms@courteau.org> - 0.8.0-1
- Initial package
- Submitted https://github.com/bluemonk/ipaddress/issues/23 upstream to remove extra file from gem
