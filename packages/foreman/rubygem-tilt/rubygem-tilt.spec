# template: default
%global gem_name tilt

Name: rubygem-%{gem_name}
Version: 2.0.10
Release: 1%{?dist}
Summary: Generic interface to multiple Ruby template engines
License: MIT
URL: https://github.com/rtomayko/tilt/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Generic interface to multiple Ruby template engines.


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
%{_bindir}/tilt
%license %{gem_instdir}/COPYING
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.0.10-1
- Update to 2.0.10

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.8-5
- Rebuild against rh-ruby27

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.8-4
- Bump packages to build for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.8-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 2.0.8-2
- Bump for moving over to foreman-packaging

* Tue Aug 14 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.8-1
- Initial package
