# Generated from route53-0.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name route53

Name: rubygem-%{gem_name}
Version: 0.4.0
Release: 1%{?dist}
Summary: Library for Amazon's Route 53 service
Group: Development/Languages
License: GPLv3
URL: https://github.com/pcorliss/ruby_route_53
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby
Requires: ruby(rubygems) >= 1.3.5
Requires: rubygem(ruby-hmac)
Requires: rubygem(nokogiri)
Requires: rubygem(builder)
BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygems-devel >= 1.3.5
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Provides CRUD and list operations for records and zones as part of Amazon's
Route 53 service.


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

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/route53
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/route53.gemspec
%{gem_instdir}/spec

%changelog
* Thu Feb 02 2017 Dominic Cleal <dominic@cleal.org> 0.4.0-1
- Update route53 to 0.4.0 (dominic@cleal.org)

* Wed Jun 15 2016 Dominic Cleal <dominic@cleal.org> 0.3.2-1
- new package built with tito

