# Generated from activemodel-3.0.17.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activemodel
%global rubyabi 1.9.1

Summary: A toolkit for building modeling frameworks (part of Rails)
Name: rubygem-%{gem_name}
Epoch: 1
Version: 3.0.17
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.rubyonrails.org
Source0: %{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby >= 1.8.7
Requires: rubygem(activesupport) = 3.0.17
Requires: rubygem(builder) => 2.1.2
Requires: rubygem(builder) < 2.2
Requires: rubygem(i18n) => 0.5.0
Requires: rubygem(i18n) < 0.6
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby >= 1.8.7
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: %{name} = %{version}
%description
A toolkit for building modeling frameworks like Active Record and Active
Resource. Rich support for attributes, callbacks, validations, observers,
serialization, internationalization, and testing.


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
%doc /usr/share/gems/gems/activemodel-3.0.17/CHANGELOG
%doc /usr/share/gems/gems/activemodel-3.0.17/MIT-LICENSE
%doc /usr/share/gems/gems/activemodel-3.0.17/README.rdoc

%changelog
* Thu Jun 14 2012 jason - 3.0.17-1
- Initial package
