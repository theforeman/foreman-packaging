%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name minitest-rails

Summary: MiniTest integration for Rails 3.x
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.2
Release: 6%{?dist}
Group: Development/Languages
License: MIT
URL: http://blowmage.com/minitest-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}ruby 
Requires: %{?scl_prefix}rubygem(minitest) => 3.4
Requires: %{?scl_prefix}rubygem(minitest) < 4
Requires: %{?scl_prefix}rubygem(rails) => 3.0
Requires: %{?scl_prefix}rubygem(rails) < 4
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Adds MiniTest as the default testing library in Rails 3.x


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/{.yardoc,.autotest,.gemtest,.travis.yml}



%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/gemfiles
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test
%{gem_instdir}/Rakefile

%changelog
* Fri Mar 29 2013 Marek Hulan <ares@igloonet.cz> 0.2-6
- SCL fix

* Tue Mar 26 2013 Marek Hulan <ares@igloonet.cz> 0.2-5
- new package built with tito

* Wed Oct 31 2012 Miroslav Suchý <msuchy@redhat.com> 0.2-4
- define gem_libdir on EL6 (msuchy@redhat.com)

* Tue Oct 30 2012 Miroslav Suchý <msuchy@redhat.com> 0.2-3
- fix files section (msuchy@redhat.com)

* Tue Oct 30 2012 Miroslav Suchý <msuchy@redhat.com> 0.2-2
- new package built with tito

* Tue Oct 30 2012 Miroslav Suchý <msuchy@redhat.com> - 0.2-1
- Initial package
