# template: default
%global gem_name ipaddress

Name: rubygem-%{gem_name}
Version: 0.8.3
Release: 4%{?dist}
Summary: IPv4/IPv6 address manipulation library
License: MIT
URL: https://github.com/bluemonk/ipaddress
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/ipaddress-gem/ipaddress/pull/86
# Integer unification on ruby2.4: ruby3.2 completely removes Fixnum
Patch0:  %{name}-pr86-ruby24-integer-unification.patch

BuildRequires: rubygem(minitest)

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
IPAddress is a Ruby library designed to make manipulation
of IPv4 and IPv6 addresses both powerful and simple. It mantains
a layer of compatibility with Ruby's own IPAddr, while
addressing many of its issues.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}
%patch -P0 -p1

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

%check
pushd .%{gem_instdir}
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.document
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rock.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/ipaddress.gemspec
%{gem_instdir}/test

%changelog
* Mon Jul 27 2026 Zach Huntington-Meath <zhunting@redhat.com> - 0.8.3-4
- Rebuild for EL10

* Sat Nov 22 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.8.3-3
- Regenerate spec file based on the current template
- Backport upstream fix for ruby3.2 Fixnum removal

* Wed May 21 2025 Zach Huntington-Meath <zhunting@redhat.com> - 0.8.3-2
- Removed unversioned obsoletes

* Tue May 31 2022 Dirk Goetz <dirk.goetz@netways.de> 0.8.3-1
- Update to 0.8.3

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.8.0-13
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.8.0-12
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.8.0-11
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.0-10
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.8.0-9
- Refresh ruby2 conversion patch to apply (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.8.0-8
- Fix build errors and modernise specs (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.8.0-7
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 22 2014 Dominic Cleal <dcleal@redhat.com> 0.8.0-6
- SCLize for EL6/7

* Fri Mar 15 2013 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-5
- Fix build breakage on >= F19 with new Ruby guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 29 2012 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-3
- Correct duplicate LICENSE file

* Thu Dec 27 2012 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-2
- Revised per review in bz#823340

* Mon Apr 30 2012 Jonas Courteau <rpms@courteau.org> - 0.8.0-1
- Initial package
- Submitted https://github.com/bluemonk/ipaddress/issues/23 upstream to remove extra file from gem
