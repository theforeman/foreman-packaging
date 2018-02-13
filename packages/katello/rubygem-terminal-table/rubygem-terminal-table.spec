%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name terminal-table

Summary: Simple, feature rich ascii table generation library
Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 1.5.2
Release: 2%{?dist}
Group:   Development/Languages
License: GPLv3
URL:     https://github.com/tj/terminal-table
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby(release)

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel

%description
Terminal Table is a fast and simple, yet feature rich ASCII table generator written in Ruby.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/lib
%{gem_instdir}/terminal-table.gemspec
%{gem_spec}

%exclude %{gem_cache}
%exclude %{gem_instdir}/examples
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Todo.rdoc
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Manifest

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.rdoc

%changelog
* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 1.5.2-2
- Build rubygem-terminal_table for rh22 SCL (ericdhelms@gmail.com)

* Tue Dec 01 2015 Eric D. Helms <ericdhelms@gmail.com> 1.5.2-1
- new package built with tito

* Mon Nov 2 2015 Ondrej Prazak <oprazak@redhat.com> 1.5.2-1
- initial build
