%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name formatador

%global bootstrap 1

Summary: Ruby STDOUT text formatting
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.2.1
Release: 13%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/geemus/%{gem_name}
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# TODO: Fix tests failing when redirected to a file, reported at
# https://github.com/geemus/formatador/commit/a874311f52a34b9a1f1d0fe9fef20a095b79f941
Patch0: formatador-fix-tests-when-redirecting-to-file.patch
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
%if 0%{bootstrap} < 1
BuildRequires: %{?scl_prefix}rubygem(shindo)
%endif
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
STDOUT text formatting

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

pushd .%{gem_instdir}
%patch0 -p8
popd

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
%if 0%{bootstrap} < 1
pushd .%{gem_instdir}
# fix "uninitialized constant StringIO" until its in the gem, as reported in https://github.com/geemus/formatador/issues/5
sed -i "1i\require 'stringio'" tests/tests_helper.rb
shindo
popd
%endif

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.rdoc
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/tests
%{gem_instdir}/formatador.gemspec

%changelog
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
