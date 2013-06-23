%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}
%define gem_name compass-960-plugin

Summary: Compass compatible Sass port of 960.gs
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.10.4
Release: 4%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/chriseppstein/compass-960-plugin
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}rubygem(compass) >= 0.10.0
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
The 960 Grid System is an effort to streamline web development workflow by
providing commonly used dimensions, based on a width of 960 pixels.
http://960.gs/

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
* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.10.4-4
- new package built with tito

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.10.4-3
- new package built with tito

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.10.4-2
- new package built with tito

* Mon Jul 25 2011 Shannon Hughes <shughes@redhat.com> 0.10.4-1
- updating to 0.10.4 (shughes@redhat.com)

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 0.10.0-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 0.10.0-1
- Initial package
