# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name git
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.11.0
Release: 2%{?dist}
Summary: An API to create, read, and manipulate Git repositories
Group: Development/Languages
License: MIT
URL: http://github.com/ruby-git/ruby-git
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: git-core

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.3
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(rchardet) >= 1.8
Requires: %{?scl_prefix}rubygem(rchardet) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.3
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
The Git Gem provides an API that can be used to create, read, and manipulate
Git repositories by wrapping system calls to the `git` binary. The API can be
used for working with Git in complex interactions including branching and
merging, object inspection and manipulation, history, patch generation and
more.


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
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.yardopts
%{gem_instdir}/ISSUE_TEMPLATE.md
%license %{gem_instdir}/LICENSE
%{gem_instdir}/MAINTAINERS.md
%{gem_instdir}/PULL_REQUEST_TEMPLATE.md
%{gem_instdir}/RELEASING.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/Dockerfile.changelog-rs
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/git.gemspec

%changelog
* Thu Mar 09 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.11.0-2
- Add dependency on git-core

* Wed May 25 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.11.0-1
- Release rubygem-git 1.11.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.5.0-2
- Rebuild for Ruby 2.7

* Fri Jan 11 2019 Marek Hulan <mhulan@redhat.com> - 1.5.0-1
- Update git to 1.5.0

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.2.5-9
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.2.5-8
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.2.5-7
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Fix build errors and modernise specs (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.2.5-6
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Mar 18 2015 Dominic Cleal <dcleal@redhat.com> 1.2.5-5
- Import and convert for SCL

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 1.2.5-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 22 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.2.5-1
- New upstream version

* Wed Oct 14 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.2.4-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 02 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.7-4
- Fix %%doc

* Mon Sep 08 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.7-3
- Add ruby(abi) = 1.8 requires (#459883, tibbs)

* Sun Sep 07 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.7-2
- Fix up comments from review (#459883, JonRob)

* Sat Aug 23 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.7-1
- Initial package for review
