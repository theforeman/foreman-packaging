%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name compass
%global rubyabi 1.9.1

Summary: A Real Stylesheet Framework
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.12.2
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://compass-style.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}rubygems 
Requires: %{?scl_prefix}rubygem(sass) => 3.1
Requires: %{?scl_prefix}rubygem(chunky_png) => 1.2
Requires: %{?scl_prefix}rubygem(fssm) >= 0.2.7
BuildRequires: %{?scl_prefix}rubygems 
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Compass is a Sass-based Stylesheet Framework that streamlines the creation and
maintainance of CSS.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{_bindir}/compass
%{gem_instdir}/frameworks
%{gem_instdir}/bin
%{gem_instdir}/lib
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/LICENSE.markdown
%doc %{gem_instdir}/README.markdown
%doc %{gem_instdir}/VERSION.yml
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/test
%doc %{gem_instdir}/features
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Tue Mar 26 2013 Marek Hulan <ares@igloonet.cz> 0.12.2-3
- require ruby193-build for tagging (msuchy@redhat.com)

* Mon Mar 25 2013 Marek Hulan <ares@igloonet.cz> 0.12.2-2
- compass update
* Mon Jul 25 2011 Shannon Hughes <shughes@redhat.com> 0.11.5-1
- upgrade to 0.11.5 (shughes@redhat.com)

* Fri Jul 22 2011 Shannon Hughes <shughes@redhat.com> - 0.11.5-1
- Initial package
