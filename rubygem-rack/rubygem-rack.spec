%global gem_name rack

# There is circular dependency between thin and rack.
%global bootstrap_thin 0
%{!?enable_test: %global enable_test 0}

Name:           rubygem-%{gem_name}
Summary:        Common API for connecting web frameworks, web servers and layers of software
# Introduce Epoch (related to bug 552972)
Epoch:          1
Version:        1.4.5
Release:        3%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://rubyforge.org/projects/%{gem_name}/
Source0:        http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
# Fix test suite for Ruby 2.0
# https://github.com/rack/rack/commit/0a74380d2e5157d94c7e9141242af33e5c0bf951
Patch0:         rubygem-rack-1.5.0-Fix-Ruby-2.0-build.patch
Requires:       ruby(rubygems)
Requires:       ruby(release)
BuildRequires:  ruby
BuildRequires:  rubygems-devel
%if 0%{enable_test} > 0
BuildRequires:  rubygem(bacon)
BuildRequires:  memcached
BuildRequires:  rubygem(memcache-client)
%if 0%{bootstrap_thin} < 1
BuildRequires:  rubygem(thin)
%endif
%endif
# Seems that lighttpd test depends on rubygem(fcgi), which is not in Fedora,
# if it will ever be.
# BuildRequires:  lighttpd-fastcgi
BuildArch:      noarch
Provides:       rubygem(%{gem_name}) = %{version}

%description
Rack provides a common API for connecting web frameworks,
web servers and layers of software in between


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Fix anything executable that does not have a shebang
for file in `find %{buildroot}/%{gem_instdir} -type f -perm /a+x`; do
    [ -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 644 $file
done

# Find files with a shebang that do not have executable permissions
for file in `find %{buildroot}%{gem_instdir} -type f`; do
    [ ! -z "`head -n 1 $file | grep \"^#!\"`" ] && chmod -v 755 $file
done

%if 0%{enable_test} > 0
%check
pushd .%{gem_instdir}

# Get temporary PID file name and start memcached daemon.
PID=%(mktemp)
memcached -d -P "$PID"

bacon --automatic --quiet

# Kill memcached daemon.
kill -TERM $(< "$PID")

popd
%endif

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/COPYING
%{gem_libdir}
%{gem_instdir}/bin
%{_bindir}/rackup
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/KNOWN-ISSUES
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Rakefile
%{gem_instdir}/SPEC
%doc %{gem_instdir}/example
%{gem_instdir}/test
%doc %{gem_instdir}/contrib


%changelog
* Fri Mar 01 2013 Vít Ondruch <vondruch@redhat.com> - 1:1.4.5-3
- Enable thin test suite.

* Mon Feb 25 2013 Vít Ondruch <vondruch@redhat.com> - 1:1.4.5-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Fri Feb 08 2013 Josef Stribny <jstribny@redhat.com> - 1:1.4.5-1
- Update to Rack 1.4.5.

* Tue Jan 15 2013 Vít Ondruch <vondruch@redhat.com> - 1:1.4.4-1
- Update to Rack 1.4.4.

* Thu Nov 01 2012 Vít Ondruch <vondruch@redhat.com> - 1:1.4.1-2
- Fixed epoch in -doc sub-package.

* Mon Oct 29 2012 Vít Ondruch <vondruch@redhat.com> - 1:1.4.1-1
- Update to Rack 1.4.1.
- Documentation moved into subpackage.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

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
