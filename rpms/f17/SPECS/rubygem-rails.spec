# Generated from rails-3.0.15.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rails
%global rubyabi 1.9.1

Summary: Full-stack web application framework
Name: rubygem-%{gem_name}
Epoch: 1
Version: 3.0.15
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.rubyonrails.org
Source0: %{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) >= 1.3.6
Requires: ruby >= 1.8.7
Requires: rubygem(activesupport) = 3.0.15
Requires: rubygem(actionpack) = 3.0.15
Requires: rubygem(activerecord) = 3.0.15
Requires: rubygem(activeresource) = 3.0.15
Requires: rubygem(actionmailer) = 3.0.15
Requires: rubygem(railties) = 3.0.15
Requires: rubygem(bundler) => 1.0
Requires: rubygem(bundler) < 2
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby >= 1.8.7
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: %{name} = %{version}
%description
Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.


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
            --bindir .%{_bindir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x


%files
%dir %{gem_instdir}
%{_bindir}/rails
%{gem_instdir}/bin
#%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Thu Jun 14 2012 jason - 3.0.15-1
- Initial package
