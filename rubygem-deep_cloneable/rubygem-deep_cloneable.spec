%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkgname %{name}}

%define gem_name deep_cloneable
%global rubyabi 1.9.1

Summary: This gem gives every ActiveRecord::Base object the possibility to do a deep clone
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.0
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/moiristo/deep_cloneable
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem-activerecord >= 1:3.1.0
Requires: %{?scl_prefix}rubygem-activerecord < 1:5.0.0
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Extends the functionality of ActiveRecord::Base#clone to perform a deep clone
that includes user specified associations.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{pkgname} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%{gem_instdir}/*
%{gem_instdir}/lib
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.document
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc

%changelog
* Tue Jul 01 2014 Dominic Cleal <dcleal@redhat.com> 2.0.0-2
- Fix rubygem-activerecord dep to use epochs (dcleal@redhat.com)

* Tue Jul 01 2014 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Update to deep_cloneable 2.0 (dcleal@redhat.com)

* Mon Mar 03 2014 Dominic Cleal <dcleal@redhat.com> 1.6.0-2
- Add rubygems-devel BR so SCL paths are used, tidy up (dcleal@redhat.com)

* Fri Feb 21 2014 Daniel Lobato <dlobatog@redhat.com> - 1.6.0-1
- new package rubygem-deep_cloneable built with tito
