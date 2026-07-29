# template: default
%global gem_name kafo_wizards

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 2%{?dist}
Summary: Wizard like interfaces in terminal
License: GPLv3+
URL: https://github.com/theforeman/kafo_wizards
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7
Requires: ruby < 5
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 5
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
This gem helps to create wizard like interfaces in terminal applications, has
support for nesting and value validation.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%gemspec_remove_dep -g logger

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
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Wed Jul 29 2026 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.0-2
- Rebuild for EL10

* Tue Feb 17 2026 Ondřej Gajdušek <ogajduse@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.2-2
- Rebuild for Ruby 2.7

* Fri Dec 11 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.0.2-1
- Release rubygem-kafo_wizards 0.0.2

* Fri Apr 03 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.0.1-4
- Obsolete non-scl version

* Thu Apr 02 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.0.1-3
- Build for SCL

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.0.1-2
- Use gem_install macro (dominic@cleal.org)

* Tue Jan 26 2016 Dominic Cleal <dcleal@redhat.com> 0.0.1-1
- new package built with tito

