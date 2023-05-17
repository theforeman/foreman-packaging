# template: default
%global gem_name ruby_parser

Name: rubygem-%{gem_name}
Version: 3.20.1
Release: 1%{?dist}
Summary: A ruby parser written in pure ruby
License: MIT
URL: https://github.com/seattlerb/ruby_parser
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6
Requires: ruby < 4
BuildRequires: ruby >= 2.6
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
racc - which does by default use a C extension). It outputs
s-expressions which can be manipulated and converted back to ruby via
the ruby2ruby gem.


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
%{_bindir}/ruby_parse
%{_bindir}/ruby_parse_extract_error
%exclude %{gem_instdir}/.autotest
%exclude %{gem_instdir}/Manifest.txt
%{gem_instdir}/bin
%{gem_instdir}/compare
%exclude %{gem_instdir}/gauntlet.md
%{gem_libdir}
%{gem_instdir}/tools
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/debugging.md
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Wed May 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.20.1-1
- Update to 3.20.1

* Wed Mar 08 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.20.0-1
- Update to 3.20.0

* Sun Jan 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.19.2-1
- Update to 3.19.2

* Tue Jul 26 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.19.1-1
- Update to 3.19.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.10.1-4
- Rebuild against rh-ruby27

* Thu Apr 09 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.10.1-3
- Bump release to build for el8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.10.1-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Jan 18 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.10.1-1
- Bump up rubygem to version 3.10.1 (dmitri@appliedlogic.ca)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.6.3-5
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 3.6.3-4
- Replace shebangs to remove deps on non-SCL Ruby (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 3.6.3-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 3.6.3-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 3.6.3-1
- Update ruby_parser to 3.6.3 (dcleal@redhat.com)
- Build for Fedora 19 (dcleal@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 3.1.1-5
- fix files section (msuchy@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 3.1.1-4
- disable tests (msuchy@redhat.com)
- fix paths in SC env (msuchy@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 3.1.1-3
- fix paths in SC environment (msuchy@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 3.1.1-2
- spec2scl -i rubygem-ruby_parser.spec (msuchy@redhat.com)
- rebase to ruby_parser-3.1.1.gem from Fedora (msuchy@redhat.com)

* Tue Mar 12 2013 Vít Ondruch <vondruch@redhat.com> - 3.1.1-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to ruby_parser 3.1.1.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 29 2012 Mo Morsi <mmorsi@redhat.com> - 3.0.1-1
- Updated to new version

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.4-7
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 2.0.4-5
- replace BR(check) with BR

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 30 2009 Matthew Kent <mkent@magoazul.com> - 2.0.4-3
- Remove exclude for gauntlet_rubyparser.rb, let user deal with dependencies if
  they need it.

* Sun Nov 29 2009 Matthew Kent <mkent@magoazul.com> - 2.0.4-2
- Move pt_testcase.rb to the build stage so it's included in the rpm (#541491).
- Drop version requirements for sexp_processor as it is a new package
  (#541491).
- Exclude gauntlet_rubyparser.rb as it introduces a circular dependency
  (#541491).

* Mon Nov 16 2009 Matthew Kent <mkent@magoazul.com> - 2.0.4-1
- Initial package
