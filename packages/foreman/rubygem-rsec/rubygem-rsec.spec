# Generated from rsec-0.4.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rsec

Name: rubygem-%{gem_name}
Version: 0.4.2
Release: 2%{?dist}
Summary: Extreme Fast Parser Combinator for Ruby
Group: Development/Languages
License: Ruby or BSD 
URL: http://rsec.herokuapp.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Easy and extreme fast dynamic PEG parser combinator.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%license %{gem_instdir}/license.txt
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/bench
%{gem_instdir}/examples
%doc %{gem_instdir}/readme.rdoc
%{gem_instdir}/test

%changelog
* Thu Aug 16 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.4.2-2
- Rebuild for Rails 5.2

* Thu May 25 2017 Dominic Cleal <dominic@cleal.org> 0.4.2-1
- new package built with tito

