# template: default
%global gem_name anemone

Name: rubygem-%{gem_name}
Version: 0.7.2
Release: 24%{?dist}
Summary: Anemone web-spider framework
License: MIT
URL: https://anemone.rubyforge.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies
Requires: (rubygem(webrick) or ruby-default-gems < 3.0)

%description
Anemone web-spider framework.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/anemone
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/bin/anemone
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/VERSION
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Mon Feb 12 2024 Evgeni Golov 0.7.2-24
- Regenerate spec based on latest template

* Tue Jun 15 2021 Odilon Sousa <osousa@redhat.com> - 0.7.2-23
- align version with satellite

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.7.2-18
- Rebuild for Ruby 2.7

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.7.2-17
- Update spec to remove the ror scl

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.7.2-16
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Jan 10 2018 Eric D. Helms <ericdhelms@gmail.com> 0.7.2-15
- new package built with tito

* Wed Apr 27 2016 Justin Sherrill <jsherril@redhat.com> 0.7.2-14
- more updates for ror42 builds (jsherril@redhat.com)

* Tue Apr 26 2016 Justin Sherrill <jsherril@redhat.com> 0.7.2-13
- rebuild for ror42 scl (jsherril@redhat.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 0.7.2-12
- Build rubygem-anemone for rh22 SCL (ericdhelms@gmail.com)

* Fri Aug 28 2015 Eric D. Helms <ericdhelms@gmail.com> 0.7.2-11
- new package built with tito

* Wed May 29 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.2-10
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Mon Mar 18 2013 Lukas Zapletal <lzap+git@redhat.com> 0.7.2-8
- adding missing provide for anemone

* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 0.7.2-7
- fixing ruby193 scl package (lzap+git@redhat.com)
- require ruby193-build for tagging (msuchy@redhat.com)

* Mon Feb 25 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.2-6
- new package built with tito

* Tue Jan 29 2013 Justin Sherrill <jsherril@redhat.com> 0.7.2-5
- dropping abi requires for robotex & anemone (jsherril@redhat.com)

* Tue Jan 22 2013 Justin Sherrill <jsherril@redhat.com> 0.7.2-4
- fixing abi spec requires (jsherril@redhat.com)

* Mon Dec 03 2012 Eric D Helms <ehelms@redhat.com> 0.7.2-3
- Rubygem-anemone - Defines some common gem variables for RHEL6.
  (ehelms@redhat.com)

* Mon Dec 03 2012 Eric D Helms <ehelms@redhat.com>
- Rubygem-anemone - Defines some common gem variables for RHEL6.
  (ehelms@redhat.com)

* Fri Nov 30 2012 Justin Sherrill <jsherril@redhat.com> 0.7.2-2
- new package built with tito


* Mon Jul 16 2012 Justin Sherrill <jsherril@redhat.com>  0.7.2-1
- new package built with tito

