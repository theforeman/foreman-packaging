# template: default
%global gem_name rainbow

Name: rubygem-%{gem_name}
Version: 3.1.1
Release: 1%{?dist}
Summary: Colorize printed text on ANSI terminals
License: MIT
URL: https://github.com/sickill/rainbow
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3.0
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Colorize printed text on ANSI terminals.


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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%doc %{gem_instdir}/README.markdown

%changelog
* Mon Jun 29 2026 Foreman Packaging Automation <packaging@theforeman.org> - 3.1.1-1
- Update to 3.1.1

* Wed Jun 16 2021 Odilon Sousa <osousa@redhat.com> - 2.2.2-1
- Release rubygem-rainbow 2.2.2

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.2.1-4
- Rebuild for Ruby 2.7

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.2.1-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 2.2.1-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Mon Mar 20 2017 Dominic Cleal <dominic@cleal.org> 2.2.1-1
- new package built with tito

