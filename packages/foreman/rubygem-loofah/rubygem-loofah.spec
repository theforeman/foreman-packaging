# template: default
%global gem_name loofah

Name: rubygem-%{gem_name}
Version: 2.25.3
Release: 1%{?dist}
Summary: Loofah is a general library for manipulating and transforming HTML/XML documents and fragments, built on top of Nokogiri
License: MIT
URL: https://github.com/flavorjones/loofah
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# 2.25.3 declares nokogiri >= 1.19.5 (Ruby >= 3.2) to get GHSA-h6v6-rg66-fqj4. We ship
# nokogiri 1.17.2 on EL9 (Ruby 3.0) and EL10 with that fix backported, so require
# the patched build explicitly: the gemspec dependency is relaxed in %%prep.
Requires: rubygem-nokogiri >= 1.17.2-5

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Loofah is a general library for manipulating and transforming HTML/XML
documents and fragments, built on top of Nokogiri.
Loofah excels at HTML sanitization (XSS prevention). It includes some nice
HTML sanitizers, which are based on HTML5lib's safelist, so it most likely
won't make your codes less secure. (These statements have not been evaluated
by Netexperts.)
ActiveRecord extensions for sanitization are available in the
[`loofah-activerecord`
gem](https://github.com/flavorjones/loofah-activerecord).


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

# Upstream requires Ruby >= 3.2 and nokogiri >= 1.19.5 only because nokogiri 1.19.5
# carries the GHSA-h6v6-rg66-fqj4 fix. The code itself runs on Ruby 3.0 (EL9) and
# our nokogiri 1.17.2-5 backports that fix; see the Requires above.
# NOTE: update-requirements regenerates the 'ruby' Requires in the block above from the
# unmodified gem; keep it at >= 2.5.0 when bumping.
sed -i 's/Gem::Requirement.new(">= 3.2.0"/Gem::Requirement.new(">= 2.5.0"/' ../%{gem_name}-%{version}.gemspec
%gemspec_remove_dep -g nokogiri ">= 1.19.5"
%gemspec_add_dep -g nokogiri ">= 1.17.2"

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
%license %{gem_instdir}/MIT-LICENSE.txt
%doc %{gem_instdir}/SECURITY.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Tue Nov 24 2026 Ondřej Gajdušek <ogajduse@redhat.com> - 2.25.3-1
- Update to 2.25.3
- Relax the nokogiri (>= 1.17.2) and Ruby (>= 2.5.0) gemspec limits; require nokogiri with the GHSA-h6v6-rg66-fqj4 backport

* Mon Jul 27 2026 Zach Huntington-Meath <zhunting@redhat.com> - 2.25.2-2
- Rebuild for EL10

* Sun Jul 19 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.25.2-1
- Update to 2.25.2

* Sun Apr 12 2026 Foreman Packaging Automation <packaging@theforeman.org> - 2.25.1-1
- Update to 2.25.1

* Wed Dec 17 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.25.0-1
- Update to 2.25.0

* Wed May 14 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.24.1-1
- Update to 2.24.1

* Wed Jan 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.24.0-1
- Update to 2.24.0

* Wed Oct 30 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.23.1-1
- Update to 2.23.1

* Mon Oct 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.23.0-1
- Update to 2.23.0

* Thu Nov 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.22.0-1
- Update to 2.22.0

* Thu Oct 12 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.21.4-1
- Update to 2.21.4

* Tue May 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.21.3-1
- Update to 2.21.3

* Wed May 10 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.21.1-1
- Update to 2.21.1

* Sun Apr 09 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.20.0-1
- Update to 2.20.0

* Sun Jan 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.19.1-1
- Update to 2.19.1

* Sun Oct 02 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.19.0-1
- Update to 2.19.0

* Wed Jul 06 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.18.0-1
- Update to 2.18.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.4.0-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.4.0-1
- Release rubygem-loofah 2.4.0

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.2-5
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.2-4
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 2.2.2-3
- Bump for moving over to foreman-packaging

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-2
- rebuilt

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-1
- Initial package
