%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name oauth

Summary: OAuth Core Ruby implementation
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.7
Release: 7%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubydoc.info/gems/oauth
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
%if 0%{?el6} && 0%{!?scl:1}
Requires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems-devel

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
OAuth Core Ruby implementation

%prep
%setup -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

%files
%{_bindir}/oauth
%{gem_instdir}
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/TODO
%{gem_cache}
%{gem_spec}

%changelog
* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.4.7-7
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 0.4.7-6
- Modernise and update for EL7 (dcleal@redhat.com)

* Wed Jul 03 2013 Lukas Zapletal <lzap+git@redhat.com> 0.4.7-5
- rubygem-oauth works for non-SCL as well (lzap+git@redhat.com)
- remove empty tito.props and definition which are duplicate with default from
  rel-eng/tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.7-3
- new package built with tito

* Thu Nov 08 2012 Miroslav Suchý <msuchy@redhat.com> 0.4.7-2
- fixing requires and buildrequires for F17 (msuchy@redhat.com)

* Tue Nov 06 2012 Ivan Necas <inecas@redhat.com> 0.4.7-1
- rebase so 0.4.7

* Fri Jan 14 2011 Shannon Hughes <shughes@redhat.com> 0.4.4-1
- new package built with tito

* Fri Jan 14 2011 Shannon Hughes <shughes@redhat.com> - 0.4.4-1
- Initial package
