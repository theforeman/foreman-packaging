%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from faraday_middleware-0.10.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name faraday_middleware

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.13.1
Release: 3%{?dist}
Summary: Various middleware for Faraday
Group: Development/Languages
License: MIT
URL: https://github.com/lostisland/faraday_middleware
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(faraday) < 1.0
Requires: %{?scl_prefix}rubygem(faraday) >= 0.7.4
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Various middleware for Faraday.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.13.1-3
- Rebuild for Ruby 2.7

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.13.1-2
- Build for SCL

* Thu Mar 28 2019 Marek Hulan <mhulan@redhat.com> 0.13.1-1
- Update to 0.13.1

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 0.10.0-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue May 17 2016 Daniel Lobato - 0.10.0-1
- Initial package
