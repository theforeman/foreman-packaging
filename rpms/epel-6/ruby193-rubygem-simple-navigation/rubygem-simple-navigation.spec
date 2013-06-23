%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name simple-navigation

Summary: simple-navigation is a ruby library for creating navigations (with multiple levels) for your Rails2, Rails3, Sinatra or Padrino application
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.3.4
Release: 4%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/andi/simple-navigation
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}rubygem(activesupport) >= 2.3.2
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
BuildRequires: %{?scl_prefix}rubygems-devel

%description
%{?scl:scl enable %{scl} "}
With the simple-navigation gem installed you can easily create multilevel
%{?scl:"}
navigations for your Rails, Sinatra or Padrino applications. The navigation is
defined in a single configuration file. It supports automatic as well as
explicit highlighting of the currently active navigation through regular
expressions.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}

%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%files
%{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 3.3.4-4
- new package built with tito

* Mon Jul 16 2012 Miroslav Suchý <msuchy@redhat.com> 3.3.4-3
- edit spec for fedora16 (msuchy@redhat.com)

* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 3.3.4-2
- rebuild

* Fri Jul 22 2011 Shannon Hughes <shughes@redhat.com> 3.3.4-1
- rebuild for 3.3.4 (shughes@redhat.com)

* Mon Jan 17 2011 Shannon Hughes <shughes@redhat.com> 3.1.0-1
- rebuild for 3.1.0 (shughes@redhat.com)

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 3.0.2-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 3.0.2-1
- Initial package
