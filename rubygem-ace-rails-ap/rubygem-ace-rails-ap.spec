%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ace-rails-ap

Summary: The Ajax.org Cloud9 Editor (Ace) for the Rails asset pipeline
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.0.0
Release: 1%{?dist}
Group: Development/Libraries
License: MIT
URL: https://github.com/codykrieger/ace-rails-ap
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%endif
Requires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
The Ajax.org Cloud9 Editor (Ace) for the Rails 3.1+ asset pipeline.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/*.gemspec
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/update.sh

%files doc
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Fri Sep 04 2015 Dominic Cleal <dcleal@redhat.com> 3.0.3-1
- new package built with tito
