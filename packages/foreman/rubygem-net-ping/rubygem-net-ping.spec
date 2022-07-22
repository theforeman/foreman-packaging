# template: default
%global gem_name net-ping

Name: rubygem-%{gem_name}
Version: 2.0.8
Release: 1%{?dist}
Summary: A ping interface for Ruby
License: Artistic 2.0
URL: https://github.com/chernesk/net-ping
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.9.3
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
The net-ping library provides a ping interface for Ruby. It includes
separate TCP, HTTP, LDAP, ICMP, UDP, WMI (for Windows) and external ping
classes.


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
%exclude %{gem_instdir}/MANIFEST
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/CHANGES.out_of_date
%{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/examples
%exclude %{gem_instdir}/net-ping.gemspec
%{gem_instdir}/test

%changelog
* Fri Jul 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.0.8-1
- Update to 2.0.8

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.1-5
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.1-4
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.1-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.1-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue Jan 03 2017 Dominic Cleal <dominic@cleal.org> 2.0.1-1
- new package built with tito

