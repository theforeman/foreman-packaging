# template: default
%global gem_name fog-libvirt

Name: rubygem-%{gem_name}
Version: 0.12.2
Release: 1%{?dist}
Summary: Module for the 'fog' gem to support libvirt
License: MIT
URL: https://github.com/fog/fog-libvirt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
This library can be used as a module for 'fog' or as standalone libvirt
provider.


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
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTORS.md
%exclude %{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/fog-libvirt.gemspec
%{gem_instdir}/minitests
%{gem_instdir}/tests

%changelog
* Fri Jul 26 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.12.2-1
- Update to 0.12.2

* Wed Nov 15 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.12.0-1
- Update to 0.12.0

* Wed Feb 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.11.0-1
- Update to 0.11.0

* Wed Jul 21 2021 Lukas Zapletal <lzap+rpm@redhat.com> 0.9.0-1
- Update to 0.9.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.8.0-2
- Rebuild against rh-ruby27

* Tue Jan 19 2021 Marek Hulan <mhulan@redhat.com> 0.8.0-1
- Update to 0.8.0

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.7.0-2
- Bump to release for EL8

* Tue Oct 29 2019 Michael Moll <mmoll@mmoll.at> 0.7.0-1
- Update to 0.7.0

* Mon Feb 04 2019 Ivan Nečas <inecas@redhat.com> 0.6.0-1
- Update to 0.6.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.4.1-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.4.1-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Aug 24 2017 Eric D. Helms <ericdhelms@gmail.com> 0.4.1-1
- update fog-libvirt 0.4.1 (kvedulv@kvedulv.de)

* Tue May 16 2017 Dominic Cleal <dominic@cleal.org> 0.4.0-1
- Update fog-libvirt to 0.4.0 (dominic@cleal.org)
- Use rubygem-ruby-libvirt on Fedora, replaces ruby-libvirt in F23+
  (dominic@cleal.org)

* Thu May 19 2016 Dominic Cleal <dominic@cleal.org> 0.2.0-1
- Update fog-libvirt to 0.2.0 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jun 16 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-1
- Update fog-libvirt to 0.0.2 (dcleal@redhat.com)

* Mon May 11 2015 Dominic Cleal <dcleal@redhat.com> 0.0.1-1
- new package built with tito
