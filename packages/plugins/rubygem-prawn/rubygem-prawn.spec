# template: default
%global gem_name prawn

Name: rubygem-%{gem_name}
Version: 2.4.0
Release: 1%{?dist}
Summary: A fast and nimble PDF generator for Ruby
License: (GPLv2 or GPLv3 or Ruby) and APAFML
URL: https://prawnpdf.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel >= 1.3.6
BuildArch: noarch
# end specfile generated dependencies

%description
Prawn is a fast, tiny, and nimble PDF generator for Ruby.


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
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/GPLv2
%license %{gem_instdir}/GPLv3
%license %{gem_instdir}/LICENSE
%{gem_instdir}/data
%{gem_libdir}
%{gem_instdir}/manual
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/prawn.gemspec
%{gem_instdir}/spec

%changelog
* Tue Jan 16 2024 Evgeni Golov - 2.4.0-1
- Update to 2.4.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-3
- Rebuild for Ruby 2.7

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-2
- Rebuild for Rails 5.2 and Ruby 2.5

