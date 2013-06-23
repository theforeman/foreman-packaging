%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name thin
%global rubyabi 1.9.1

Summary: A thin and fast web server
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.1
Release: 7%{?dist}
Group: Development/Languages
License: (GPLv2 or Ruby) and BSD and MIT
URL: http://code.macournoyer.com/thin/
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-thin-fix-parser-load-path.patch
# https://github.com/macournoyer/thin/issues/77
Patch1: rubygem-thin-remove-rspec1-require.patch
Patch2: rubygem-thin-rspec2-null-object.patch
# https://github.com/macournoyer/thin/issues/76
Patch3: rubygem-thin-fix-install-spec.patch
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(rack) >= 1.0.0
Requires: %{?scl_prefix}rubygem(eventmachine) >= 0.12.6
Requires: %{?scl_prefix}rubygem(daemons) >= 1.0.9
Requires: curl
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: curl
BuildRequires: libcurl-devel
BuildRequires: %{?scl_prefix}rubygem(rake-compiler)
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildRequires: %{?scl_prefix}rubygem(eventmachine) >= 0.12.6
BuildRequires: %{?scl_prefix}rubygem(daemons) >= 1.0.9
BuildRequires: %{?scl_prefix}rubygem(rack) >= 1.0.0
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Thin is a Ruby web server that glues together three of the best Ruby
libraries in web history.
The Mongrel parser, the root of Mongrel speed and security,
Event Machine, a network I/O library with extremely high scalability and
Rack, a minimal interface between webservers and Ruby frameworks.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p ./%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %{scl} "}
gem install --local --install-dir ./%{gem_dir} -V --force %{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_vendorarchdir}/%{gem_name}
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_prefix}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}
mv -f %{buildroot}%{gem_libdir}/*.so %{buildroot}%{ruby_vendorarchdir}/
mv -f %{buildroot}%{gem_dir}/bin %{buildroot}%{_prefix}
for f in $(find %{buildroot}%{gem_instdir} -name \*.rb); do
  sed -i -e '/^#!/d' $f
  chmod 0644 $f
done
find %{buildroot}%{gem_instdir} -type f -exec sed -i 's/^#!\/usr\/local\/bin\/ruby/#!\/usr\/bin\/ruby/g' {} \;
chmod +x %{buildroot}%{gem_libdir}/thin/controllers/service.sh.erb
rm -rf %{buildroot}%{gem_instdir}/{ext,tmp}/
rm -f %{buildroot}%{gem_instdir}/{.autotest,.require_paths}

%check
# https://bugzilla.redhat.com/show_bug.cgi?id=566401
%ifarch ppc64
exit 0
%endif
pushd .%{gem_instdir}

# Depends on rubygem-benchmark_unit, not available in Fedora yet.
rm -rf spec/perf
# Test fails.
# https://github.com/macournoyer/thin/issues/40
rm spec/server/pipelining_spec.rb
# The 'should force kill process in pid file' spec is not compatible with RSpec2.
# https://github.com/rspec/rspec-core/issues/520
# http://rubyforge.org/tracker/?func=detail&aid=29450&group_id=524&atid=2086
%{?scl:scl enable %{scl} '}
ruby -ne "print unless (99..117).include? $." spec/daemonizing_spec.rb > spec/daemonizing_spec.rb
%{?scl:'}

%{?scl:scl enable %{scl} "}
rspec spec
%{?scl:"}

popd

%files
%{_bindir}/%{gem_name}
%{ruby_vendorarchdir}/thin_parser.so
%dir %{gem_instdir}/
%{gem_instdir}/bin/
%dir %{gem_libdir}
%{gem_libdir}/thin.rb
%{gem_libdir}/rack/
%dir %{gem_libdir}/thin/
%{gem_libdir}/thin/*.rb
%{gem_libdir}/thin/backends/
%{gem_libdir}/thin/controllers/
%{gem_cache}
%{gem_spec}
# BSD
%{gem_libdir}/thin/stats.html.erb

%files doc
%{gem_docdir}
%{gem_instdir}/benchmark/
%{gem_instdir}/tasks/
%{gem_instdir}/example/
%{gem_instdir}/CHANGELOG
%{gem_instdir}/README
%{gem_instdir}/Rakefile
%dir %{gem_instdir}/spec/
%{gem_instdir}/spec/backends/
%{gem_instdir}/spec/*.rb
%{gem_instdir}/spec/configs/
%{gem_instdir}/spec/controllers/
%{gem_instdir}/spec/perf/
%{gem_instdir}/spec/rack/
%{gem_instdir}/spec/request/
%{gem_instdir}/spec/server/
%dir %{gem_instdir}/spec/rails_app/
%{gem_instdir}/spec/rails_app/app/
%{gem_instdir}/spec/rails_app/config/
%{gem_instdir}/spec/rails_app/script/
# MIT
%{gem_instdir}/spec/rails_app/public/

%changelog
* Mon Mar 18 2013 Lukas Zapletal <lzap+git@redhat.com> 1.3.1-7
- fixing a scl rubygem

* Tue Mar 12 2013 Lukas Zapletal <lzap+git@redhat.com> 1.3.1-6
- fixing ruby193 scl package (lzap+git@redhat.com)

* Tue Mar 12 2013 Lukas Zapletal <lzap+git@redhat.com> 1.3.1-5
- converted rubygem-thin to ruby193-rubygem-thin (lzap+git@redhat.com)
- import rubygem-thin from Fedora (lzap+git@redhat.com)
- removing thin and em - will re-import F18 version (lzap+git@redhat.com)
- review of ruby193-rubygem-thin (lzap+git@redhat.com)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Vít Ondruch <vondruch@redhat.com> - 1.3.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.1-1
- Update to Thin 1.3.1.

* Tue Sep 06 2011 Chris Lalancette <clalance@redhat.com> - 1.2.11-10
- Bump the release so upgrades from F-16 work

* Mon Jul 25 2011 Chris Lalancette <clalance@redhat.com> - 1.2.11-3
- Move stats.html.erb to the main package (it is a runtime requirement)

* Fri Jul 22 2011 Chris Lalancette <clalance@redhat.com> - 1.2.11-2
- Fix the load path for thin_parser

* Tue Mar 01 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.11-1
- Version bump

* Tue Mar 01 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.8-3
- Removed Rake dependency completely

* Tue Mar 01 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.8-2
- Fixed RSpec tests

* Tue Mar 01 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.8-1
- Updated to upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 08 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.7-1
- Updated to upstream version

* Tue Feb 04 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-5
- Excluded ppc64 in tests (566401)
- Fixed Licensing

* Tue Feb 03 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-4
- Added rspec tests
- Fixed unwanted recompilation
- Fixed licensing

* Tue Feb 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-3
- Fixed description

* Tue Feb 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-2
- Build fixed
- Licence corrected
- Added missing requires
- Marked relevant files as documentation

* Tue Feb 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-1
- Initial package


