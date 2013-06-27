%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from twitter-bootstrap-rails-2.2.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name twitter-bootstrap-rails
%global rubyabi 1.9.1

Summary: Bootstrap CSS toolkit for Rails 3.1 Asset Pipeline
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.2.6
Release: 5%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/seyhunak/twitter-bootstrap-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}ruby 
Requires: %{?scl_prefix}rubygem(railties) >= 3.1
Requires: %{?scl_prefix}rubygem(actionpack) >= 3.1
Requires: %{?scl_prefix}rubygem(execjs) 
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel 
BuildRequires: %{?scl_prefix}ruby 
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
twitter-bootstrap-rails project integrates Bootstrap CSS toolkit for Rails 3.1
Asset Pipeline


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
%{gem_instdir}/vendor
%{gem_instdir}/app
%doc %{gem_instdir}/README.md

%files doc
%doc %{gem_docdir}
%{gem_instdir}/test
%{gem_instdir}/Rakefile

%changelog
* Thu Jun 27 2013 Miroslav Suchý <msuchy@redhat.com> 2.2.6-5
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Fri Mar 29 2013 Miroslav Suchý <msuchy@redhat.com> 2.2.6-3
- new package built with tito

* Fri Mar 29 2013 Miroslav Suchý <msuchy@redhat.com> 2.2.6-2
- new package built with tito

* Fri Mar 29 2013 msuchy@redhat.com - 2.2.6-1
- Initial package
