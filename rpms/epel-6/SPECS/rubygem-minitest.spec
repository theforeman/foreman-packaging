%define rbname minitest
%define version 2.12.0
%define release 2

Summary: minitest provides a complete suite of testing facilities supporting TDD, BDD, mocking, and benchmarking
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/seattlerb/minitest
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.3.7
BuildRequires: ruby 
BuildRequires: rubygems >= 1.3.7
BuildArch: noarch
Provides: rubygem(minitest) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
minitest provides a complete suite of testing facilities supporting
TDD, BDD, mocking, and benchmarking.
"I had a class with Jim Weirich on testing last week and we were
allowed to choose our testing frameworks. Kirk Haines and I were
paired up and we cracked open the code for a few test
frameworks...
I MUST say that minitest is *very* readable / understandable
compared to the 'other two' options we looked at. Nicely done and
thank you for helping us keep our mental sanity."
-- Wayne E. Seguin
minitest/unit is a small and incredibly fast unit testing framework.
It provides a rich set of assertions to make your tests clean and
readable.
minitest/spec is a functionally complete spec engine. It hooks onto
minitest/unit and seamlessly bridges test assertions over to spec
expectations.
minitest/benchmark is an awesome way to assert the performance of your
algorithms in a repeatable manner. Now you can assert that your newb
co-worker doesn't replace your linear algorithm with an exponential
one!
minitest/mock by Steven Baker, is a beautifully tiny mock object
framework.
minitest/pride shows pride in testing and adds coloring to your test
output. I guess it is an example of how to write IO pipes too. :P
minitest/unit is meant to have a clean implementation for language
implementors that need a minimal set of methods to bootstrap a working
test suite. For example, there is no magic involved for test-case
discovery.
"Again, I can't praise enough the idea of a testing/specing
framework that I can actually read in full in one sitting!"
-- Piotr Szotkowski


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
%{gemdir}/gems/minitest-2.12.0/.autotest
%doc %{gemdir}/gems/minitest-2.12.0/History.txt
%doc %{gemdir}/gems/minitest-2.12.0/Manifest.txt
%doc %{gemdir}/gems/minitest-2.12.0/README.txt
%{gemdir}/gems/minitest-2.12.0/Rakefile
%{gemdir}/gems/minitest-2.12.0/design_rationale.rb
%{gemdir}/gems/minitest-2.12.0/lib/hoe/minitest.rb
%{gemdir}/gems/minitest-2.12.0/lib/minitest/autorun.rb
%{gemdir}/gems/minitest-2.12.0/lib/minitest/benchmark.rb
%{gemdir}/gems/minitest-2.12.0/lib/minitest/mock.rb
%{gemdir}/gems/minitest-2.12.0/lib/minitest/pride.rb
%{gemdir}/gems/minitest-2.12.0/lib/minitest/spec.rb
%{gemdir}/gems/minitest-2.12.0/lib/minitest/unit.rb
%{gemdir}/gems/minitest-2.12.0/test/metametameta.rb
%{gemdir}/gems/minitest-2.12.0/test/test_minitest_benchmark.rb
%{gemdir}/gems/minitest-2.12.0/test/test_minitest_mock.rb
%{gemdir}/gems/minitest-2.12.0/test/test_minitest_spec.rb
%{gemdir}/gems/minitest-2.12.0/test/test_minitest_unit.rb
%{gemdir}/gems/minitest-2.12.0/.gemtest

%doc %{gemdir}/doc/minitest-2.12.0
%{gemdir}/cache/minitest-2.12.0.gem
%{gemdir}/specifications/minitest-2.12.0.gemspec

%changelog
* Tue May 08 2012 jmontleo@redhat.com - 2.12.0-2
- Cleaned up spec file

