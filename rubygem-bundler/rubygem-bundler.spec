%global gemname bundler

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

%global thorversion 0.14.6

%{!?enable_test: %global enable_test 0}

Summary: Library and utilities to manage a Ruby application's gem dependencies
Name: rubygem-%{gemname}
Version: 1.0.15
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://gembundler.com
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: rubygems
Requires: ruby(abi) = 1.8
Requires: rubygem(thor) = %{thorversion}
BuildRequires: rubygems
%if 0%{enable_test} > 0
BuildRequires: rubygem(rake)
BuildRequires: rubygem(thor) = %{thorversion}
BuildRequires: rubygem(fakeweb) = 1.3.0
BuildRequires: rubygem(builder) = 2.1.2
# Use rspec-core until rspec are not migrated to RSpec 2.x
BuildRequires: rubygem(rspec-core)
BuildRequires: git sudo
%endif
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force --rdoc %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x
rm %{buildroot}/%{geminstdir}/.gitignore

# Remove bundled Thor
rm -rf %{buildroot}/%{geminstdir}/lib/bundler/vendor

# Man pages are used by Bundler internally, do not remove them!
mkdir -p %{buildroot}%{_mandir}/man5
cp -a %{buildroot}%{geminstdir}/lib/bundler/man/gemfile.5 %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man1
for i in bundle bundle-config bundle-exec bundle-install bundle-package bundle-update 
do
        cp -a %{buildroot}%{geminstdir}/lib/bundler/man/$i %{buildroot}%{_mandir}/man1/`echo $i.1`
done

# Remove the man pages sources
rm -r %{buildroot}%{geminstdir}/man/

# Specs are still not passing. There are several reasons:
# 1) Depency on git, git needs modified global configuration settings, this
#    would mess with developer computer, requires sudo etc.
# 2) Test needs local copy of rake, fakeweb and builder gems, otherwise they
#    are installed during runtime.
# There might be other issues I am not aware of ATM.
#
# Nevertheless, specs should be possible to execute after installation.
#
%if 0%{enable_test} > 0
%check
pushd %{buildroot}%{geminstdir}
RUBYOPT="$RUBYOPT I%{gemdir}/gems/thor-%{thorversion}/lib" rspec spec/
# The test suite for 1.0.15 fails with two errors:
# https://github.com/carlhuda/bundler/issues/1290
# https://github.com/carlhuda/bundler/issues/986
# Neither of them should have impact on Bundler functionality.
rm -rf %{buildroot}%{geminstdir}/tmp/
%endif

find %{buildroot}%{geminstdir} --name .yardoc | xargs rm -f

%files
%dir %{geminstdir}
%{geminstdir}/lib
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/CHANGELOG.md
%doc %{geminstdir}/README.md
%{_bindir}/bundle
%{geminstdir}/bin
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%doc %{_mandir}/man1/*
%doc %{_mandir}/man5/*

%files doc
%defattr(-,root, root, -)
%doc %{geminstdir}/ISSUES.md
%doc %{geminstdir}/UPGRADING.md
%{geminstdir}/Rakefile
%{geminstdir}/spec
%{geminstdir}/%{gemname}.gemspec
%doc %{gemdir}/doc/%{gemname}-%{version}

%changelog
* Mon Jul 02 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.15-3
- remove hidden file .yardoc

* Mon Jul 02 2012 Miroslav Suchý <msuchy@redhat.com>
- remove hidden file .yardoc

* Thu Jul 07 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.15-1
- Updated to Bundler 1.0.15

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.10-1
- Upstream update

* Thu Jan 27 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.9-2
- More concise summary
- Do not remove manpages, they are used internally
- Added buildroot cleanup in clean section

* Mon Jan 24 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.9-1
- Bumped to Bundler 1.0.9
- Installed manual pages
- Removed obsolete buildroot cleanup

* Mon Nov 1 2010 Jozef Zigmund <jzigmund@redhat.com> - 1.0.3-2
- Add ruby(abi) dependency
- Add using macro %{geminstdir} in files section
- Add subpackage doc for doc files
- Removed .gitignore file
- Removed rubygem-thor from vendor folder
- Add dependency rubygem(thor)

* Mon Oct 18 2010 Jozef Zigmund <jzigmund@redhat.com> - 1.0.3-1
- Initial package
