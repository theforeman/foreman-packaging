%{?scl:%scl_package rubygem-%{gemname}}
%{!?scl:%global pkg_name %{name}}

%global	gemname	rake-compiler
%global	gem_name	%{gemname}
%global	gemdir		%{gem_dir}
%global	geminstdir	%{gem_instdir}

%global	gemdir	%{gem_dir}
%global	gem_name	%{gemname}
%global	geminstdir	%{gem_instdir}
%global	rubyabi	1.9.1
%global	ruby19	1

Summary:	Rake-based Ruby C Extension task generator
Name:		%{?scl_prefix}rubygem-%{gemname}
Version:	0.8.3
Release:	5%{?dist}
Group:		Development/Languages
License:	MIT
URL:		http://rake-compiler.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem

BuildRequires:	%{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires:	%{?scl_prefix}ruby(rubygems) >= 1.3.5
#BuildRequires:	%{?scl_prefix}rubygem(cucumber)
#BuildRequires:	%{?scl_prefix}rubygem(isolate)
#BuildRequires:	%{?scl_prefix}rubygem(rcov)
BuildRequires:	%{?scl_prefix}rubygem(rake)
BuildRequires:	%{?scl_prefix}rubygem(rspec)
BuildRequires:	%{?scl_prefix}rubygems-devel
Requires:	%{?scl_prefix}ruby(abi) = %{rubyabi}
Requires:	%{?scl_prefix}ruby(rubygems) >= 1.3.5
Requires:	%{?scl_prefix}rubygem(rake) >= 0.8.3
BuildArch:	noarch
Provides:	%{?scl_prefix}rubygem(%{gemname}) = %{version}-%{release}

%description
rake-compiler aims to help Gem developers while dealing with
Ruby C extensions, simplifiying the code and reducing the duplication.

It follows *convention over configuration* and set an standarized
structure to build and package C extensions in your gems.

This is the result of expriences dealing with several Gems 
that required native extensions across platforms and different 
user configurations where details like portability and 
clarity of code were lacking. 

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description	doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T

mkdir -p .%{gemdir}
%{?scl:scl enable %{scl} "}
gem install \
	--local \
	--install-dir $(pwd)%{gemdir} \
	--force \
	--rdoc \
	-V \
	%{SOURCE0}
%{?scl:"}

# rpmlint cosmetic
pushd .%{geminstdir}
sed -i -e 's|\r||' README.rdoc
find ./lib/rake -name \*.rb | xargs sed -i -e '\@/usr/bin/env@d'
popd

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* %{buildroot}%{gemdir}/

# Move files under %%_bindir
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}

rmdir %{buildroot}%{gemdir}/bin

%check
pushd .%{geminstdir}

# Modify Isolate file
cp -p Isolate{,.orig}
sed -i -e 's|gem |# gem|' Isolate

# cucumber 0.10.0 needs fixing for newer rake (0.9.0 beta5)
# rake aborted!
# undefined method `desc' for #<Cucumber::Rake::Task:0xb742ebb0>
# rake spec
%{?scl:scl enable %{scl} "}
ruby -Ilib -S rspec spec/
%{?scl:"}

# back to the original
mv -f Isolate{.orig,}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/rake-compiler

%dir %{geminstdir}
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/LICENSE.txt
%doc %{geminstdir}/History.txt
%{geminstdir}/cucumber.yml

%{geminstdir}/bin/
%{geminstdir}/features/
%{geminstdir}/lib/
%{geminstdir}/tasks/

%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-,root,root,-)
%{gemdir}/doc/%{gemname}-%{version}
%{geminstdir}/Isolate
%{geminstdir}/Rakefile
%{geminstdir}/spec/

%changelog
* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 0.8.3-5
- fixing ruby193 scl package (lzap+git@redhat.com)

* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 0.8.3-4
- fixing ruby193 scl package (lzap+git@redhat.com)

* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 0.8.3-3
- fixing ruby193 scl package (lzap+git@redhat.com)

* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 0.8.3-2
- new package built with tito

* Fri Feb 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.3-1
- 0.8.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-2
- Fix BR

* Thu Jan 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-1
- 0.8.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.1-1
- 0.8.1

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.0-3
- Fix conditionals for F17 to work for RHEL 7 as well.

* Sun Jan 22 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.0-2
- Rebuild against ruby 1.9

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.0-1
- 0.8.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-3
- F-17: Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.9-2
- Kill BR: rubygem(rcov) for now

* Sat Jun 11 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.9-1
- 0.7.9
- %%check now uses rspec, not spec

* Sat Apr 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.8-1
- 0.7.8

* Mon Apr  4 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.7-1
- 0.7.7

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.6-1
- 0.7.6

* Tue Nov 30 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.5-2
- 0.7.5
- Move more files to -doc
- Now needs rubygem(isolate) and some other rubygem(foo) for BR

* Wed Aug 11 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-1
- 0.7.1

* Thu Dec 10 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.0-1
- 0.7.0

* Wed Jul 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.0-1
- 0.6.0

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.0-2
- F-12: Mass rebuild

* Thu Jul  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.0-2
- Restore files under %%{geminstdir}/bin

* Thu Jun 11 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.0-1
- Initial package
