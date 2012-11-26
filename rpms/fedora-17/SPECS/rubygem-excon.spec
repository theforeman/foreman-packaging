# Generated from excon-0.14.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name excon
%global rubyabi 1.9.1

Summary: speed, persistence, http(s)
Name: rubygem-%{gem_name}
Version: 0.14.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/geemus/excon
Source0: %{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
EXtended http(s) CONnections


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
   /usr/share/gems/gems/excon-0.14.0/Gemfile
   /usr/share/gems/gems/excon-0.14.0/Rakefile
   /usr/share/gems/gems/excon-0.14.0/benchmarks/
   /usr/share/gems/gems/excon-0.14.0/changelog.txt
   /usr/share/gems/gems/excon-0.14.0/data/cacert.pem
   /usr/share/gems/gems/excon-0.14.0/excon.gemspec
   /usr/share/gems/gems/excon-0.14.0/tests/

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Jun 14 2012 jason - 0.14.0-1
- Initial package
