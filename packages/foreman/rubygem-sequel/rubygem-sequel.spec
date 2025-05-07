# template: default
%global gem_name sequel

Name: rubygem-%{gem_name}
Version: 5.92.0
Release: 1%{?dist}
Summary: The Database Toolkit for Ruby
License: MIT
URL: https://sequel.jeremyevans.net
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.9.2
BuildRequires: ruby >= 1.9.2
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

# https://github.com/jeremyevans/sequel/pull/2003
Requires: rubygem(bigdecimal)

%description
The Database Toolkit for Ruby.


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

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/sequel
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Wed May 07 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.92.0-1
- Update to 5.92.0

* Wed Apr 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.91.0-1
- Update to 5.91.0

* Sun Mar 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.90.0-1
- Update to 5.90.0

* Sun Feb 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.89.0-1
- Update to 5.89.0

* Wed Jan 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.88.0-1
- Update to 5.88.0

* Tue Dec 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.87.0-1
- Update to 5.87.0

* Sun Nov 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.86.0-1
- Update to 5.86.0

* Wed Oct 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.85.0-1
- Update to 5.85.0

* Wed Sep 04 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.84.0-1
- Update to 5.84.0

* Sun Aug 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.83.1-1
- Update to 5.83.1

* Tue Jul 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.82.0-1
- Update to 5.82.0

* Sun Jun 09 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.81.0-1
- Update to 5.81.0

* Mon May 06 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.80.0-1
- Update to 5.80.0

* Sun Apr 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.79.0-1
- Update to 5.79.0

* Sun Mar 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.78.0-1
- Update to 5.78.0

* Sun Feb 04 2024 Foreman Packaging Automation <packaging@theforeman.org> - 5.77.0-1
- Update to 5.77.0

* Tue Jan 02 2024 Foreman Packaging Automation <packaging@theforeman.org> 5.76.0-1
- Update to 5.76.0

* Sun Dec 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.75.0-1
- Update to 5.75.0

* Sun Nov 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.74.0-1
- Update to 5.74.0

* Sun Oct 08 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.73.0-1
- Update to 5.73.0

* Sun Sep 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.72.0-1
- Update to 5.72.0

* Sun Aug 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.71.0-1
- Update to 5.71.0

* Sun Jul 09 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.70.0-1
- Update to 5.70.0

* Sun Jun 04 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.69.0-1
- Update to 5.69.0

* Fri May 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.68.0-1
- Update to 5.68.0

* Sun Apr 09 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.67.0-1
- Update to 5.67.0

* Thu Mar 09 2023 Bernhard Suttner <suttner@atix.de> 5.66.0-2
- bigdecimal is a requirement of sequel

* Sun Mar 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.66.0-1
- Update to 5.66.0

* Sun Feb 12 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.65.0-1
- Update to 5.65.0

* Tue Jan 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.64.0-1
- Update to 5.64.0

* Sun Jan 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.63.0-1
- Update to 5.63.0

* Thu Nov 03 2022 Foreman Packaging Automation <packaging@theforeman.org> 5.62.0-1
- Update to 5.62.0

* Sun Oct 09 2022 Foreman Packaging Automation <packaging@theforeman.org> 5.61.0-1
- Update to 5.61.0

* Sun Sep 18 2022 Foreman Packaging Automation <packaging@theforeman.org> 5.60.1-1
- Update to 5.60.1

* Sun Aug 28 2022 Foreman Packaging Automation <packaging@theforeman.org> 5.59.0-1
- Update to 5.59.0

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 5.58.0-1
- Update to 5.58.0

* Wed Feb 09 2022 Evgeni Golov 5.53.0-1
- Update to 5.53.0

* Mon Apr 05 2021 Eric D. Helms <ericdhelms@gmail.com> - 5.42.0-2
- Rebuild against rh-ruby27

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> 5.42.0-1
- Update to 5.42.0

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.7.1-3
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.7.1-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Apr 12 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.7.1-1
- Update to 5.7.1
- Regenerate the spec based on gem2rpm/scl.spec.erb

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.20.0-7
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 4.20.0-6
-

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 4.20.0-5
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Fri Oct 23 2015 Dominic Cleal <dcleal@redhat.com> 4.20.0-4
- Move docs to doc subpackage, remove big files (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 4.20.0-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

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
