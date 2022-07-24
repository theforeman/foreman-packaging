# template: default
%global gem_name logging-journald

Name: rubygem-%{gem_name}
Version: 2.1.0
Release: 1%{?dist}
Summary: Journald appender for logging gem
License: MIT
URL: https://github.com/lzap/logging-journald
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.0.0
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Plugin for logging gem providing journald appender.


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
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%exclude %{gem_instdir}/logging-journald.gemspec
%{gem_instdir}/test

%changelog
* Sun Jul 24 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.1.0-1
- Update to 2.1.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.0-3
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.0-2
- Bump to release for EL8

* Fri Oct 12 2018 Lukas Zapletal <lzap+rpm@redhat.com> 2.0.0-1
- Upstream version 2.0.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Feb 20 2018 Daniel Lobato Garcia <me@daniellobato.me> 1.0.0-1
- new package built with tito

