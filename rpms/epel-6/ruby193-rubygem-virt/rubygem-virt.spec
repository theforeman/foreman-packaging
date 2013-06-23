%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name virt

Summary: Simple to use ruby interface to libvirt
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.2.1
Release: 5%{dist}
Group: Development/Ruby
License: GPLv3+
URL: https://github.com/ohadlevy/virt
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
Requires: %{?scl_prefix}rubygem-ruby-libvirt 
BuildRequires: %{?scl_prefix}ruby 
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(virt) = %{version}

%define gembuilddir %{buildroot}%{gem_dir}

%description
Simplied interface to use ruby the libvirt ruby library


%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
%{?scl:"}
rm -rf %{buildroot}%{gem_instdir}/.yardoc

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/templates
%{gem_instdir}/LICENSE.txt
%exclude %{gem_cache}
%exclude %{gem_instdir}/Gemfile.lock
%{gem_spec}

%files doc
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/VERSION
%{gem_instdir}/README.rdoc
%{gem_instdir}/Gemfile
%{gem_instdir}/.document
%{gem_instdir}/virt.gemspec
%{gem_docdir}

%changelog
* Wed Mar 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.1-5
- put correct license in spec (msuchy@redhat.com)

* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.1-4
- new package built with tito

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.1-3
- fix BR (msuchy@redhat.com)

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.1-2
- polish the spec (msuchy@redhat.com)

* Thu Sep 06 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.1-1
- new package built with tito

