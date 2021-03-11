# Generated from ruby2ruby-2.4.2.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ruby2ruby

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.4.2
Release: 4%{?dist}
Summary: ruby2ruby provides a means of generating pure ruby code easily from RubyParser compatible Sexps
Group: Development/Languages
License: MIT
URL: https://github.com/seattlerb/ruby2ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(sexp_processor) >= 4.6
Requires: %{?scl_prefix}rubygem(sexp_processor) < 5
Requires: %{?scl_prefix}rubygem(ruby_parser) >= 3.1
Requires: %{?scl_prefix}rubygem(ruby_parser) < 4
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
ruby2ruby provides a means of generating pure ruby code easily from
RubyParser compatible Sexps. This makes making dynamic language
processors in ruby easier than ever!


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

# The first line is a shebang that isn't needed but creates a dependency
sed -i 1d bin/r2r_show

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/r2r_show
%exclude %{gem_instdir}/Manifest.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/.autotest
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.4.2-4
- Rebuild against rh-ruby27

* Sun May 17 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.4.2-3
- Drop shebang to avoid a dependency on /usr/bin/ruby

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.4.2-2
- Bump to release for EL8

* Wed Mar 13 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.4.2-1
- Update to 2.4.2-1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.4.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 19 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.4.0-1
- Updated rubygem-ruby2ruby to 2.4.0 (dmitri@appliedlogic.ca)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.1.3-5
- Final set of rebuilds (ericdhelms@gmail.com)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 2.1.3-4
- Replace shebangs to remove deps on non-SCL Ruby (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 2.1.3-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 2.1.3-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 2.1.3-1
- Update ruby2ruby to 2.1.3 (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 2.0.1-7
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 20 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.1-5
- soften requires even in gemspec (msuchy@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.1-4
- soften requires (msuchy@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.1-3
- rebase to ruby2ruby-2.0.1 (msuchy@redhat.com)

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.1-2
- add libdir macro to el6 (msuchy@redhat.com)

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.1-1
- new package built with tito

* Fri Nov 30 2012 Mo Morsi <mmorsi@redhat.com> - 2.0.1-2
- Add missing file

* Fri Nov 30 2012 Mo Morsi <mmorsi@redhat.com> - 2.0.1-1
- Update to new upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.4-6
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 1.2.4-4
- replace BR(check) w/ BR

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 29 2009 Matthew Kent <mkent@magoazul.com> - 1.2.4-2
- Move pt_testcase.rb to the build stage so it's included in the rpm (#541512).
- Drop version requirements for sexp_processor and ruby_parser as they are new
  packages (#541512).

* Mon Nov 16 2009 Matthew Kent <mkent@magoazul.com> - 1.2.4-1
- Initial package
