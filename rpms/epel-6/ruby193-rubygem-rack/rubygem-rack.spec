%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name rack

Name:           %{?scl_prefix}rubygem-%{gem_name}
Summary:        Common API for connecting web frameworks, web servers and layers of software
# Introduce Epoch (related to bug 552972)
Epoch:          1
Version:        1.4.1
Release:        5%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://rubyforge.org/projects/%{gem_name}/
Source0:        http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem

# Fixes CVE-2012-6109.
# https://bugzilla.redhat.com/show_bug.cgi?id=895277
Patch2:         rubygem-rack-1.4.2-CVE-2012-6109-Fix-parsing-performance-for-unquoted-filenames.patch

# Fixes CVE-2013-0183.
# https://bugzilla.redhat.com/show_bug.cgi?id=895282
Patch3:         rubygem-rack-1.4.3-CVE-2013-0183-avoid-unbounded-gets-method.patch

# Fixes CVE-2013-0184.
# https://bugzilla.redhat.com/show_bug.cgi?id=895384
Patch4:         rubygem-rack-1.4.4-CVE-2013-0184-Auth-scheme-fix.patch

# Fixes CVE-2013-0262.
# https://bugzilla.redhat.com/show_bug.cgi?id=909076
Patch5:         rubygem-rack-1.4.5-CVE-2013-0262-path-sanitization-information-disclosure-fix.patch

# Fixes CVE-2013-0263.
# https://bugzilla.redhat.com/show_bug.cgi?id=909071
Patch6:         rubygem-rack-1.4.5-CVE-2013-0263-secure-hmac-comparison.patch

BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       %{?scl_prefix}ruby(rubygems)
Requires:       %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires:  %{?scl_prefix}rubygems-devel
BuildRequires:  %{?scl_prefix}rubygem(bacon)
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Rack provides a common API for connecting web frameworks,
web servers and layers of software in between

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
popd

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Remove backup files
find %{buildroot}/%{gem_instdir} -type f -name "*~" -delete

# Delete zero-length files
find %{buildroot}/%{gem_instdir} -type f -size 0c -exec rm -rvf {} \;

# Fix anything executable that does not have a shebang
for file in `find %{buildroot}/%{gem_instdir} -type f -perm /a+x`; do
    [ -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 644 $file
done

# Find files with a shebang that do not have executable permissions
for file in `find %{buildroot}/%{gem_instdir} -type f ! -perm /a+x -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 755 $file
done

# Find files that have non-standard-executable-perm
find %{buildroot}/%{gem_instdir} -type f -perm /g+wx -exec chmod -v g-w {} \;

# Find files that are not readable
find %{buildroot}/%{gem_instdir} -type f ! -perm /go+r -exec chmod -v go+r {} \;

# Move %%{gem_dir}/bin/rackup to %%{_bindir}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}/%{gem_dir}/bin/rackup %{buildroot}/%{_bindir}
rm -rf %{buildroot}/%{gem_dir}/bin/

%clean
rm -rf %{buildroot}

%check
pushd %{buildroot}%{gem_instdir}
%{?scl:scl enable %scl "}
bacon --automatic --quiet
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%doc %{gem_docdir}
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/KNOWN-ISSUES
%doc %{gem_instdir}/SPEC
%doc %{gem_instdir}/example
%doc %{gem_instdir}/test
%doc %{gem_instdir}/contrib
%{gem_instdir}/%{gem_name}.gemspec
%{gem_libdir}
%{gem_instdir}/bin
%{_bindir}/rackup
%exclude %{gem_cache}
%{gem_spec}

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-5
- new package built with tito

* Mon Feb 11 2013 Josef Stribny <jstribny@redhat.com> - 1:1.4.1-4
- Fixes for CVE-2013-0262 and CVE-2013-0263.

* Tue Jan 15 2013 Vít Ondruch <vondruch@redhat.com> - 1:1.4.1-3
- Fixes for CVE-2011-6109, CVE-2013-0183 and CVE-2013-0184.

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.4.1-2
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.4.1-1
- Rebuilt for scl.
- Updated to 1.4.1.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.4.0-2
- Rebuilt for Ruby 1.9.3.

* Thu Jan 05 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.4.0-1
- Update to Rack 1.4.
- Moved gem install to %%prep to be able to apply patches.
- Applied two patches that fix test failures with Ruby 1.8.7-p357.

* Tue Jun 28 2011 Vít Ondruch <vondruch@redhat.com> - 1:1.3.0-1
- Updated to Rack 1.3.
- Fixed FTBFS.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Mar 11 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:1.1.0-2
- Epoch 1 for keeping upgrade path from F-12 (related to bug 552972)
- Enable %%check

* Mon Jan  4 2010 Jeroen van Meeuwen <kanarip@kanarip.com> - 1.1.0-1
- New upstream version

* Sun Oct 25 2009 Jeroen van Meeuwen <kanarip@kanarip.com> - 1.0.1-1
- New upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 26 2009 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.0-1
- New upstream version

* Mon Mar 16 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 0.9.1-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 09 2008 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 0.4.0-2
- Remove unused macro (#470694)
- Add ruby(abi) = 1.8 as required by package guidelines (#470694)
- Move %%{gem_dir}/bin/rackup to %%{_bindir} (#470694)

* Sat Nov 08 2008 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 0.4.0-1
- Initial package
