# template: default
%global gem_name journald-logger

Name: rubygem-%{gem_name}
Version: 3.1.0
Release: 1%{?dist}
Summary: systemd-journal native logger
License: MIT
URL: https://github.com/theforeman/journald-logger
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
systemd-journal native logger.


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
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/journald-logger.gemspec
%{gem_instdir}/spec

%changelog
* Sun Jul 24 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.1.0-1
- Update to 3.1.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.4-3
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.4-2
- Bump to release for EL8

* Thu Oct 11 2018 Lukas Zapletal <lzap+rpm@redhat.com> 2.0.4-1
- Bumped version for Ruby 2.0 support

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.3-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Feb 22 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.3-1
- new package built with tito

