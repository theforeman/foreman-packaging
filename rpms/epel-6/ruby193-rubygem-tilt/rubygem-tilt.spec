%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name tilt

%global rubyabi 1.9.1
%global bootstrap 0

Summary: Generic interface to multiple Ruby template engines
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.3
Release: 9%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/rtomayko/%{gem_name}
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/rtomayko/tilt/commit/ff097e8722056dfef6ac4523d406bdbca6eae87d#test/tilt_rdoctemplate_test.rb
Patch0: tilt-rdoc-test.patch
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
# comment out the packages that are not in the scl
%if 0%{bootstrap} < 1
BuildRequires: %{?scl_prefix}rubygem(minitest)
#BuildRequires: %{?scl_prefix}rubygem(nokogiri)
BuildRequires: %{?scl_prefix}rubygem(erubis)
#BuildRequires: %{?scl_prefix}rubygem(haml)
BuildRequires: %{?scl_prefix}rubygem(builder)
#BuildRequires: %{?scl_prefix}rubygem(RedCloth)
%endif

# Markaby test fails. It is probably due to rather old version found in Fedora.
# https://github.com/rtomayko/tilt/issues/96
# BuildRequires: %{?scl_prefix}rubygem(markaby)

# RDiscount test fails. Is it due to old version in Fedora?
# BuildRequires: %{?scl_prefix}rubygem(rdiscount)

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Generic interface to multiple Ruby template engines


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
%if 0%{bootstrap} < 1
pushd %{buildroot}%{gem_instdir}
%{?scl:scl enable %scl - << \EOF}
RUBYOPT="-rrdoc" LANG=en_US.utf8 testrb -Ilib test/*_test.rb
%{?scl:EOF}
popd
%endif

%files
%{_bindir}/%{gem_name}
%exclude %{gem_instdir}/%{gem_name}.gemspec
%if "%{bootstrap}" == "0"
#%exclude %{gem_instdir}/.sass-cache
#%exclude %{gem_instdir}/.yardoc
%endif
%exclude %{gem_instdir}/Gemfile
%{gem_instdir}/bin
%{gem_libdir}
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/TEMPLATES.md
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/Rakefile
%doc %{gem_docdir}
%{gem_instdir}/test


%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.3-9
- new package built with tito

* Tue Jul 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-8
- Exclude the cached gem.

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-7
- Specfile cleanup

* Thu May 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-6
- Fix the rdoc test patch to apply cleanly.

* Thu Apr 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-5
- Fix the rdoc template tests.

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-4
- Rebuilt for scl.

* Fri Feb 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-3
- Allowed running the tests.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-2
- Rebuilt for Ruby 1.9.3.
- Introduced %%bootstrap macro to deal with dependency loop for BuildRequires.

* Mon Jan 16 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-1
- Updated to tilt 1.3.3.
- Removed patch that fixed BZ #715713, as it is a part of this version.
- Excluded unnecessary files.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.2-1
- Updated to the tilt 1.3.2.
- Test suite for erubis, haml, builder and RedCloth template engines enabled.

* Fri Jun 24 2011 Vít Ondruch <vondruch@redhat.com> - 1.2.2-3
- Fixes FTBFS (rhbz#715713).

* Thu Feb 10 2011 Vít Ondruch <vondruch@redhat.com> - 1.2.2-2
- Test moved to doc subpackage
- %{gem_name} macro used whenever possible.

* Mon Feb 07 2011 Vít Ondruch <vondruch@redhat.com> - 1.2.2-1
- Initial package
