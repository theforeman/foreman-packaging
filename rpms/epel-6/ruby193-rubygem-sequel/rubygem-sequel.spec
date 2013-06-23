%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name sequel

Summary: The Database Toolkit for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.45.0
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: http://sequel.rubyforge.org
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
The Database Toolkit for Ruby

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

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
* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 3.45.0-4
- correct BR (msuchy@redhat.com)

* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 3.45.0-3
- run gem spec inside of SC (msuchy@redhat.com)

* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 3.45.0-2
- new package built with tito

* Thu Mar 07 2013 Alejandro Pérez <aeperezt@fedoraproject.org> - 3.45.0-1
- Initial package
