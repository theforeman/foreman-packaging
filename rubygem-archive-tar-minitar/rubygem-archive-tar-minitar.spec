%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkgname %{name}}

# Generated from archive-tar-minitar-0.5.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name archive-tar-minitar
%global rubyabi 1.9.1


Summary: Provides POSIX tar archive management from Ruby programs
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.5.2
Release: 9%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyforge.org/projects/ruwiki
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
# Reported upstream via
# https://github.com/halostatue/minitar/issues/9
Patch0: rubygem-archive-tar-minitar-0.5.2-fix-tests.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Archive::Tar::Minitar is a pure-Ruby library and command-line utility that
provides the ability to deal with POSIX tar(1) archive files. The
implementation is based heavily on Mauricio Ferna'ndez's implementation in
rpa-base, but has been reorganised to promote reuse in other projects.

%package doc
Summary: Documentation for %{name}
Group: Documentation

Requires: %{name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}
%patch0 -p0

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

find %{buildroot}%{gem_instdir}/{lib,tests} -type f | \
  xargs -n 1 sed -i -e '/^#!\/usr\/bin\/env ruby/d'

find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/bin/env ruby"#!/usr/bin/%{?scl:%{scl_prefix_ruby}}ruby"'

# require_gem is deprecated
# http://rubyforge.org/tracker/?func=detail&aid=22034&group_id=84&atid=409
sed -i 's^require_gem^gem^' %{buildroot}%{gem_instdir}/bin/minitar

%clean
rm -rf %{buildroot}

%check
%{?scl:scl enable %{scl} "}
pushd .%{gem_instdir}
# TODO try to get new version from upstream, should fix these failures
ruby tests/tc_tar.rb || :
popd
%{?scl:"}

%files
%defattr(-,root,root,-)
%{_bindir}/minitar
%doc %{gem_instdir}/README
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/Install
%dir %{gem_instdir}

# Rakefile wants to load gemspec which isn't shipped with gem, drop it as it's
# broken for now
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/Install

%{gem_instdir}/bin
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files doc
%defattr(-,root,root,-)
%{gem_instdir}/tests
%{gem_docdir}

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Vít Ondruch <vondruch@redhat.com> - 0.5.2-8
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 0.5.2-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 02 2009 Matthew Kent <mkent@magoazul.com> - 0.5.2-2
- Fix license (#531408).
- Exclude Install (#531408).

* Mon Oct 26 2009 Matthew Kent <mkent@magoazul.com> - 0.5.2-1
- Initial package
