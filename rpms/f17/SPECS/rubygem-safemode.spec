# Generated from safemode-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name safemode
%global rubyabi 1.9.1

Summary: A library for safe evaluation of Ruby code based on ParseTree/RubyParser and Ruby2Ruby
Name: rubygem-%{gem_name}
Version: 1.0.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/svenfuchs/safemode
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(ruby2ruby) 
Requires: rubygem(ruby_parser) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A library for safe evaluation of Ruby code based on RubyParser and Ruby2Ruby.
Provides Rails ActionView template handlers for ERB and Haml.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

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
/usr/share/gems/gems/safemode-1.0.1/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.markdown

%changelog
* Thu Jun 14 2012 jason - 1.0.1-1
- Initial package
