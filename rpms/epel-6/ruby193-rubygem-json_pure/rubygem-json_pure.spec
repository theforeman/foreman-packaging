%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name json_pure
%global rubyabi 1.9.1

Summary: JSON Implementation for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.7.3
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2 or Ruby
URL: http://flori.github.com/json
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi} 
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi} 
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(rake)
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%description
This is a JSON implementation in pure Ruby.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
%{?scl:scl enable %scl "}
gem install -V --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}
for file in `find %{buildroot}/%{gem_instdir} -type f -perm /a+x`; do
    [ -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 644 $file
done
for file in `find %{buildroot}/%{gem_instdir} -type f ! -perm /a+x -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 755 $file
done
find %{buildroot}/%{gem_instdir} -type f -perm /g+wx -exec chmod -v g-w {} \;
rm -rf %{buildroot}/%{gem_instdir}/ext
rm -rf %{buildroot}/%{gem_instdir}/java
rm -f %{buildroot}/%{gem_instdir}/json_pure.gemspec
rm -f %{buildroot}/%{gem_instdir}/json.gemspec
rm -f %{buildroot}/%{gem_instdir}/json-java.gemspec
rm -f %{buildroot}/%{gem_instdir}/Gemfile
rm -f %{buildroot}/%{gem_instdir}/diagrams/.keep
rm -f %{buildroot}/%{gem_instdir}/.travis.yml
rm -f %{buildroot}/%{gem_instdir}/.gitignore

%check
pushd %{buildroot}%{gem_instdir}
%{?scl:scl enable %scl - << \EOF}
JSON=pure testrb tests
%{?scl:EOF}
popd

%clean
rm -rf %{buildroot}

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/README-json-jruby.markdown
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/GPL
%doc %{gem_instdir}/COPYING-json-jruby
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/VERSION
%doc %{gem_instdir}/TODO


%files doc
%{gem_instdir}/tests
%{gem_instdir}/data
%{gem_instdir}/tools
%{gem_instdir}/Rakefile
%doc %{gem_docdir}
%{gem_instdir}/install.rb

%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.7.3-2
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.7.3-1
- Updated to Json_Pure 1.7.3.
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.6.3-5
- Rebuilt for scl.

* Mon Jan 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.6.3-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 12 2011 Michal Fojtik <mfojtik@redhat.com> - 1.6.3-2
- Rebuild after Koji outage

* Thu Dec 8 2011 Michal Fojtik <mfojtik@redhat.com> - 1.6.3-1
- Version bump

* Fri Jun 3 2011 Michal Fojtik <mfojtik@redhat.com> - 1.5.1-1
- Version bump
- Removed gtk dependency to keep this lightweight

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 04 2010 Michal Fojtik <mfojtik@redhat.com> - 1.4.6-3
- Removed tests which was failing under F14

* Sat Oct 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.4.6-2
- Fixed failing test
- Removed unusefull rm call

* Mon Aug 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.4.6-1
- Version bump
- Removed BuildRoot
- Moved 'rm' from check to install
- Moved files from -doc to main package and install.rb to -doc

* Tue Jul 20 2010 Michal Fojtik <mfojtik@redhat.com> - 1.4.3-1
- Initial package
