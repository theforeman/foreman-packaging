# template: default
%global gem_name nokogiri
%global gem_require_name %{gem_name}

Name: rubygem-%{gem_name}
Version: 1.15.2
Release: 1%{?dist}
Summary: Nokogiri (鋸) makes it easy and painless to work with XML and HTML from Ruby
# MIT: see LICENSE.md
# ASL 2.0
#  1.12.0 bundles forked and modified gumbo -
#  see gumbo-parser/src/attribute.c and ext/nokogiri/gumbo.c
#  also lib/nokogiri/html5 is licensed under ASL 2.0
License:	MIT and ASL 2.0
URL: https://nokogiri.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Shut down libxml2 version unmatching warning
Patch0:	%{name}-1.11.0.rc4-shutdown-libxml2-warning.patch

Provides:	bundled(gumbo-parser) = 0.10.1

# start specfile generated dependencies
Requires: ruby >= 2.7.0
BuildRequires: ruby-devel >= 2.7.0
BuildRequires: rubygems-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies

BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel

# Prefer to consume racc as a default gem
Requires: ruby-default-gems
BuildRequires: ruby-default-gems
# CI runs rpmlint on EL7 and doesn't understand rich dependencies
%if 0%{?rhel} >= 8
Requires: (bundled(rubygem-racc) >= 1.4 with bundled(rubygem-racc) < 2)
BuildRequires: (bundled(rubygem-racc) >= 1.4 with bundled(rubygem-racc) < 2)
%endif

%description
Nokogiri parses and searches XML/HTML very quickly, and also has
correctly implemented CSS3 selector support as well as XPath support.

Nokogiri also features an Hpricot compatibility layer to help ease the change
to using correct CSS and XPath.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

# On EL8 rubygem-racc is bundled into ruby-libs package and
# auto-generated dependencies will break dependency resolution
%gemspec_remove_dep -g racc "~> 1.4"

# patches
%patch0 -p1

# remove bundled external libraries
sed -i \
	-e 's|, "ports/archives/[^"][^"]*"||g' \
	-e 's|, "ports/patches/[^"][^"]*"||g' \
	../%{gem_name}-%{version}.gemspec
# Actually not needed when using system libraries
sed -i -e '\@mini_portile@d' ../%{gem_name}-%{version}.gemspec

# Don't use mini_portile2, but build libgumbo.a first and
# tell extconf.rb the path to the archive
sed -i \
	ext/nokogiri/extconf.rb \
	-e "s@^\(def process_recipe.*\)\$@\1 ; return true@" \
	-e "s@^\(append_cppflags\).*gumbo.*\$@\1(\"-I$(pwd)/gumbo-parser/src\")@" \
	-e "\@libs.*gumbo@s@File\.join.*@\"$(pwd)/gumbo-parser/src/libgumbo.a\"@" \
	-e "\@LIBPATH.*gumbo@s|^\(.*\)\$|# \1|" \
	%{nil}

# #line directive can confuse debuginfo, removing for now
sed -i \
	gumbo-parser/src/char_ref.c \
	-e '\@^#line [0-9]@s|^\(.*\)$|// \1|'

# Compile libgumbo.a with -fPIC
sed -i \
	gumbo-parser/src/Makefile \
	-e 's|^\(CFLAGS.*=.*\)$|\1 -fPIC|'

%build
env LANG=C.UTF-8 gem build ../%{gem_name}-%{version}.gemspec

# 1.6.0 needs this
export NOKOGIRI_USE_SYSTEM_LIBRARIES=yes

%set_build_flags
# First build libgumbo.a
pushd gumbo-parser/src/
make libgumbo.a
popd

%gem_install

# Remove precompiled Java .jar file
find .%{gem_instdir}/lib/ -name '*.jar' -delete
# For now remove JRuby support
rm -rf .%{gem_instdir}/ext/java

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* \
	%{buildroot}%{gem_dir}

# Also first copy these, clean up later
cp -a ./gumbo-parser  %{buildroot}%{gem_instdir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# remove all shebang
for f in $(find %{buildroot}%{gem_instdir} -name \*.rb)
do
	sed -i -e '/^#!/d' $f
	chmod 0644 $f
done

# cleanups
# Remove bundled gumbo parser
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile* \
	dependencies.yml \
	patches \
	ports \
	gumbo-parser/Makefile
	%{nil}
find gumbo-parser/src -type f | \
	grep -v README.md | \
	xargs rm -f

%check
# Ideally, this would be something like this:
# GEM_PATH="%{buildroot}%{gem_dir}:$GEM_PATH" ruby -e "require '%{gem_name}'"
# But that fails to find native extensions on EL8, so we fake the structure that ruby expects
mkdir gem_ext_test
cp -a %{buildroot}%{gem_dir} gem_ext_test/
mkdir -p gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
cp -a %{buildroot}%{gem_extdir_mri} gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
GEM_PATH="./gem_ext_test/gems:$GEM_PATH" ruby -e "require '%{gem_name}'"
rm -rf gem_ext_test

%files
%dir %{gem_instdir}
%{_bindir}/%{gem_name}
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE-DEPENDENCIES.md
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%dir %{gem_instdir}/gumbo-parser
%doc %{gem_instdir}/gumbo-parser/CHANGES.md
%doc %{gem_instdir}/gumbo-parser/THANKS
%dir %{gem_instdir}/gumbo-parser/src
%doc %{gem_instdir}/gumbo-parser/src/README.md

%changelog
* Sun Jun 25 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.15.2-1
- Update to 1.15.2

* Sun May 21 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.15.1-1
- Update to 1.15.1

* Tue May 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.15.0-1
- Update to 1.15.0

* Sun Apr 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.14.3-1
- Update to 1.14.3

* Sun Feb 19 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.14.2-1
- Update to 1.14.2

* Sun Feb 12 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.14.1-1
- Update to 1.14.1

* Sun Jan 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.14.0-1
- Update to 1.14.0

* Sun Jan 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.13.10-1
- Update to 1.13.10

* Sun Oct 23 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.13.9-1
- Update to 1.13.9

* Wed Jul 27 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.13.8-1
- Update to 1.13.8
- Include improvements from Fedora spec file

* Tue Jul 19 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.13.7-2
- Turn on auto-requires again

* Sun Jul 17 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.13.7-1
- Update to 1.13.7

* Wed May 18 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.13.6-2
- Add back disable of Autoreq

* Fri May 13 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.13.6-1
- Release rubygem-nokogiri 1.13.6

* Thu May 27 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.11.3-2
- Do not generate auto requires due to rubygem-racc

* Fri Apr 30 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.11.3-1
- Release 1.11.3

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.10.9-2
- Rebuild against rh-ruby27

* Thu Apr 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 1.10.9-1
- Update to 1.10.9

* Thu Apr 16 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.8.4-8
- Add check section to test native library

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.8.4-7
- Bump release to build for el8

* Tue Jan 21 2020 Zach Huntington-Meath <zhunting@redhat.com> 1.8.4-6
- Bump to Obsolete the ror_52 version of Nokogiri

* Tue Jan 21 2020 Zach Huntington-Meath <zhunting@redhat.com> 1.8.4-5
- Bump to fix issue with nokogiri.so placement

* Mon Jan 20 2020 Zach Huntington-Meath <zhunting@redhat.com> 1.8.4-4
- Bump to fix issue with nokogiri.so placement

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 1.8.4-3
- Bump for moving over to foreman-packaging

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.8.4-2
- Add missing gem_docdir

* Mon Aug 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.8.4-1
- Initial package
