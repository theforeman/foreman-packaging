# template: default
%global gem_name safemode

Name: rubygem-%{gem_name}
Version: 1.4.0
Release: 1%{?dist}
Summary: A library for safe evaluation of Ruby code based on ParseTree/RubyParser and Ruby2Ruby
License: MIT
URL: https://github.com/svenfuchs/safemode
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7
Requires: ruby < 3.1
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 3.1
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A library for safe evaluation of Ruby code based on RubyParser and Ruby2Ruby.
Provides Rails ActionView template handlers for ERB and Haml.


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

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/demo.rb
%{gem_instdir}/init.rb
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/safemode.gemspec
%{gem_instdir}/test

%changelog
* Thu Dec 14 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.4.0-1
- Update to 1.4.0

* Tue Jul 11 2023 Oleh Fedorenko <ofedoren@redhat.com> 1.3.8-1
- Update to 1.3.8

* Tue May 17 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.3.7-1
- Release rubygem-safemode 1.3.7

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.3.6-2
- Rebuild against rh-ruby27

* Mon Aug 31 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.6-1
- Update to 1.3.6
- Regenerate spec file based on the latest template

* Tue Jul 14 2020 Dirk Goetz <dirk.goetz@netways.de> - 1.3.5-4
- Add patch to allow to_sentence for array

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.3.5-3
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.3.5-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon Apr 16 2018 Dmitri Dolguikh <dmitri@appliedlogic.ca> 1.3.5-1
- Update to 1.3.5

* Fri Jan 19 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.4-1
- Update rubygem-safemode to 1.3.4 (dmitri@appliedlogic.ca)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.2-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Update safemode to 1.3.2 (tbrisker@gmail.com)

* Mon Feb 13 2017 Dominic Cleal <dominic@cleal.org> 1.3.1-1
- Update safemode to 1.3.1 (dominic@cleal.org)

* Wed Jan 25 2017 Dominic Cleal <dominic@cleal.org> 1.2.5-1
- Update rubygem-safemode to 1.2.5 (dmitri@appliedlogic.ca)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 1.2.4-2
- Use gem_install macro (dominic@cleal.org)

* Fri Apr 15 2016 Dominic Cleal <dominic@cleal.org> 1.2.4-1
- Update safemode to 1.2.4 (dominic@cleal.org)

* Wed Mar 09 2016 Dominic Cleal <dominic@cleal.org> 1.2.3-1
- Update safemode to 1.2.3 (mhulan@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.2.2-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.2.2-2
- Converted to tfm SCL (dcleal@redhat.com)
- Fixes #9703 - change %%{dist} to %%{?dist} (jmontleo@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 1.2.2-1
- Update safemode to 1.2.2 (dcleal@redhat.com)

* Wed Jul 30 2014 Dominic Cleal <dcleal@redhat.com> 1.2.1-1
- Update to v1.2.1 (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 1.2.0-5
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- remove unused BRs (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 1.2.0-3
- new package built with tito

* Wed Feb 20 2013 Lukas Zapletal <lzap+git@redhat.com> 1.2.0-2
- safemode 1.2

* Wed Feb 20 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.2.0-1
- new version

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.0-2
- require correct version of gems -namely ruby2ruby (msuchy@redhat.com)

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.0-1
- rebase to safemode-1.1.0.gem (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-6
- fix sed expression (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-5
- it should work even with older rdoc (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-4
- fix build requires (msuchy@redhat.com)

* Thu Aug 09 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-3
- fix filelist (msuchy@redhat.com)

* Thu Aug 09 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-2
- new package built with tito
