# template: default
%global gem_name rb-inotify

Name: rubygem-%{gem_name}
Version: 0.11.1
Release: 1%{?dist}
Summary: A Ruby wrapper for Linux inotify, using FFI
License: MIT
URL: https://github.com/guard/rb-inotify
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A Ruby wrapper for Linux inotify, using FFI.


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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rb-inotify.gemspec
%{gem_instdir}/spec

%changelog
* Sun Jul 07 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.11.1-1
- Update to 0.11.1

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.10.1-1
- Update to 0.10.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.9.7-6
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.9.7-5
- Bump to release for EL8

* Tue Oct 01 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.9.7-4
- Update and rebuild into SCL

* Tue Sep 24 2019 Eric D. Helms <ericdhelms@gmail.com> 0.9.7-3
- Update to handle SCL building

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 0.9.7-2
- Add missing EL6 build information (ericdhelms@gmail.com)

* Fri Jul 29 2016 Dominic Cleal <dominic@cleal.org> 0.9.7-1
- new package built with tito

