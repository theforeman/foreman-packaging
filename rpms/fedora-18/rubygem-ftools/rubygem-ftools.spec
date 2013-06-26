%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ftools
%global rubyabi 1.9.1

Summary: Various file-tools for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/kaspernj/ftools
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Various file-tools for Ruby.

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

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}
%{gem_instdir}/LICENSE.txt
%{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/VERSION
%{gem_instdir}/%{gem_name}.gemspec

%exclude %{gem_instdir}/.document
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/Gemfile*

%changelog
* Wed Jun 26 2013 Dominic Cleal <dcleal@redhat.com> 0.0.0-1
- new package built with tito

