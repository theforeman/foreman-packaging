# template: default
%global gem_name multipart-post

Name: rubygem-%{gem_name}
Version: 2.2.3
Release: 1%{?dist}
Summary: A multipart form post accessory for Net::HTTP
License: MIT
URL: https://github.com/socketry/multipart-post
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3.0
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A multipart form post accessory for Net::HTTP.


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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Fri Jul 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.2.3-1
- Update to 2.2.3

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.0-3
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.0-2
- Bump to release for EL8

* Thu Mar 14 2019 kgaikwad <kavitagaikwad103@gmail.com> 2.0.0-1
- Update to 2.0.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.2.0-6
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.0-5
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.2.0-4
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.2.0-3
- Converted to tfm SCL (dcleal@redhat.com)

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 1.2.0-2
- Fix missing .gem (dcleal@redhat.com)

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 1.2.0-1
- new package built with tito
