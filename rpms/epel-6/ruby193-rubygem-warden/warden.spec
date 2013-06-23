%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name warden

Summary: Rack middleware that provides authentication for rack applications
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.3
Release: 3%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/hassox/warden
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}rubygem(rack) >= 1.0.0
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Rack middleware that provides authentication for rack applications

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

%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.3-3
- new package built with tito

* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.3-2
- rebuild

* Fri Jan 14 2011 Shannon Hughes <shughes@redhat.com> 1.0.3-1
- rebuild for 1.0.3 gem (shughes@redhat.com)

* Thu Nov 11 2010 Shannon Hughes <shughes@redhat.com> 1.0.2-1
- new gem 1.0.2 (shughes@redhat.com)

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 1.0.1-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 1.0.1-1
- Initial package
