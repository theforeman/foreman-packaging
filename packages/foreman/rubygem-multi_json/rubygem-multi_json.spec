# template: default
%global gem_name multi_json

Name: rubygem-%{gem_name}
Version: 1.15.0
Release: 1%{?dist}
Summary: A common interface to multiple JSON libraries
License: MIT
URL: https://github.com/intridea/multi_json
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel >= 1.3.5
BuildArch: noarch
# end specfile generated dependencies

%description
A common interface to multiple JSON libraries, including Oj, Yajl, the JSON
gem (with C-extensions), the pure-Ruby JSON gem, NSJSONSerialization, gson.rb,
JrJackson, and OkJson.


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
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.15.0-1
- Update to 1.15.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.14.1-3
- Rebuild against rh-ruby27

* Thu May 28 2020 Evgeni Golov 1.14.1-2
- Only obsolete the ror52 SCL version in the tfm SCL build

* Wed May 27 2020 Evgeni Golov 1.14.1-1
- Update to 1.14.1

* Thu Mar 26 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.12.2-6
- Rebuild for EL8

* Wed Jan 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.12.2-5
- Obsolete the rails scl version for moving rails to foreman-packaging

* Wed Jan 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.12.2-4
- Rebuild not in the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.12.2-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.12.2-2
- Final set of rebuilds (ericdhelms@gmail.com)

* Wed Sep 27 2017 Daniel Lobato Garcia <me@daniellobato.me> 1.12.2-1
- Fixes #20960 - update activerecord-session_store to 1.1.0
  (kvedulv@kvedulv.de)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.10.1-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.10.1-2
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 1.10.1-1
- Update multi_json to 1.10.1 (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 1.8.2-2
- Modernise and update for EL7 (dcleal@redhat.com)

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 1.8.2-1
- Rebase to multi_json 1.8.2 (dcleal@redhat.com)

* Wed Aug 21 2013 Dominic Cleal <dcleal@redhat.com> 1.3.6-11
- Don't override gem macros when building under SCL (dcleal@redhat.com)

* Tue Aug 20 2013 Dominic Cleal <dcleal@redhat.com> 1.3.6-10
- fix dependency on ruby(abi) for ruby193 SCL builds (dcleal@redhat.com)

* Fri Aug 16 2013 Sam Kottler <shk@redhat.com> 1.3.6-9
- Rebuild for proper version dependencies

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 1.3.6-8
- Removed rubygems version requirement (shk@redhat.com)

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 1.3.6-7
- Corrected the abi logic (shk@redhat.com)
- Ensure the right ruby(abi) is used on F18 (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.3.6-6
- Fix another conditional (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.3.6-5
- Fix conditional (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.3.6-4
- Modernize the gemspec for SCL and non-SCL (shk@redhat.com)
- remove empty tito.props and definition which are duplicate with default from
  rel-eng/tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.6-2
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.6-1
- Updated to Multi_Json 1.3.6.
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-1
- Rebuilt for scl.
- Updated to 1.2.0.

* Tue Jan 24 2012 Vít Ondruch <vondruch@redhat.com> - 1.0.3-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.3-3
- Removed useless shebang.

* Fri Nov 11 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.3-2
- Review fixes.

* Fri Jul 08 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.3-1
- Initial package
