%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name Platform
%global rubyabi 1.9.1

Summary: Hopefully robust platform sensing
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.0
Release: 2%{?dist}
Group: Development/Languages
License: LGPLv2+
URL: http://rubyforge.org/projects/platform/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Hopefully robust platform sensing


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

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


%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.0-2
- new package built with tito

* Sat Jun 30 2012 Miroslav Suchý <msuchy@redhat.com> 0.4.0-1
- new package built with tito

* Mon May 30 2011 Vít Ondruch <vondruch@redhat.com> - 0.4.0-1
- Initial package
