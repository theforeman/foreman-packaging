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
Release:	2%{?dist}
Summary:	Collection of text algorithms

License:	MIT
URL:		http://github.com/threedaymonk/text
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	%{?scl_prefix}ruby(abi)
BuildRequires:	%{?scl_prefix}rubygems-devel
# Check
BuildRequires:	%{?scl_prefix}%gem_minitest
Requires:	%{?scl_prefix}ruby(abi)
Requires:	%{?scl_prefix}ruby(rubygems)

BuildArch:	noarch
Provides:	%{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}

%description
A collection of text algorithms: Levenshtein, Soundex, Metaphone, Double
Metaphone, Figlet, Porter Stemming

%package	doc
Summary:	Documentation for %{pkg_name}
Group:	Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}
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
%{?scl:scl enable %{scl} - << \EOF}
gem install \
  --local \
  --install-dir .%{gem_dir} \
  --force \
  --rdoc \
  -V \
  %{gem_name}-%{version}.gem
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
ruby -Ilib:test:. -e 'gem "minitest", "<5" ; Dir.glob("test/*_test.rb").each{|f| require f}'
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
