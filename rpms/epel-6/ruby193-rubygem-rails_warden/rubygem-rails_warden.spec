%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name rails_warden

Summary: A gem that provides authenitcation via the Warden framework
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.5.2
Release: 5%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/hassox/rails_warden
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}rubygem(warden) >= 0
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A gem that provides authenitcation via the Warden framework

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

%doc %{gem_instdir}/LICENSE

%doc %{gem_instdir}/README.textile

%doc %{gem_instdir}/TODO

%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.5.2-5
- BR rubygems-devel (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.5.2-4
- new package built with tito

* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 0.5.2-3
- rebuild

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 0.5.2-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 0.5.2-1
- Initial package
