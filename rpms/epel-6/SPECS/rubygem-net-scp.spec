%define rbname net-scp
%define version 1.0.4
%define release 1

Summary: A pure Ruby implementation of the SCP client protocol
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://net-ssh.rubyforge.org/scp
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-net-ssh >= 1.99.1
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(net-scp) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
A pure Ruby implementation of the SCP client protocol


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc %{gemdir}/gems/net-scp-1.0.4/CHANGELOG.rdoc
%doc %{gemdir}/gems/net-scp-1.0.4/lib/net/scp/download.rb
%doc %{gemdir}/gems/net-scp-1.0.4/lib/net/scp/errors.rb
%doc %{gemdir}/gems/net-scp-1.0.4/lib/net/scp/upload.rb
%doc %{gemdir}/gems/net-scp-1.0.4/lib/net/scp/version.rb
%doc %{gemdir}/gems/net-scp-1.0.4/lib/net/scp.rb
%doc %{gemdir}/gems/net-scp-1.0.4/lib/uri/open-scp.rb
%doc %{gemdir}/gems/net-scp-1.0.4/lib/uri/scp.rb
%{gemdir}/gems/net-scp-1.0.4/Rakefile
%doc %{gemdir}/gems/net-scp-1.0.4/README.rdoc
%{gemdir}/gems/net-scp-1.0.4/setup.rb
%{gemdir}/gems/net-scp-1.0.4/test/common.rb
%{gemdir}/gems/net-scp-1.0.4/test/test_all.rb
%{gemdir}/gems/net-scp-1.0.4/test/test_download.rb
%{gemdir}/gems/net-scp-1.0.4/test/test_scp.rb
%{gemdir}/gems/net-scp-1.0.4/test/test_upload.rb
%{gemdir}/gems/net-scp-1.0.4/Manifest
%{gemdir}/gems/net-scp-1.0.4/net-scp.gemspec


%doc %{gemdir}/doc/net-scp-1.0.4
%{gemdir}/cache/net-scp-1.0.4.gem
%{gemdir}/specifications/net-scp-1.0.4.gemspec

%changelog
