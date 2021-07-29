# template: nonscl
%global gem_name rexml
%global gem_require_name %{gem_name}

Name: rubygem-%{gem_name}
Version: 3.2.5
Release: 1%{?dist}
Summary: An XML toolkit for Ruby
Group: Development/Languages
License: BSD-2-Clause
URL: https://github.com/ruby/rexml
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby(release)
Requires: ruby
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
An XML toolkit for Ruby.


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
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/NEWS.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/doc

%changelog
* Thu Jul 29 2021 Justin Sherrill <jsherril@redhat.com> 3.2.5-1
- Add rubygem-rexml generated by gem2rpm using the nonscl template

