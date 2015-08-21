%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hoe

Summary:    	Hoe is a simple rake/rubygems helper for project Rakefiles
Name:       	%{?scl_prefix}rubygem-%{gem_name}
Version:    	2.12.3
Release:    	6%{?dist}
Group:      	Development/Languages
License:    	MIT
URL:        	http://rubyforge.org/projects/seattlerb/
Source0:    	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Rescue Hoe.spec task when Manifest.txt
# seattlerb-Bugs-28571
Patch0:		rubygem-hoe-2.12.2-rescue-missing-Manifest.patch
# Rescue RDoc::Task when rubygem(rdoc) is not installed
Patch1:		rubygem-hoe-2.12.3-rdoctask-rescue.patch
Requires:   	%{?scl_prefix_ruby}ruby(abi) = 1.9.1
Requires:   	%{?scl_prefix_ruby}rubygems >= 1.3.6
Requires:   	%{?scl_prefix}rubygem(rubyforge) >= 2.0.4
Requires:   	%{?scl_prefix_ruby}rubygem(rake)      >= 0.8.7
#Requires:       %{?scl_prefix_ruby}rubygem(minitest)  >= 1.7.0
BuildRequires:  %{?scl_prefix_ruby}rubygems-devel >= 1.3.6
# %%check
BuildRequires:	%{?scl_prefix_ruby}rubygem(minitest)
BuildRequires:	%{?scl_prefix_ruby}rubygem(rake)
BuildRequires:	%{?scl_prefix}rubygem(rubyforge)
BuildArch:  	noarch
Provides:   	%{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps generate
rubygems and includes a dynamic plug-in system allowing for easy
extensibility. Hoe ships with plug-ins for all your usual project
tasks including rdoc generation, testing, packaging, and deployment.
Plug-ins Provided:
* Hoe::Clean
* Hoe::Debug
* Hoe::Deps
* Hoe::Flay
* Hoe::Flog
* Hoe::Inline
* Hoe::Package
* Hoe::Publish
* Hoe::RCov
* Hoe::Signing
* Hoe::Test
See class rdoc for help. Hint: ri Hoe

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description	doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install \
	--local \
	-V \
	--install-dir .%{gem_dir} \
	--force \
	--rdoc \
	%{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}
%patch0 -p0
%patch1 -p1

%build
# Allow rake 0.9
pushd .%{gem_dir}/specifications/
sed -i -e '/rake.*0\.8/s|~>|>=|' %{gem_name}-%{version}.gemspec
popd
pushd .%{gem_instdir}
sed -i -e '/rake/s|~> 0\.8|>= 0.8.7|' lib/hoe.rb

# Allow RubyInline 3.8.4
sed -i -e '/RubyInline/s|~> 3\.9|>= 3.8.4|' lib/hoe/inline.rb

popd


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

chmod 0644 %{buildroot}%{gem_dir}/cache/*gem

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gem_dir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}/%{gem_dir}/bin
find %{buildroot}/%{gem_instdir}/bin -type f | xargs chmod 0755

chmod 0755 %{buildroot}/%{gem_instdir}/template/bin/file_name.erb
# Don't remove template files
#rm -f %{buildroot}/%{gem_instdir}/template/.autotest.erb

%check
pushd .%{gem_instdir}

# Make sure that hoe currently building are loaded
export RUBYLIB=$(pwd)/lib

%{?scl:scl enable %{scl} "}
rake test -v --trace
%{?scl:"}
popd

%files
%defattr(-, root, root, -)
%{_bindir}/sow
%dir %{gem_instdir}/
%{gem_instdir}/bin/
%{gem_instdir}/lib/
%{gem_instdir}/template/
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%doc %{gem_instdir}/[A-Z]*

%files	doc
%defattr(-,root,root,-)
%{gem_instdir}/.autotest
%{gem_instdir}/.gemtest
%{gem_instdir}/test/
%{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 2.12.3-5
- run rake in SC env (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 2.12.3-4
- new package built with tito

* Tue Jul 17 2012 Miroslav Suchý <msuchy@redhat.com> 2.12.3-3
- another round of koji building for rhel 6 (lzap+git@redhat.com)

* Fri Sep  9 2011 Mamoru Tasaka <mtasaka@fedroaproject.org> - 2.12.3-1
- 2.12.3

* Sun Aug 28 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.2-1
- 2.12.2

* Thu Aug 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.0-2
- Fix glob order issue under test/

* Thu Aug 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.0-1
- 2.12.0

* Sun Jul  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.10.0-1
- 2.10.0

* Sun Jun 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.9.6-1
- 2.9.6

* Sun Apr  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.9.4-1
- 2.9.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.1-1
- 2.9.1

* Wed Feb  2 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.0-1
- 2.9.0

* Fri Dec 10 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.8.0-1
- 2.8.0

* Sat Nov 20 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.0-2
- 2.7.0

* Fri Sep 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.2-3
- Rescue Hoe.spec task when Manifest.txt is missing

* Sat Sep  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.2-2
- Kill unneeded patch

* Fri Sep  3 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.2-1
- 2.6.2
- Drop development dependency
- Split documentation files

* Sat Jun  5 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.1-1
- 2.6.1

* Thu Jun  3 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.0-3
- Use upstreamed patch for rubyforge-without-account.patch
- Fix test failure related to glob
  (build failed with Matt's mass build, also failed on koji)

* Wed Apr 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.0-1
- 2.6.0
- gemcutter dependency dropped

* Thu Mar  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.0-3
- Enable test
- Some cleanups

* Mon Feb 15 2010 Darryl L. Pierce <dpierce@redhat.com> 2.5.0-2
- Updated the dependency on rubygem-rubyforge to >= 2.0.3.

* Mon Feb 15 2010 Darryl L. Pierce <dpierce@redhat.com> 2.5.0-1
- Added dependency on rubygem-gemcutter >= 0.2.1.
- Added dependency on rubygem-minitest >= 1.4.2.
- Release 2.5.0 of Hoe.

* Sat Aug  8 2009 Darryl L. Pierce <dpierce@redhat.com> - 2.3.3-1
- Release 2.3.3 of Hoe.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul  1 2009 Darryl L. Pierce <dpierce@redhat.com> - 2.3.2-1
- Release 2.3.2 of Hoe.

* Fri Jun 26 2009 Darryl L. Pierce <dpierce@redhat.com> - 2.3.1-1
- Release 2.3.1 of Hoe.

* Thu Jun 18 2009 Darryl L. Pierce <dpierce@redhat.com> - 2.2.0-1
- Release 2.2.0 of Hoe.

* Mon Jun 15 2009 Darryl L. Pierce <dpierce@redhat.com> - 2.1.0-1
- Release 2.1.0 of Hoe.

* Wed Jun  3 2009 Darryl L. Pierce <dpierce@redhat.com> - 2.0.0-1
- Release 2.0.0 of Hoe.

* Fri Apr 17 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.12.2-1
- Release 1.12.2 of Hoe.

* Wed Apr  1 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.12.1-1
- Release 1.12.1 of Hoe.

* Tue Mar 17 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.11.0-1
- Release 1.11.0 of Hoe.

* Tue Mar 10 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.10.0-1
- Release 1.10.0 of Hoe.

* Fri Feb 27 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.9.0-1
- Release 1.9.0 of Hoe.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.8.3-1
- Release 1.8.3 of Hoe.

* Mon Oct 27 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.8.2-1
- Release 1.8.2 of Hoe.

* Thu Oct 23 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.8.1-2
- Last build failed.

* Thu Oct 23 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.8.1-1
- Release 1.8.1 of the gem.

* Mon Oct 13 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.8.0-1
- Release 1.8.0 of the gem.

* Tue Jul 01 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.7.0-1
- Release 1.7.0 of the gem.

* Wed Jun 18 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.6.0-1
- Release 1.6.0 of the gem.

* Mon Jun 09 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.3-2
- Fixed the dependency for the newer version of rubygem-rubyforge.

* Tue Jun 03 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.3-1
- New release of Hoe.

* Wed May 14 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.1-6
- Fixed the build, which failed only on devel.

* Wed May 14 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.1-5
- First official build.

* Mon May 12 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.1-4
- Update for Fedora 8 and 9.

* Tue Apr 29 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.1-3
- Fixed the license to read MIT.

* Mon Apr 28 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.1-2
- Updated the spec to comply with Ruby packaging guidelines.

* Fri Apr 18 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.1-1
- Initial package
