%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
# Generated from ZenTest-4.1.4.gem by gem2rpm -*- rpm-spec -*-

%global gem_name ZenTest
%global rubyabi 1.9.1

Summary: Automated test scaffolding for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.8.1
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.zenspider.com/ZSS/Products/ZenTest/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
ZenTest is an automated test scaffolding for Ruby that provides 4 different
tools: zentest, unit_diff, autotest and multiruby. These tools can be used for
test conformance auditing and rapid XP.

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
gem install --local --install-dir .%{gem_dir} \
            --force -V --rdoc %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gem_dir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gem_dir}/bin
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod 0755

# Various files marked executable that shouldn't be, and remove needless
# shebangs
find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/bin/env ruby"#!%{?scl:%_scl_root}/usr/bin/ruby"'
find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/local/bin/ruby"#!%{?scl:%_scl_root}/usr/bin/ruby"'
find %{buildroot}%{gem_instdir}/test -type f | \
  xargs -n 1 sed -i  -e '/^#!\/usr\/.*\/ruby.*/d'
# Ships with extremely tight permissions, bring them inline with other gems
find %{buildroot}%{gem_instdir} -type f | \
  xargs chmod 0644
find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs chmod 0755

%check
pushd .%{gem_instdir}
%{?scl:scl enable %scl "}
testrb -Ilib test
%{?scl:"}
popd

%files
%{_bindir}/autotest
%{_bindir}/multigem
%{_bindir}/multiruby
%{_bindir}/multiruby_setup
%{_bindir}/unit_diff
%{_bindir}/zentest
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_instdir}/lib
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/articles
%{gem_instdir}/example*.rb
%{gem_instdir}/example.txt

%changelog
* Tue Mar 05 2013 Miroslav Suchý <msuchy@redhat.com> 4.8.1-2
- new package built with tito

* Tue Jul 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 4.8.1-1
- Updated to ZenTest 4.8.1.
- Specfile cleanup.

* Fri Mar 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 4.6.2-2
- Rebuilt for scl.

* Sun Jan 21 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.6.2-1
- 4.6.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Mo Morsi - 4.6.0-1
- New upstream version. Minor fixes and enhancements.

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 4.3.3-3
- Replace BR(check) with BR

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 26 2010 Matthew Kent <mkent@magoazul.com> - 4.3.3-1
- New upstream version. Minor fixes and enhancements.

* Tue May 4 2010 Matthew Kent <mkent@magoazul.com> - 4.3.1-1
- New upstream version. Minor bugfixes - 1.9 compatibility.

* Sun Jan 24 2010 Matthew Kent <mkent@magoazul.com> - 4.2.1-1
- New upstream version.
- Don't reorganize files, leave as upstream intended.

* Sat Nov 21 2009 Matthew Kent <mkent@magoazul.com> - 4.1.4-3
- Drop Requires on hoe, only used by Rakefile (#539442).
- Move Rakefile to -doc (#539442).

* Sat Nov 21 2009 Matthew Kent <mkent@magoazul.com> - 4.1.4-2
- Better Source (#539442).
- More standard permissions on files.

* Mon Nov 16 2009 Matthew Kent <mkent@magoazul.com> - 4.1.4-1
- Initial package
