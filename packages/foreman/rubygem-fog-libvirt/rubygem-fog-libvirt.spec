%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-libvirt

Summary: Module for the 'fog' gem to support libvirt
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.8.0
Release: 2%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/fog/fog-libvirt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(fog-core) >= 1.27.4
Requires: %{?scl_prefix}rubygem(fog-json)
Requires: %{?scl_prefix}rubygem(fog-xml) >= 0.1.1
Requires: %{?scl_prefix}rubygem(fog-xml) < 0.2
Requires: %{?scl_prefix}rubygem(ruby-libvirt) >= 0.7.0
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This library can be used as a module for `fog` or as standalone provider to
use the Amazon Web Services in applications.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -T -c
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.md
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/tests
%{gem_instdir}/minitests
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/%{gem_name}.gemspec

%changelog
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
