# Generated from activerecord-3.0.15.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activerecord
%global rubyabi 1.9.1

Summary: Object-relational mapper framework (part of Rails)
Name: rubygem-%{gem_name}
Epoch: 1
Version: 3.0.15
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.rubyonrails.org
Source0: %{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby >= 1.8.7
Requires: rubygem(activesupport) = 3.0.15
Requires: rubygem(activemodel) = 3.0.15
Requires: rubygem(arel) => 2.0.10
Requires: rubygem(arel) < 2.1
Requires: rubygem(tzinfo) => 0.3.23
Requires: rubygem(tzinfo) < 0.4
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby >= 1.8.7
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: %{name} = %{version}
%description
Databases on Rails. Build a persistent domain model by mapping database tables
to Ruby classes. Strong conventions for associations, validations,
aggregations, migrations, and testing come baked-in.


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

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc /usr/share/gems/gems/activerecord-3.0.15/CHANGELOG
%doc /usr/share/gems/gems/activerecord-3.0.15/examples/associations.png
%doc /usr/share/gems/gems/activerecord-3.0.15/examples/performance.rb
%doc /usr/share/gems/gems/activerecord-3.0.15/examples/simple.rb

%changelog
* Thu Jun 14 2012 jason - 3.0.15-1
- Initial package
