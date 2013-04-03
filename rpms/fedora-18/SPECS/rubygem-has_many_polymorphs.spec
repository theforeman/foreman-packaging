# Generated from has_many_polymorphs-3.0.0.beta1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name has_many_polymorphs
%global rubyabi 1.9.1

Summary: An ActiveRecord plugin for self-referential and double-sided polymorphic associations
Name: rubygem-%{gem_name}
Version: 3.0.0.beta1
Release: 3%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://blog.evanweaver.com/files/doc/fauna/has_many_polymorphs/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) >= 1.3.6
Requires: ruby
Requires: rubygem(activerecord)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description



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
%doc /usr/share/gems/gems/has_many_polymorphs-3.0.0.beta1/CHANGELOG
%doc /usr/share/gems/gems/has_many_polymorphs-3.0.0.beta1/Gemfile
%doc /usr/share/gems/gems/has_many_polymorphs-3.0.0.beta1/LICENSE
%doc /usr/share/gems/gems/has_many_polymorphs-3.0.0.beta1/README
%changelog
* Thu Jun 14 2012 jason - 3.0.0.beta1-1
- Initial package
