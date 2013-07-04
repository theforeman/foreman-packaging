%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name flot-rails
%global rubyabi 1.9.1

Summary: jQuery-flot javascript for Rails apps
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.3
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: https://rubygems.org/gems/flot-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(railties) => 3.1
Requires: %{?scl_prefix}rubygem(railties) < 4
Requires: %{?scl_prefix}rubygem(jquery-rails)
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
Provides easy installation and usage of jQuery-flot javascript
library for your Rails 3.1+ application.


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
%exclude %{gem_instdir}/.gitignore

%files doc
%doc %{gem_docdir}
%{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.0.3-3
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Thu May 02 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.3-2
- new package built with tito

* Thu May 02 2013 Ivan Necas <inecas@redhat.com> 0.0.3-1
- new package built with tito

* Thu Apr 11 2013 Ivan Necas <inecas@redhat.com> 0.0.2-1
- new package built with tito

