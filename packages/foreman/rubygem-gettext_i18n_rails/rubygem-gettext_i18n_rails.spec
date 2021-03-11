%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name gettext_i18n_rails

Summary: Simple FastGettext Rails integration
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.8.0
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/grosser/gettext_i18n_rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix}rubygem(fast_gettext) >= 0.9.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Translate via FastGettext, use any other I18n backend as extension/fallback.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%doc %{gem_instdir}/MIT-LICENSE.txt
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.8.0-3
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.8.0-2
- Bump to release for EL8

* Tue Jan 08 2019 Ondřej Ezr <oezr@redhat.com> 1.8.0-1
- Update to 1.8.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.2.1-5
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.1-4
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.2.1-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.2.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Feb 24 2015 Dominic Cleal <dcleal@redhat.com> 1.2.1-1
- Update gettext_i18n_rails to 1.2.1 (dcleal@redhat.com)

* Thu Jan 08 2015 Dominic Cleal <dcleal@redhat.com> 1.2.0-1
- Update gettext_i18n_rails to 1.2.0 (dcleal@redhat.com)

* Tue Nov 25 2014 Dominic Cleal <dcleal@redhat.com> 1.0.5-1
- Modernise and update gettext_i18n_rails to 1.0.5 (dcleal@redhat.com)

* Thu Sep 12 2013 Lukas Zapletal <lzap+git@redhat.com> 0.10.0-3
- Revert "update rubygems to include wrapper BuildRequires and Requires"
  (jmontleo@redhat.com)
- update rubygems to include wrapper BuildRequires and Requires
  (jmontleo@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.10.0-2
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Mon Jun 10 2013 Dmitri Dolguikh <dmitri@redhat.com> 0.10.0-1
- updated gettext_i18n_rails gem to version 0.10.0 (dmitri@redhat.com)

* Tue May 14 2013 Dominic Cleal <dcleal@redhat.com> 0.9.4-1
- remove empty tito.props and definition which are duplicate with default from
  rel-eng/tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.13-4
- BR rubygems-devel (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.13-3
- new package built with tito

* Fri Feb 03 2012 Mike McCune <mmccune@redhat.com> 0.2.13-2
- moving to possibly a more appropriate specname (mmccune@redhat.com)

* Mon Jan 17 2011 Shannon Hughes <shughes@redhat.com> 0.2.13-1
- new package built with tito

* Mon Jan 17 2011 Shannon Hughes <shughes@scooby.rdu.redhat.com> - 0.2.13-1
- Initial package
