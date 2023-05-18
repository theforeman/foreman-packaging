# template: default
%global gem_name git

Name: rubygem-%{gem_name}
Version: 1.18.0
Release: 1%{?dist}
Summary: An API to create, read, and manipulate Git repositories
License: MIT
URL: https://github.com/ruby-git/ruby-git
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3
BuildRequires: ruby >= 2.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
The Git Gem provides an API that can be used to create, read, and manipulate
Git repositories by wrapping system calls to the `git` binary. The API can be
used for working with Git in complex interactions including branching and
merging, object inspection and manipulation, history, patch generation and
more.


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
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.yardopts
%exclude %{gem_instdir}/ISSUE_TEMPLATE.md
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/MAINTAINERS.md
%exclude %{gem_instdir}/PULL_REQUEST_TEMPLATE.md
%exclude %{gem_instdir}/RELEASING.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%exclude %{gem_instdir}/Dockerfile.changelog-rs
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/git.gemspec

%changelog
* Thu May 18 2023 Evgeni Golov 1.18.0-1
- Update to 1.18.0

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
