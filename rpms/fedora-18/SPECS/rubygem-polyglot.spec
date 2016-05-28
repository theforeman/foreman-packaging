# Generated from polyglot-0.3.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name polyglot
%global rubyabi 1.9.1

Summary: Augment 'require' to load non-Ruby file types
Name: rubygem-%{gem_name}
Version: 0.3.3
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/cjheath/polyglot
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
The Polyglot library allows a Ruby module to register a loader
for the file type associated with a filename extension, and it
augments 'require' to find and load matching files.


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
/usr/share/gems/gems/polyglot-0.3.3/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.txt

%changelog
* Thu Jun 14 2012 jason - 0.3.3-1
- Initial package
