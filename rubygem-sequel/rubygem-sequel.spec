%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name sequel

Summary: The Database Toolkit for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.20.0
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://sequel.jeremyevans.net
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby

%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
Requires: %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif

BuildRequires: %{?scl_prefix_ruby}ruby-devel
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
The Database Toolkit for Ruby

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
This package contains documentation for %{pkg_name}.


%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n %{gem_name}-%{version}
%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p ./%{gem_dir}
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}
#buildroot in %%install 
%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc  \
        %{gem_name}-%{version}.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
find %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/bin -type f | xargs chmod a+x
chmod a+x %{buildroot}%{gem_instdir}/spec/adapters/db2_spec.rb 

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gem_dir}/bin/sequel
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGELOG
%{gem_dir}/gems/%{gem_name}-%{version}/
%{gem_cache}
%{gem_spec}

%files doc
%defattr(-, root, root, -)
%doc %{gem_docdir}
%doc %{gem_instdir}/doc

%changelog
* Fri Aug 21 2015 Dominic Cleal <dcleal@redhat.com> 4.20.0-2
- Add smart_proxy_dynflow (RPM) (stbenjam@redhat.com)

* Tue Mar 17 2015 Dominic Cleal <dcleal@redhat.com> 4.20.0-1
- Update sequel to 4.20.0 (dcleal@redhat.com)

* Mon Dec 15 2014 Dominic Cleal <dcleal@redhat.com> 4.17.0-1
- Update sequel to 4.17.0 (dcleal@redhat.com)

* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 3.45.0-4
- correct BR (msuchy@redhat.com)

* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 3.45.0-3
- run gem spec inside of SC (msuchy@redhat.com)

* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 3.45.0-2
- new package built with tito

* Thu Mar 07 2013 Alejandro Pérez <aeperezt@fedoraproject.org> - 3.45.0-1
- Initial package
