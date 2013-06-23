%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name maruku

%define rubyabi 1.9.1

Name: %{?scl_prefix}rubygem-%{gem_name}
Summary: Maruku is a Markdown-superset interpreter written in Ruby
Version: 0.6.0
Release: 9%{?dist}
Group: Development/Languages
License: GPLv2+
URL: http://maruku.rubyforge.org

Source0: http://gemcutter.org/downloads/%{gem_name}-%{version}.gem
Patch0:  remove_deprecated_method.patch
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(syntax) >= 1.0.0
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(rake)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Maruku is a Markdown interpreter in Ruby. It features native export to HTML
and PDF (via Latex). The output is really beautiful!


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p ./%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install \
  --local \
  --install-dir $(pwd)/%{gem_dir} \
  --force --no-ri --rdoc \
  %{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}
%patch0 -p0

# fixes rpmlint warning about file-not-utf8
# http://fedoraproject.org/wiki/Common_Rpmlint_issues#file-not-utf8
iconv -f iso8859-1 -t utf-8 tests/unittest/lists10.md > list10.md.conv && mv -f list10.md.conv tests/unittest/lists10.md

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}/%{_bindir}

cp -a ./%{gem_dir}/* %{buildroot}/%{gem_dir}/.
mv %{buildroot}%{gem_dir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gem_dir}/bin
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
RUBYOPT=-I. rake test || :
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/maruku
%{_bindir}/marutex
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}

%{gem_cache}
%{gem_spec}

%doc %{gem_instdir}/docs
%doc %{gem_instdir}/tests
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/maruku_gem.rb
%doc %{gem_instdir}/*.sh
%doc %{gem_docdir}

%changelog
* Fri Mar 15 2013 Lukas Zapletal <lzap+git@redhat.com> 0.6.0-9
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.6.0-7
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 0.6.0-5
- Replace BR(check) with BR

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 23 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.6.0-3
- added geminstdir to file list
- added rubygem(rake) dependency
- other fixes to conform to package guidelines

* Mon Feb 08 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.6.0-2
- cleaned up macros, other package guideline compliance fixes
- corrected license
- include all files and docs, added check/test section

* Mon Feb 08 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.6.0-1
- Initial package
