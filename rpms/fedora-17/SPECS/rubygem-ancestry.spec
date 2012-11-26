# Generated from ancestry-1.2.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ancestry
%global rubyabi 1.9.1

Summary: Ancestry allows the records of a ActiveRecord model to be organised in a tree structure, using a single, intuitively formatted database column. It exposes all the standard tree structure relations (ancestors, parent, root, children, siblings, descendants) and all of them can be fetched in a single sql query. Additional features are named_scopes, integrity checking, integrity restoration, arrangement of (sub)tree into hashes and different strategies for dealing with orphaned records
Name: rubygem-%{gem_name}
Version: 1.2.5
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/stefankroes/ancestry
Source0: %{gem_name}-%{version}.gem
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
/usr/share/gems/gems/ancestry-1.2.5/MIT-LICENSE
/usr/share/gems/gems/ancestry-1.2.5/README.rdoc
/usr/share/gems/gems/ancestry-1.2.5/ancestry.gemspec
/usr/share/gems/gems/ancestry-1.2.5/init.rb
/usr/share/gems/gems/ancestry-1.2.5/install.rb

%files doc
%doc %{gem_docdir}

%changelog
* Thu Jun 14 2012 jason - 1.2.5-1
- Initial package
