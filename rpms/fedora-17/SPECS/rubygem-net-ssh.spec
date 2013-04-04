# Generated from net-ssh-2.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name net-ssh
%global rubyabi 1.9.1

Summary: Net::SSH: a pure-Ruby implementation of the SSH2 client protocol
Name: rubygem-%{gem_name}
Version: 2.3.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/net-ssh/net-ssh
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
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.


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
/usr/share/gems/gems/net-ssh-2.3.0/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/THANKS.rdoc
%doc %{gem_instdir}/CHANGELOG.rdoc

%changelog
* Thu Jun 14 2012 jason - 2.3.0-1
- Initial package
