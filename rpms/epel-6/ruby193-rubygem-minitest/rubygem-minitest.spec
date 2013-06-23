%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
# Generated from minitest-1.4.2.gem by gem2rpm -*- rpm-spec -*-
%global	gem_name minitest

%global rubyabi 1.9.1

Summary: Small and fast replacement for ruby's huge and slow test/unit
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.5.0
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubyforge.org/projects/bfts
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
minitest/unit is a small and fast replacement for ruby's huge and slow
test/unit. This is meant to be clean and easy to use both as a regular
test writer and for language implementors that need a minimal set of
methods to bootstrap a working unit test suite.

miniunit/spec is a functionally complete spec engine.

miniunit/mock, by Steven Baker, is a beautifully tiny mock object framework.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
This package contains documentation for %{pkg_name}.

%prep
%setup -q -c -T

mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gem_dir} \
  --force --rdoc \
  %{SOURCE0}
%{?scl:"}

find . -name \*gem -exec chmod 0644 {} \;

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

find %{buildroot}%{gem_instdir}/lib -type f | \
  xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/ruby.*/d'
# Ships with extremely tight permissions, bring them inline with other gems
find %{buildroot}%{gem_instdir} -type f | \
  xargs chmod 0644

rm -f %{buildroot}%{gem_instdir}/{.autotest,.gemtest}

# provide the symlink to %%ruby_libdir
mkdir %{buildroot}%{ruby_libdir}
ln -s %{gem_libdir}/%{gem_name} %{buildroot}%{ruby_libdir}/%{gem_name}

%check
pushd .%{gem_instdir}
%{?scl:scl enable %scl - << \EOF}
RUBYOPT="-Ilib:test" testrb test/minitest/*
%{?scl:EOF}

%files
%doc %{gem_instdir}/README.txt
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{ruby_libdir}/%{gem_name}

%files doc
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/design_rationale.rb
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt

%changelog
* Wed Mar 27 2013 Marek Hulan <ares@igloonet.cz> 3.5.0-2
- require ruby193-build for tagging (msuchy@redhat.com)
- update minitest to 3.5.0

* Wed Feb 20 2013 Miroslav Suchý <msuchy@redhat.com> 3.2.0-4
- new package built with tito

* Tue Jul 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.0-3
- Provide the symlink to %%{ruby_libdir}.

* Fri Jul 27 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.0-2
- Switch forgotten %%gemname for %%gem_name.

* Tue Jul 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.0-1
- Update to Minitest 3.2.0.
- Specfile cleanup.

* Fri Mar 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.10.1-2
- Rebuilt for scl.

* Sun Jan 21 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.10.1-1
- 2.10.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 10 2011 Vít Ondruch <vondruch@redhat.com> - 1.6.0-3
- Removed Rake circular dependency.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.6.0-1
- Update to 1.6.0 (#586505)
- Patch0 removed

* Sat Nov 21 2009 Matthew Kent <mkent@magoazul.com> - 1.4.2-3
- Drop Requires on hoe, only used by Rakefile (#538303).
- Move Rakefile to -doc (#538303).

* Sat Nov 21 2009 Matthew Kent <mkent@magoazul.com> - 1.4.2-2
- Better Source (#538303).
- More standard permissions on files.

* Tue Nov 17 2009 Matthew Kent <mkent@magoazul.com> - 1.4.2-1
- Initial package
