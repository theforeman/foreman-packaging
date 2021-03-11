%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global	gem_name	text

%if 0%{?fedora} >= 21
%global	gem_minitest	rubygem(minitest4)
%else
%global	gem_minitest	rubygem(minitest)
%endif

Name:		%{?scl_prefix}rubygem-%{gem_name}
Version:	1.3.0
Release:	8%{?dist}
Summary:	Collection of text algorithms

License:	MIT
URL:		https://github.com/threedaymonk/text
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	%{?scl_prefix_ruby}ruby(release)
BuildRequires:	%{?scl_prefix_ruby}rubygems-devel
# Check
BuildRequires:	%{?scl_prefix_ruby}%gem_minitest
BuildRequires:	%{?scl_prefix_ruby}rubygem(test-unit)
Requires:	%{?scl_prefix_ruby}ruby(release)
Requires:	%{?scl_prefix_ruby}ruby(rubygems)

BuildArch:	noarch
Provides:	%{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A collection of text algorithms: Levenshtein, Soundex, Metaphone, Double
Metaphone, Figlet, Porter Stemming

%package	doc
Summary:	Documentation for %{pkg_name}
Group:	Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch:	noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T

TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

%{?scl:scl enable %{scl} - << \EOF}
gem unpack -V %{SOURCE0}
%{?scl:EOF}
cd %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
%{?scl:EOF}
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
%{?scl:scl enable %{scl} - <<EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
ruby -Ilib:test:. -e 'Dir.glob("test/*_test.rb").each{|f| require f}'
%{?scl:EOF}
popd

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/README.rdoc
%doc	%{gem_instdir}/COPYING.txt

%{gem_libdir}/
%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%exclude	%{gem_instdir}/Rakefile
%exclude	%{gem_instdir}/test/

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.3.0-8
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.3.0-7
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.3.0-6
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.0-5
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.3.0-4
- Fix build errors and modernise specs (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.3.0-3
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Nov 24 2014 Dominic Cleal <dcleal@redhat.com> 1.3.0-2
- Convert to SCL

* Fri Jun 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.0-1
- 1.3.0

* Thu Jun 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-4
- Force to use minitest ver4 for now

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-2
- Include license text

* Wed Aug 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-1
- 1.2.3

* Sun Aug 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.2-1
- Initial package
