%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global	ruby_sitelib		%(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global	rubyabi	1.9.1

%global	gem_name	flexmock

# Note
# 0.8.11 seems to work only with ruby 1.8.7+
# (test fails with 1.8.6.x (i.e. F-13))

Summary:	Mock object library for ruby
Name:		%{?scl_prefix}rubygem-%{gem_name}
Version:	1.3.0
Release:	4%{?dist}
Group:		Development/Languages
License:	Copyright only
URL:		http://flexmock.rubyforge.org
Source0:	http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	%{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires:	%{?scl_prefix}rubygems-devel
BuildRequires:	%{?scl_prefix}rubygem(minitest)
BuildRequires:	%{?scl_prefix}rubygem(rake)
Requires:	%{?scl_prefix}ruby(abi) = %{rubyabi}
Requires:	%{?scl_prefix}ruby(rubygems)
Provides:	%{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}
BuildArch:	noarch
%if 0%{?fedora} >= 17
Obsoletes:	%{?scl_prefix}ruby-%{gem_name} < 0.9.0-3
%endif

%description
FlexMock is a simple, but flexible, mock object library for Ruby unit
testing.

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description	doc
This package contains documentation for %{pkg_name}.

%package	-n %{?scl_prefix}ruby-%{gem_name}
Summary:	Non-Gem support package for %{gem_name}
Group:		Development/Languages
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}
Provides:	%{?scl_prefix}ruby(%{gem_name}) = %{version}-%{release}

%description    -n %{?scl_prefix}ruby-%{gem_name}
This package provides non-Gem support for %{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T

mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install \
	--local \
	--install-dir .%{gem_dir} \
	--force --rdoc -V \
	%{SOURCE0}
%{?scl:"}

find . -name \*.rb | xargs sed -i -e '\@/usr/bin/env@d'
find . -name \*.gem -or -name \*.rb -or -name \*.rdoc | xargs chmod 0644

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
%{?scl:scl enable %{scl} "}
pushd .%{gem_instdir}
rake test_all --trace
%{?scl:"}

%files
%defattr(-,root,root,-)
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Rakefile
%exclude	%{gem_instdir}/install.rb
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files	doc
%defattr(-,root,root,-)
%{gem_instdir}/Rakefile
%{gem_instdir}/flexmock.blurb
%{gem_instdir}/doc/
%{gem_instdir}/test/
%{gem_dir}/doc/%{gem_name}-%{version}/

%changelog
* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.3.0-4
- fixing ruby193 scl package (lzap+git@redhat.com)

* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.3.0-3
- fixing ruby193 scl package (lzap+git@redhat.com)

* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.3.0-2
- new package built with tito

* Mon Feb  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.0-1
- 1.3.0

* Tue Jan  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.0-1
- 1.2.0

* Sun Nov  4 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.0-1
- 1.1.0

* Thu Oct 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.3-1
- 1.0.3

* Fri Sep 14 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.2-1
- 1.0.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 29 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.0-3
- F-17: rebuild against ruby 1.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 28 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.0-1
- 0.9.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.11-2
- Fix typo Provides on main package (bug 674413)

* Sun Oct 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.11-1
- 0.8.11

* Fri Jul 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.7-1
- 0.8.7

* Thu Jul 30 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.6-1
- Switch to gem, repackage

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 08 2007 Paul Nasrat <pauln@truemesh.com> - 0.7.1-3
- Fix repoid 

* Wed Nov 07 2007 Paul Nasrat <pauln@truemesh.com> - 0.7.1-2
- Spec cleanups in response to review
- Fix license
- strip out shebangs

* Sun Sep 09 2007 Paul Nasrat <pauln@truemesh.com> - 0.7.1-1
- Initial vesion
