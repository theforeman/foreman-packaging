%global gem_name logify

Name: rubygem-%{gem_name}
Version: 0.2.0
Release: 1%{?dist}
Summary: Logify is an incredibly light-weight Ruby logger
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/sethvargo/logify
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)

Requires: ruby(release)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel

BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Logify is an incredibly light-weight Ruby logger with a developer-friendly
API and no dependencies. It is intentionally very opinionated and is
optimized for speed. This combination makes it perfect for command line
applications.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml

%files doc
%doc %{gem_docdir}
%{gem_instdir}/CHANGELOG.md
%{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile*

%changelog

