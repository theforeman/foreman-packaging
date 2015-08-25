%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from addressable-2.2.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name addressable

%global rubyabi 1.9.1

Summary: URI Implementation
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.3.6
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://addressable.rubyforge.org/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Addressable is a replacement for the URI implementation that is part of
Ruby's standard library. It more closely conforms to the relevant RFCs and
adds support for IRIs and URI templates.


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
%{gem_instdir}/*
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README.md

%changelog
* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 2.3.6-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 2.3.6-1
- Update addressable to 2.3.6 (dcleal@redhat.com)

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 2.3.5-1
- Rebase to addressable 2.3.5 (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Fri Mar 29 2013 Marek Hulan <ares@igloonet.cz> 2.2.6-4
- fix for SCL

* Wed Mar 27 2013 Marek Hulan <ares@igloonet.cz> 2.2.6-3
- new package built with tito

* Mon Nov 05 2012 Miroslav Suchý <msuchy@redhat.com> 2.2.6-2
- add rubygem-addressable (msuchy@redhat.com)

* Wed Aug 10 2011 John Eckersberg <jeckersb@redhat.com> - 2.2.6-1
- Initial package
