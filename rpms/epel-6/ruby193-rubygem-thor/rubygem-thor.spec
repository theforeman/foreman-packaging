%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

# Generated from thor-0.12.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name thor

%global rubyabi 1.9.1

Summary: Scripting framework that replaces rake, sake and rubigen
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.15.4
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/wycats/thor
Source0: http://rubygems.org/download/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}rubygem(rake)
Requires: %{?scl_prefix}rubygem(diff-lcs)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildRequires: %{?scl_prefix}rubygem(rake)
BuildRequires: %{?scl_prefix}rubygem(rdoc)
BuildRequires: %{?scl_prefix}rubygem(fakeweb)
BuildRequires: %{?scl_prefix}rubygem(bundler)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Thor is a scripting framework that replaces rake, sake and rubigen.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
This package contains documentation for %{pkg_name}.

%prep
%setup -q -c -T

mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gem_dir} \
  --force --rdoc \
  %{SOURCE0}
%{?scl:"}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gem_dir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gem_dir}/bin
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/bin/env ruby"#!%{?scl:%_scl_root}/usr/bin/ruby"'

%clean
rm -rf %{buildroot}

%check
pushd %{buildroot}%{gem_instdir}
# kill simplecov dependency
sed -i '3,7d' spec/spec_helper.rb
%{?scl:scl enable %scl - << \EOF}
LANG=en_US.utf8 rspec spec
%{?scl:EOF}
popd

%files
%{_bindir}/thor
%{_bindir}/rake2thor
%doc %{gem_instdir}/LICENSE.md
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Thorfile
%{gem_instdir}/spec
%{gem_instdir}/thor.gemspec

%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 0.15.4-4
- Revert "bootstrap thor" (msuchy@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 0.15.4-3
- bootstrap thor (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.15.4-2
- new package built with tito

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.15.4-1
- Update to Thor 0.15.4.
- Specfile cleanup

* Thu May 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.6-7
- Fix patches to apply cleanly.

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.6-6
- Rebuilt for scl.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.6-5
- Enable tests.
- Add patches for the failing tests.
- Removed unnecessary ParseTree dependency.

* Mon Jan 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.6-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Mohammed Morsi <mmorsi@redhat.com> - 0.14.6-1
- Updated to latest upstream version

* Wed May 5 2010 Matthew Kent <mkent@magoazul.com> - 0.13.6-1
- New upstream version.

* Fri Dec 18 2009 Matthew Kent <mkent@magoazul.com> - 0.12.0-2
- Add Requires for rubygem(rake) (#542559).
- Upstream replaced Source after the gemcutter migration, update to latest
  (#542559).
- Add Requires for rubygem(diff-lcs) as Thor can take advantage of it for
  colourized diff output (#542559).

* Mon Nov 16 2009 Matthew Kent <mkent@magoazul.com> - 0.12.0-1
- Initial package
