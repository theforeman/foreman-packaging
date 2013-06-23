%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rbovirt

Summary: A Ruby client for oVirt REST API
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.0.20
Release: 1%{dist}
Group: Development/Ruby
License: MIT
URL: http://github.com/abenari/rbovirt
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
Requires: %{?scl_prefix}rubygem-nokogiri 

Requires: %{?scl_prefix}rubygem-rest-client 
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(rbovirt) = %{version}

%define gembuilddir %{buildroot}%{gem_dir}

%description
A Ruby client for oVirt REST API

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
rm -f %{buildroot}%{gem_instdir}/.document
rm -rf %{buildroot}%{gem_instdir}/.yardoc

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.txt
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Gemfile
%{gem_instdir}/spec
%{gem_instdir}/Rakefile
%{gem_instdir}/VERSION
%{gem_instdir}/rbovirt.gemspec
%doc %{gem_docdir}

%changelog
* Thu May 23 2013 Dominic Cleal <dcleal@redhat.com> 0.0.20-1
- rebase to rbovirt-0.0.20.gem (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.16-3
- put correct license in spec (msuchy@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.16-2
- rebase to rbovirt-0.0.16.gem (msuchy@redhat.com)

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.16-1
- rebase to rbovirt-0.0.16.gem (msuchy@redhat.com)

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.12-2
- polish the spec (msuchy@redhat.com)

* Thu Sep 06 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.12-1
- new package built with tito

