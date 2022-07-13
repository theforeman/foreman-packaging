# template: default
%global gem_name faraday_middleware

Name: rubygem-%{gem_name}
Version: 1.2.0
Release: 1%{?dist}
Summary: Various middleware for Faraday
License: MIT
URL: https://github.com/lostisland/faraday_middleware
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3
BuildRequires: ruby >= 2.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Various middleware for Faraday.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Jul 13 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.0-1
- Update to 1.2.0

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
