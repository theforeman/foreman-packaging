%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-aws

Summary: Module for the 'fog' gem to support Amazon Web Services
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 1.3.0
Release: 3%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/fog/fog-aws
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(fog-core) >= 1.38
Requires: %{?scl_prefix}rubygem(fog-core) < 2
Requires: %{?scl_prefix}rubygem(fog-json) >= 1
Requires: %{?scl_prefix}rubygem(fog-json) < 2
Requires: %{?scl_prefix}rubygem(fog-xml) >= 0.1
Requires: %{?scl_prefix}rubygem(fog-xml) < 1
Requires: %{?scl_prefix}rubygem(ipaddress) >= 0.8
Requires: %{?scl_prefix}rubygem(ipaddress) < 1
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This library can be used as a module for `fog` or as standalone provider to
use the Amazon Web Services in applications.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -T -c
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
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.md
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/tests
%{gem_instdir}/gemfiles
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/%{gem_name}.gemspec

%changelog
* Thu Aug 16 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.3.0-3
- Rebuild for Rails 5.2

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.0-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri Mar 31 2017 Dominic Cleal <dominic@cleal.org> 1.3.0-1
- Update fog-aws to 1.3.0 (dominic@cleal.org)

* Tue Jan 24 2017 Dominic Cleal <dominic@cleal.org> 1.2.0-1
- Update fog-aws to 1.2.0 (dominic@cleal.org)

* Thu Dec 22 2016 Dominic Cleal <dominic@cleal.org> 0.13.0-1
- Update fog-aws to 0.13.0 (#17781, kvedulv@kvedulv.de)

* Tue Jul 19 2016 Dominic Cleal <dominic@cleal.org> 0.10.0-1
- Update fog-aws to 0.10.0 (dominic@cleal.org)

* Wed Mar 09 2016 Dominic Cleal <dominic@cleal.org> 0.9.1-1
- Update fog-aws to 0.9.1 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.7.4-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.7.4-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Aug 12 2015 Dominic Cleal <dcleal@redhat.com> 0.7.4-1
- Update fog-aws to 0.7.4 (dcleal@redhat.com)

* Wed Jul 08 2015 Dominic Cleal <dcleal@redhat.com> 0.7.0-1
- Update fog-aws to 0.7.0 (dcleal@redhat.com)

* Fri Jul 03 2015 Dominic Cleal <dcleal@redhat.com> 0.6.0-1
- Update fog-aws to 0.6.0 (dcleal@redhat.com)

* Tue Jun 23 2015 Dominic Cleal <dcleal@redhat.com> 0.5.0-1
- Update fog-aws to 0.5.0 (dcleal@redhat.com)

* Mon Jun 01 2015 Dominic Cleal <dcleal@redhat.com> 0.4.0-1
- Update fog-aws to 0.4.0 (dcleal@redhat.com)
- Fixes #9703 - change %%{dist} to %%{?dist} (jmontleo@redhat.com)

* Sun Feb 22 2015 Daniel Lobato <dlobatog@redhat.com> 0.1.0-1
- Update fog-aws to version 0.1.0

* Tue Feb 17 2015 Dominic Cleal <dcleal@redhat.com> 0.0.8-1
- new package built with tito
