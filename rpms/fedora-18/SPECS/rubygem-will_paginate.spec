# Generated from will_paginate-3.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name will_paginate
%global rubyabi 1.9.1

Summary: Pagination plugin for web frameworks and other apps
Name: rubygem-%{gem_name}
Version: 3.0.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/mislav/will_paginate/wiki
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
will_paginate provides a simple API for performing paginated queries with
Active Record, DataMapper and Sequel, and includes helpers for rendering
pagination links in Rails, Sinatra and Merb web apps.


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
/usr/share/gems/gems/will_paginate-3.0.3/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE

%changelog
* Thu Jun 14 2012 jason - 3.0.3-1
- Initial package
