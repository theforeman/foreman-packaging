# template: default
%global gem_name pdf-core

Name: rubygem-%{gem_name}
Version: 0.9.0
Release: 1%{?dist}
Summary: PDF::Core is used by Prawn to render PDF documents
License: GPLv2 or GPLv3 or Ruby
URL: https://prawnpdf.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel >= 1.3.6
BuildArch: noarch
# end specfile generated dependencies

%description
PDF::Core is used by Prawn to render PDF documents.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
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
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/GPLv2
%license %{gem_instdir}/GPLv3
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/pdf-core.gemspec

%changelog
* Tue Jan 16 2024 Evgeni Golov - 0.9.0-1
- Update to 0.9.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.7.0-3
- Rebuild for Ruby 2.7

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.7.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

