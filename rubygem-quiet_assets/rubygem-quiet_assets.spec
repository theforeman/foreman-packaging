%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from quiet_assets-1.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name quiet_assets
%global rubyabi 1.9.1

Summary: Turn off rails assets log
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.2
Release: 6%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/evrone/quiet_assets
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems) 
Requires: %{?scl_prefix_ruby}ruby 
Requires: %{?scl_prefix_ruby}rubygem(railties) >= 3.1
Requires: %{?scl_prefix_ruby}rubygem(railties) < 5.0
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel 
BuildRequires: %{?scl_prefix_ruby}ruby 
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Quiet assets turn off rails assets log.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

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
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/%{gem_name}.gemspec

%files doc
%doc %{gem_docdir}
%{gem_instdir}/test

%changelog
* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 1.0.2-6
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 1.0.2-5
- new package built with tito

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.2-3
- new package built with tito

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.2-2
- new package built with tito

* Wed Apr 03 2013 msuchy@redhat.com - 1.0.2-1
- Initial package
