%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name css_parser

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.7
Release: 1%{?dist}
Summary: A set of classes for parsing CSS in Ruby
Group: Development/Languages
License: MIT
URL: https://github.com/premailer/css_parser
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(addressable)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Load, parse and cascade CSS rule sets in Ruby.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}


%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install
%{?scl:EOF}


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}/%{gem_dir}

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Thu Jun 02 2016 Dominic Cleal <dominic@cleal.org> 1.3.7-1
- new package built with tito

