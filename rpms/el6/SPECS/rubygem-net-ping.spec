%define rbname net-ping
%define version 1.3.7
%define release 1

Summary: A ping interface for Ruby.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://www.rubyforge.org/projects/shards
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(net-ping) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
The net-ping library provides a ping interface for Ruby. It includes
separate TCP, HTTP, ICMP, UDP, WMI (for Windows) and external ping
classes.


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
%doc %{gemdir}/gems/net-ping-1.3.7/CHANGES
%doc %{gemdir}/gems/net-ping-1.3.7/doc/ping.txt
%{gemdir}/gems/net-ping-1.3.7/examples/example_pingexternal.rb
%{gemdir}/gems/net-ping-1.3.7/examples/example_pinghttp.rb
%{gemdir}/gems/net-ping-1.3.7/examples/example_pingtcp.rb
%{gemdir}/gems/net-ping-1.3.7/examples/example_pingudp.rb
%{gemdir}/gems/net-ping-1.3.7/lib/net/ping/external.rb
%{gemdir}/gems/net-ping-1.3.7/lib/net/ping/http.rb
%{gemdir}/gems/net-ping-1.3.7/lib/net/ping/icmp.rb
%{gemdir}/gems/net-ping-1.3.7/lib/net/ping/ping.rb
%{gemdir}/gems/net-ping-1.3.7/lib/net/ping/tcp.rb
%{gemdir}/gems/net-ping-1.3.7/lib/net/ping/udp.rb
%{gemdir}/gems/net-ping-1.3.7/lib/net/ping/wmi.rb
%{gemdir}/gems/net-ping-1.3.7/lib/net/ping.rb
%{gemdir}/gems/net-ping-1.3.7/MANIFEST
%{gemdir}/gems/net-ping-1.3.7/net-ping.gemspec
%{gemdir}/gems/net-ping-1.3.7/Rakefile
%doc %{gemdir}/gems/net-ping-1.3.7/README
%{gemdir}/gems/net-ping-1.3.7/test/test_net_ping.rb
%{gemdir}/gems/net-ping-1.3.7/test/test_net_ping_external.rb
%{gemdir}/gems/net-ping-1.3.7/test/test_net_ping_http.rb
%{gemdir}/gems/net-ping-1.3.7/test/test_net_ping_icmp.rb
%{gemdir}/gems/net-ping-1.3.7/test/test_net_ping_tcp.rb
%{gemdir}/gems/net-ping-1.3.7/test/test_net_ping_udp.rb
%{gemdir}/gems/net-ping-1.3.7/test/test_net_ping_wmi.rb


%doc %{gemdir}/doc/net-ping-1.3.7
%{gemdir}/cache/net-ping-1.3.7.gem
%{gemdir}/specifications/net-ping-1.3.7.gemspec

%changelog
