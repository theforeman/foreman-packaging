%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rsec

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.3
Release: 2%{?dist}
Summary: Extreme Fast Parser Combinator for Ruby
Group: Development/Languages
License: Ruby or BSD
URL: http://rsec.herokuapp.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Easy and extreme fast dynamic PEG parser combinator.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T

%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%license %{gem_instdir}/license.txt
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/bench
%{gem_instdir}/examples
%doc %{gem_instdir}/readme.rdoc
%{gem_instdir}/test

%changelog
* Fri Sep 06 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.4.3-2
- Updates to build for SCL

* Wed Mar 13 2019 Evgeni Golov 0.4.3-1
- Update to 0.4.3

* Thu May 25 2017 Dominic Cleal <dominic@cleal.org> 0.4.2-1
- new package built with tito

