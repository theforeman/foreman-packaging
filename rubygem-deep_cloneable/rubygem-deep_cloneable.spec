%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkgname %{name}}

%define gem_name deep_cloneable
%global rubyabi 1.9.1

Summary: This gem gives every ActiveRecord::Base object the possibility to do a deep clone
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.1.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/moiristo/deep_cloneable
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}rubygem-activerecord >= 1:3.1.0
Requires: %{?scl_prefix_ruby}rubygem-activerecord < 1:5.0.0
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
Extends the functionality of ActiveRecord::Base#clone to perform a deep clone
that includes user specified associations.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
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
* Wed Sep 30 2015 Dominic Cleal <dcleal@redhat.com> 2.1.1-1
- Update deep_cloneable to 2.1.1 (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 2.0.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Jan 07 2015 Dominic Cleal <dcleal@redhat.com> 2.0.2-1
- Update deep_cloneable to 2.0.2 (dcleal@redhat.com)

* Thu Jul 17 2014 Lukas Zapletal <lzap+git@redhat.com> 2.0.0-4
- Fixed dependency in the -doc subpackage (lzap+git@redhat.com)
- Fixed doc subpackages (lzap+git@redhat.com)

* Thu Jul 17 2014 Lukas Zapletal <lzap+rpm@redhat.com> 2.0.0-3
- Fixed dependency in the -doc subpackage

* Tue Jul 01 2014 Dominic Cleal <dcleal@redhat.com> 2.0.0-2
- Fix rubygem-activerecord dep to use epochs (dcleal@redhat.com)

* Tue Jul 01 2014 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Update to deep_cloneable 2.0 (dcleal@redhat.com)

* Mon Mar 03 2014 Dominic Cleal <dcleal@redhat.com> 1.6.0-2
- Add rubygems-devel BR so SCL paths are used, tidy up (dcleal@redhat.com)

* Fri Feb 21 2014 Daniel Lobato <dlobatog@redhat.com> - 1.6.0-1
- new package rubygem-deep_cloneable built with tito
