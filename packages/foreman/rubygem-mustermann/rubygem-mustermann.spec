# template: default
%global gem_name mustermann

Name: rubygem-%{gem_name}
Version: 2.0.2
Release: 1%{?dist}
Summary: Your personal string matching expert
License: MIT
URL: https://github.com/sinatra/mustermann
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.2.0
BuildRequires: ruby >= 2.2.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A library implementing patterns that behave like regular expressions.


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
%{gem_instdir}/bench
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/mustermann.gemspec
%{gem_instdir}/spec

%changelog
* Mon Aug 01 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.2-1
- Update to 2.0.2

* Wed May 05 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.1.1-1
- Update to 1.1.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.2-5
- Rebuild against rh-ruby27

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.2-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.2-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 1.0.2-2
- Bump for moving over to foreman-packaging

* Tue Aug 14 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.2-1
- Initial package
