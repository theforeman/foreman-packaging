# template: default
%global gem_name sinatra

Name: rubygem-%{gem_name}
Version: 2.2.2
Release: 1%{?dist}
Epoch: 1
Summary: Classy web-development dressed in a DSL
License: MIT
URL: https://sinatrarb.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3.0
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
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
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_instdir}/VERSION
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/AUTHORS.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/MAINTENANCE.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.de.md
%doc %{gem_instdir}/README.es.md
%doc %{gem_instdir}/README.fr.md
%doc %{gem_instdir}/README.hu.md
%doc %{gem_instdir}/README.ja.md
%doc %{gem_instdir}/README.ko.md
%doc %{gem_instdir}/README.malayalam.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/README.pt-br.md
%doc %{gem_instdir}/README.pt-pt.md
%doc %{gem_instdir}/README.ru.md
%doc %{gem_instdir}/README.zh.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/examples
%exclude %{gem_instdir}/sinatra.gemspec

%changelog
* Mon Aug 01 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1:2.2.2-1
- Update to 2.2.2

* Sat Jul 23 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1:2.2.1-1
- Update to 2.2.1

* Fri May 13 2022 Eric D. Helms <ericdhelms@gmail.com> - 1:2.2.0-1
- Release rubygem-sinatra 2.2.0

* Thu Feb 10 2022 Patrick Creech <pcreech@redhat.com> - 1:2.1.0-3
- rebuilt

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-2
- Rebuild against rh-ruby27

* Thu Dec 17 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-1
- Release rubygem-sinatra 2.1.0

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.3-4
- Bump packages to build for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.3-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 2.0.3-2
- Bump for moving over to foreman-packaging

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.3-1
- Initial package
