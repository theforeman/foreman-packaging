%global gem_name virt
%if 0%{?rhel} == 6
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%endif

Summary: Simple to use ruby interface to libvirt
Name: rubygem-%{gem_name}

Version: 0.2.1
Release: 4%{dist}
Group: Development/Ruby
License: GPLv3
URL: https://github.com/ohadlevy/virt
Source0: %{gem_name}-%{version}.gem
Requires: rubygems
%if 0%{?rhel} == 6 || 0%{?fedora} < 17
Requires: ruby(abi) = 1.8
%else
Requires: ruby(abi) = 1.9.1
%endif
%if 0%{?fedora}
BuildRequires: rubygems-devel
%endif
Requires: rubygem-ruby-libvirt 
BuildRequires: ruby 
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(virt) = %{version}

%define gembuilddir %{buildroot}%{gem_dir}

%description
Simplied interface to use ruby the libvirt ruby library


%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
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
* Wed Mar 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.1-4
- put correct license in spec (msuchy@redhat.com)

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.1-3
- fix BR (msuchy@redhat.com)

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.1-2
- polish the spec (msuchy@redhat.com)

* Thu Sep 06 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.1-1
- new package built with tito

