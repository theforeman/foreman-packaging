%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name safe_yaml

Summary: Parse YAML safely
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.4
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/dtao/safe_yaml
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
The SafeYAML gem provides an alternative implementation of YAML.load
suitable for accepting user input in Ruby applications

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/safe_yaml
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/*.sh
%exclude %{gem_instdir}/spec
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGES.md

%changelog
* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.0.4-3
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.0.4-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Nov 3 2015 Ondrej Prazak <oprazak@redhat.com> - 1.0.4-1
- Initial package
