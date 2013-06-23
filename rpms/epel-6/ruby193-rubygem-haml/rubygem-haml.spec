%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from haml-2.2.14.gem by gem2rpm -*- rpm-spec -*-
%global gem_name haml

Summary: An elegant, structured XHTML/XML templating engine
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.1.6
Release: 2%{?dist}
Group: Development/Languages
License: MIT and WTFPL
URL: http://haml-lang.com/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
# for html2haml
Requires: %{?scl_prefix}rubygem(erubis)
Requires: %{?scl_prefix}rubygem(hpricot)
Requires: %{?scl_prefix}rubygem(ruby_parser)
Requires: %{?scl_prefix}rubygem(sass)

BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(erubis)
BuildRequires: %{?scl_prefix}rubygem(hpricot)
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(rails)
BuildRequires: %{?scl_prefix}rubygem(ruby_parser)
BuildRequires: %{?scl_prefix}rubygem(sass)

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Haml (HTML Abstraction Markup Language) is a layer on top of XHTML or XML
that's designed to express the structure of XHTML or XML documents in a
non-repetitive, elegant, easy way, using indentation rather than closing
tags and allowing Ruby to be embedded with ease.
It was originally envisioned as a plugin for Ruby on Rails, but it can
function as a stand-alone templating engine.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} --force -V --rdoc %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gem_dir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gem_dir}/bin

%check
pushd %{buildroot}%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
ruby -I. -e "Dir.glob('test/**/*_test.rb').each {|t| require t}"
%{?scl:EOF}
popd

%files
%{_bindir}/haml
%{_bindir}/html2haml
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/bin
%{gem_instdir}/init.rb
%{gem_instdir}/rails
%{gem_instdir}/REVISION
%{gem_instdir}/VERSION
%{gem_instdir}/VERSION_NAME
%exclude %{gem_instdir}/.*
# No vendored libraries thanks
%exclude %{gem_instdir}/vendor
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING
%doc %{gem_instdir}/README.md
%{gem_instdir}/extra
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 3.1.6-2
- converted $GEM to $PGEM (lzap+git@redhat.com)
- import $GEM from Fedora (lzap+git@redhat.com)
- require ruby193-build for tagging (msuchy@redhat.com)

* Fri Jul 27 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.1.6-1
- Updated to Haml 3.1.6.
- Removed patch that is included in this upstream release.
- Introduced -doc subpackage.
- Simplified the test running.
- Adjusted Requires accordingly.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.1.2-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Mo Morsi <mmorsi@redhat.com> - 3.1.2-3
- remove fssm dependency as upstream project no longer bundles it
  (sass, which is vendored by haml upstream, still depends on it)

* Fri Jul 22 2011 Chris Lalancette <clalance@redhat.com> - 3.1.2-2
- Fix up the sass includes

* Mon Jul 11 2011 Mo Morsi <mmorsi@redhat.com> - 3.1.2-1
- updated to latest upstream release

* Tue Mar 29 2011 Mo Morsi <mmorsi@redhat.com> - 3.0.25-1
- updated to latest upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 26 2010 Matthew Kent <mkent@magoazul.com> - 3.0.17-1
- New upstream version.
- Include VERSION and VERSION_NAME in main package (#627454).
- Exclude vendored copy of fssm.

* Thu Aug 12 2010 Matthew Kent <mkent@magoazul.com> - 3.0.15-2
- New BR on rubygem-erubis and ruby_parser.

* Wed Jul 28 2010 Matthew Kent <mkent@magoazul.com> - 3.0.15-1
- New upstream version.
- New dependencies on yard/maruku.

* Tue May 4 2010 Matthew Kent <mkent@magoazul.com> - 2.2.24-1
- New upstream version - minor bugfixes and improvements.
- Drop unused sitelib macro.
- No backup files to cleanup now.

* Mon Jan 04 2010 Michal Babej <mbabej@redhat.com> - 2.2.20-1
- update to new upstream release

* Mon Jan 04 2010 Michal Babej <mbabej@redhat.com> - 2.2.16-1
- update to new upstream release
- get rid of test_files macro
- add shebang/permission handling from Jeroen van Meeuwen

* Fri Dec 04 2009 Michal Babej <mbabej@redhat.com> - 2.2.15-2
- change %%define to %%global
- change license to "MIT and WTFPL" (test/haml/spec/README.md)
- add Requires on hpricot for html2haml
- change %%gem_dir to %%gem_instdir where appropriate

* Wed Dec 02 2009 Michal Babej <mbabej@redhat.com> - 2.2.15-1
- Update to new upstream release
- URL changed by upstream

* Wed Dec 02 2009 Michal Babej <mbabej@redhat.com> - 2.2.14-1
- Initial package
