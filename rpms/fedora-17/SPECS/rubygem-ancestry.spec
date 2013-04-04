# Generated from ancestry-%{version}.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ancestry
%global rubyabi 1.9.1

Summary: Ancestry allows the records of a ActiveRecord model to be organised in a tree structure, using a single, intuitively formatted database column. It exposes all the standard tree structure relations (ancestors, parent, root, children, siblings, descendants) and all of them can be fetched in a single sql query. Additional features are named_scopes, integrity checking, integrity restoration, arrangement of (sub)tree into hashes and different strategies for dealing with orphaned records
Name: rubygem-%{gem_name}
Version: 1.3.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/stefankroes/ancestry
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(activerecord) >= 2.2.2
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Organise ActiveRecord model into a tree structure


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
/usr/share/gems/gems/ancestry-%{version}/MIT-LICENSE
/usr/share/gems/gems/ancestry-%{version}/README.rdoc
/usr/share/gems/gems/ancestry-%{version}/ancestry.gemspec
/usr/share/gems/gems/ancestry-%{version}/init.rb
/usr/share/gems/gems/ancestry-%{version}/install.rb

%files doc
%doc %{gem_docdir}

%changelog
* Mon Feb 4 2013 shk@redhat.com 1.3.0-1
- Updated to 1.3.0
* Thu Jun 14 2012 jason - 1.2.5-1
- Initial package
