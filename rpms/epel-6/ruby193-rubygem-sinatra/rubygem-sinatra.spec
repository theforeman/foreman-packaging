%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name sinatra

%global bootstrap 0

Summary:        Ruby-based web application framework
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.3.2
Release:        15%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://sinatra.rubyforge.org
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       %{?scl_prefix}ruby(abi) = 1.9.1
Requires:       %{?scl_prefix}ruby(rubygems)
Requires:       %{?scl_prefix}rubygem(rack) >= 1.3.6
Requires:       %{?scl_prefix}rubygem(rack) < 2
Requires:       %{?scl_prefix}rubygem(rack-protection) >= 1.2
Requires:       %{?scl_prefix}rubygem(rack-protection) < 2
Requires:       %{?scl_prefix}rubygem(tilt) >= 1.3.3
Requires:       %{?scl_prefix}rubygem(tilt) < 2
BuildRequires:  %{?scl_prefix}rubygems-devel
%if 0%{bootstrap} < 1
BuildRequires:  %{?scl_prefix}rubygem(rack) >= 1.3.6
BuildRequires:  %{?scl_prefix}rubygem(rack) < 2
BuildRequires:  %{?scl_prefix}rubygem(rack-protection) >= 1.2
BuildRequires:  %{?scl_prefix}rubygem(rack-protection) < 2
BuildRequires:  %{?scl_prefix}rubygem(tilt) >= 1.3.3
BuildRequires:  %{?scl_prefix}rubygem(tilt) < 2
BuildRequires:  %{?scl_prefix}rubygem(rack-test)
BuildRequires:  %{?scl_prefix}rubygem(minitest)
%endif
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Epoch:          1

%description
Sinatra is a DSL intended for quickly creating web-applications in Ruby
with minimal effort.

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation

Requires:	%{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}
Requires:	%{?scl_prefix}ruby(rubygems)

%description	doc
This package contains documentation for %{pkg_name}.

%prep
%setup -q -c -T
%{__mkdir_p} .%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir .%{gem_dir} \
            --force -V %{SOURCE0}
%{?scl:"}

%build

%check
%if 0%{bootstrap} < 1
pushd .%{gem_instdir}
%define test_files $(find * -path 'test/*_test.rb' -not -path "test/filter_test.rb" -not -path "test/integration_test.rb" | awk '{ print "-r"$1 }')
%{?scl:scl enable %scl - << \EOF}
ruby -I. %{test_files} -e ""
%{?scl:EOF}
popd
%endif

%install
mkdir -p %{buildroot}%{gem_dir}
cp -rv .%{gem_dir}/* %{buildroot}%{gem_dir}
rm %{buildroot}/%gem_instdir/.yardopts # Remove YARD configuration

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/README.*.rdoc
%doc %{gem_instdir}/AUTHORS
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/examples
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/sinatra.gemspec
%{gem_instdir}/test

%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.2-14
- remove bootstrap (msuchy@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.2-13
- allow bootstrap (msuchy@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.2-12
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.3.2-11
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.3.2-10
- Allowed test running.

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.3.2-9
- Rebuilt for scl.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.3.2-8
- Set %%bootstrap to 0 to allow tests.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.3.2-7
- Rebuilt for Ruby 1.9.3.
- Introduced %%bootstrap macro to deal with dependency loop.

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-6
- Fixed Epoch once again

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-5
- Added Epoch to -dc subpackage

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-4
- Rebuild for missing -dc subpackage

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-3
- Added missing build requires

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-2
- Added tests
- Added doc subpackage

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-2
- Version bump

* Thu Feb 10 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.6-1
- Version bump

* Thu Feb 10 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.0-1
- Version bump

* Thu Feb 10 2011 Michal Fojtik <mfojtik@redhat.com> - 1.1.2-3
- Added tilt dependency

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Michal Fojtik <mfojtik@redhat.com> - 1.1.2-1
- Version bump

* Thu Mar 25 2010 Michal Fojtik <mfojtik@redhat.com> - 1.0-1
- Sinatra now uses Tilt for rendering templates
- New helper methods
- New argument to specify the address to bind to
- Speed improvement in rendering templates

* Thu Feb 15 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.4-2
- Downgrade-Release

* Thu Jan 07 2010 Michal Fojtik <mfojtik@redhat.com> - 0.10.1-1
- Version-Release
- Added jp README

* Fri Jun 26 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.2-3
- Get rid of duplicate files (thanks to Mamoru Tasaka)

* Mon Jun 08 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.2-2
- Fix up documentation list
- Bring tests back
- Depend on ruby(abi)
- Replace defines with globals

* Fri Jun 05 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.9.2-1
- Package generated by gem2rpm
- Don't ship tests
- Fix up License
