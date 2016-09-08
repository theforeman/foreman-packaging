# Generated from builder-3.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name builder

Name: rubygem-%{gem_name}
Version: 3.2.2
Release: 1%{?dist}
Summary: Builders for MarkUp
Group: Development/Languages
License: MIT
URL: http://onestepback.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?rhel} == 6
Requires: ruby(abi)
%else
Requires: ruby(release)
%endif
Requires: ruby
Requires: ruby(rubygems)
%if 0%{?rhel} == 6
BuildRequires: ruby(abi)
%else
BuildRequires: ruby(release)
%endif
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Builder provides a number of builder objects that make creating structured
data simple to do.  Currently the following builder objects are supported:
* XML Markup
* XML Events.


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
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%{gem_instdir}/rakelib
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGES
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/test

%changelog
* Wed Jun 15 2016 Dominic Cleal <dominic@cleal.org> 3.2.2-1
- new package built with tito

