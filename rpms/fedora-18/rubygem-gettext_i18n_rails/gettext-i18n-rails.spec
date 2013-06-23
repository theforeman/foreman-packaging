%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name gettext_i18n_rails

Summary: Simple FastGettext Rails integration
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.10.0 
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/grosser/gettext_i18n_rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}rubygem(fast_gettext) >= 0.4.8
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Simple FastGettext Rails integration.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}

%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)

%{gem_dir}/gems/%{gem_name}-%{version}/

%doc %{gem_dir}/doc/%{gem_name}-%{version}


%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
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
