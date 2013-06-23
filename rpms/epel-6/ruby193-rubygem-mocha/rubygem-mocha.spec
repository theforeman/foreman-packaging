%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name mocha

Summary:        Mocking and stubbing library
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        0.12.1
Release:        2%{?dist}
Group:          Development/Languages
License:        MIT and Ruby
URL:            http://mocha.rubyforge.org
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	%{?scl_prefix}ruby(abi) = 1.9.1
Requires:	%{?scl_prefix}ruby(rubygems)
Requires:	%{?scl_prefix}ruby
Requires:	%{?scl_prefix}rubygem(metaclass) >= 0.0.1
Requires:	%{?scl_prefix}rubygem(metaclass) < 0.1
BuildRequires:	%{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires:  %{?scl_prefix}rubygems-devel
BuildRequires:	%{?scl_prefix}ruby
BuildRequires:	%{?scl_prefix}rubygem(introspection)
BuildRequires:	%{?scl_prefix}rubygem(metaclass) >= 0.0.1
BuildRequires:	%{?scl_prefix}rubygem(metaclass) < 0.1
BuildRequires:	%{?scl_prefix}rubygem(minitest)
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Mocking and stubbing library with JMock/SchMock syntax, which allows mocking
and stubbing of methods on real (non-mock) classes.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for %{pkg_name}.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%check 
pushd %{buildroot}%{gem_instdir}
%{?scl:scl enable %scl - << \EOF}
ruby -Ilib -e "Dir.glob('./test/**/*_test.rb').each {|t| require t}"
%{?scl:EOF}
popd

%files
%exclude %{gem_instdir}/.gemtest
%exclude %{gem_instdir}/init.rb
%exclude %{gem_instdir}/mocha.gemspec
%doc %{gem_instdir}/COPYING.rdoc
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/MIT-LICENSE.rdoc
%doc %{gem_instdir}/RELEASE.rdoc
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/build-matrix.rb
%{gem_instdir}/Gemfile
%{gem_instdir}/gemfiles/*
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/test


%changelog
* Thu Feb 21 2013 Miroslav Suchý <msuchy@redhat.com> 0.12.1-2
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.12.1-1
- Update to Mocha 0.12.1.
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.10.0-4
- Rebuilt for scl.

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 0.10.0-3
- Rebuild for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 03 2011 Vít Ondruch <vondruch@redhat.com> - 0.10.0-1
- Updated to the Mocha 0.10.0.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 29 2010 Michael Stahnke <stahnma@fedoraproject.org> - 0.9.8-1
- Fixed odd naming in BR
- Updating to 0.9.8
- Breaking into -doc package as well
- Adding tests

* Thu Jul 23 2009 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 0.9.7-1
- New upstream version

* Mon Apr 27 2009 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 0.9.5-1
- New upstream version

* Sun Feb 01 2009 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 0.9.1-4
- Mark files as %%doc

* Thu Oct 30 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 0.9.1-3
- Use gem instead of tgz

* Sat Oct 25 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 0.9.1-2
- Fix license

* Sat Oct 25 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 0.9.1-1
- New upstream version
- Fix license not being marked as %%doc

* Mon Sep 08 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 0.9.0-2
- Add ruby(abi) = 1.8 requirement

* Sat Aug 23 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 0.9.0-1
- New upstream version
- Initial package for review

* Sun Jul 13 2008 root <root@oss1-repo.usersys.redhat.com> - 0.5.6-1
- Initial package
