%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name gettext_i18n_rails

Summary: Simple FastGettext Rails integration
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.5
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/grosser/gettext_i18n_rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
Requires: %{?scl_prefix}rubygem(fast_gettext) >= 0.4.8
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Translate via FastGettext, use any other I18n backend as extension/fallback.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

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
