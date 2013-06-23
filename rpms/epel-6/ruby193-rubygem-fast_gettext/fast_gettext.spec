%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name fast_gettext

Summary: A simple, fast and threadsafe implementation of GetText
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.5.10
Release: 3%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/grosser/fast_gettext
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A simple, fast and threadsafe implementation of GetText

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


%doc %{gem_instdir}/README.markdown

%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.5.10-3
- new package built with tito

* Fri Feb 03 2012 Mike McCune <mmccune@redhat.com> 0.5.10-2
- renaming to follow convention (mmccune@redhat.com)
* Mon Jan 17 2011 Shannon Hughes <shughes@redhat.com> 0.5.10-1
- new package built with tito

* Mon Jan 17 2011 Shannon Hughes <shughes@scooby.rdu.redhat.com> - 0.5.10-1
- Initial package
