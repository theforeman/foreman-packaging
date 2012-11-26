%define rbname multi_json
%define version 1.2.0
%define release 1

Summary: A gem to provide swappable JSON backends.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/intridea/multi_json
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(multi_json) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
A gem to provide easy switching between different JSON backends, including Oj,
Yajl, the JSON gem (with C-extensions), the pure-Ruby JSON gem, and OkJson.


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
%doc %{gemdir}/gems/multi_json-1.2.0/LICENSE.md
%doc %{gemdir}/gems/multi_json-1.2.0/README.md
%{gemdir}/gems/multi_json-1.2.0/Rakefile
%{gemdir}/gems/multi_json-1.2.0/multi_json.gemspec
%{gemdir}/gems/multi_json-1.2.0/Gemfile
%{gemdir}/gems/multi_json-1.2.0/.document
%{gemdir}/gems/multi_json-1.2.0/.rspec
%{gemdir}/gems/multi_json-1.2.0/.travis.yml
%{gemdir}/gems/multi_json-1.2.0/spec/engine_shared_example.rb
%{gemdir}/gems/multi_json-1.2.0/spec/helper.rb
%{gemdir}/gems/multi_json-1.2.0/spec/multi_json_spec.rb
%{gemdir}/gems/multi_json-1.2.0/lib/multi_json/engines/json_common.rb
%{gemdir}/gems/multi_json-1.2.0/lib/multi_json/engines/json_gem.rb
%{gemdir}/gems/multi_json-1.2.0/lib/multi_json/engines/json_pure.rb
%{gemdir}/gems/multi_json-1.2.0/lib/multi_json/engines/nsjsonserialization.rb
%{gemdir}/gems/multi_json-1.2.0/lib/multi_json/engines/oj.rb
%{gemdir}/gems/multi_json-1.2.0/lib/multi_json/engines/ok_json.rb
%{gemdir}/gems/multi_json-1.2.0/lib/multi_json/engines/yajl.rb
%{gemdir}/gems/multi_json-1.2.0/lib/multi_json/vendor/ok_json.rb
%{gemdir}/gems/multi_json-1.2.0/lib/multi_json/version.rb
%{gemdir}/gems/multi_json-1.2.0/lib/multi_json.rb


%doc %{gemdir}/doc/multi_json-1.2.0
%{gemdir}/cache/multi_json-1.2.0.gem
%{gemdir}/specifications/multi_json-1.2.0.gemspec

%changelog
