%define rbname hoe
%define version 3.0.3
%define release 1

Summary: Hoe is a rake/rubygems helper for project Rakefiles
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://www.zenspider.com/projects/hoe.html
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.3.7

Requires: rubygem-rake => 0.8
Requires: rubygem-rake < 1
BuildRequires: ruby 
BuildRequires: rubygems >= 1.3.7
BuildArch: noarch
Provides: rubygem(hoe) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps you
manage, maintain, and release your project and includes a dynamic
plug-in system allowing for easy extensibility. Hoe ships with
plug-ins for all your usual project tasks including rdoc generation,
testing, packaging, deployment, and announcement..
See class rdoc for help. Hint: `ri Hoe` or any of the plugins listed
below.
For extra goodness, see: http://seattlerb.rubyforge.org/hoe/Hoe.pdf


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/sow
%{gemdir}/gems/hoe-3.0.3/.autotest
%doc %{gemdir}/gems/hoe-3.0.3/History.txt
%{gemdir}/gems/hoe-3.0.3/Hoe.pdf
%doc %{gemdir}/gems/hoe-3.0.3/Manifest.txt
%doc %{gemdir}/gems/hoe-3.0.3/README.txt
%{gemdir}/gems/hoe-3.0.3/Rakefile
%{gemdir}/gems/hoe-3.0.3/bin/sow
%{gemdir}/gems/hoe-3.0.3/lib/hoe.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/clean.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/compiler.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/debug.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/deps.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/flay.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/flog.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/gem_prelude_sucks.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/gemcutter.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/inline.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/newb.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/package.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/publish.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/racc.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/rake.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/rcov.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/rubyforge.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/signing.rb
%{gemdir}/gems/hoe-3.0.3/lib/hoe/test.rb
%{gemdir}/gems/hoe-3.0.3/template/.autotest.erb
%{gemdir}/gems/hoe-3.0.3/template/History.txt.erb
%{gemdir}/gems/hoe-3.0.3/template/Manifest.txt.erb
%{gemdir}/gems/hoe-3.0.3/template/README.txt.erb
%{gemdir}/gems/hoe-3.0.3/template/Rakefile.erb
%{gemdir}/gems/hoe-3.0.3/template/bin/file_name.erb
%{gemdir}/gems/hoe-3.0.3/template/lib/file_name.rb.erb
%{gemdir}/gems/hoe-3.0.3/template/test/test_file_name.rb.erb
%{gemdir}/gems/hoe-3.0.3/test/test_hoe.rb
%{gemdir}/gems/hoe-3.0.3/test/test_hoe_debug.rb
%{gemdir}/gems/hoe-3.0.3/test/test_hoe_gemcutter.rb
%{gemdir}/gems/hoe-3.0.3/test/test_hoe_publish.rb
%{gemdir}/gems/hoe-3.0.3/test/test_hoe_test.rb
%{gemdir}/gems/hoe-3.0.3/.gemtest


%doc %{gemdir}/doc/hoe-3.0.3
%doc /usr/lib/ruby/gems/1.8/cache/hoe-3.0.3.gem
%doc /usr/lib/ruby/gems/1.8/specifications/hoe-3.0.3.gemspec
%changelog
