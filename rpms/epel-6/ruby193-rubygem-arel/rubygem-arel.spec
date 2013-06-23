%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name arel

Summary: Arel is a Relational Algebra for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.0.2
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/rails/%{gem_name}

Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch1: arel-add-bigdecimal-dependency.patch
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(bigdecimal)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(bigdecimal)
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Arel is a Relational Algebra for Ruby. It 1) simplifies the generation complex
of SQL queries and it 2) adapts to various RDBMS systems. It is intended to be
a framework framework; that is, you can build your own ORM with it, focusing
on innovative object and collection modeling as opposed to database
compatibility and query generation.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

pushd .%{gem_dir}
%patch1 -p0
popd

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm %{buildroot}/%{gem_instdir}/.autotest
rm %{buildroot}/%{gem_instdir}/.gemtest

%check
pushd %{buildroot}/%{gem_instdir}/test
%{?scl:scl enable %scl - << \EOF}
ruby -I../lib -I. -e "Dir.glob('./**/test_*').each {|t| require t}"
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/Gemfile
%{gem_libdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/MIT-LICENSE.txt
%doc %{gem_instdir}/README.markdown
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/test
%{gem_instdir}/arel.gemspec
%doc %{gem_instdir}/Manifest.txt
%{gem_instdir}/Rakefile
%doc %{gem_docdir}


%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 3.0.2-4
- new package built with tito

* Tue Jul 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.2-3
- Exclude the cached gem.

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.2-2
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.2-1
- Rebuilt for scl.
- Updated to 3.0.2.

* Fri Mar 09 2012 Vít Ondruch <vondruch@redhat.com> - 2.0.9-4
- Fix dependency on BigDecimal.

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 2.0.9-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 24 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.9-1
- Update to Arel 2.0.9
- Removed unnecessary cleanup

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.7-1
- Updated to Arel 2.0.7 
- Removed some build dependencies

* Fri Jan 07 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.6-3
- Move all documentation into subpackage

* Fri Jan 07 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.6-2
- Clean buildroot

* Fri Jan 7 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.6-1
- Initial package
