%define rbname sexp_processor
%define version 3.1.0
%define release 1

Summary: sexp_processor branches from ParseTree bringing all the generic sexp processing tools with it
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/seattlerb/sexp_processor
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(sexp_processor) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
sexp_processor branches from ParseTree bringing all the generic sexp
processing tools with it. Sexp, SexpProcessor, Environment, etc... all
for your language processing pleasure.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

# Drop the standalone mode - won't run that way due to missing rubygems require
# anyway
find %{buildroot}/usr/lib/ruby/gems/1.8/gems/sexp_processor-3.1.0/test/ -type f | \
  xargs -n 1 sed -i  -e '/^#!\/usr\/.*\/ruby.*/d'
# Ships with extremely tight permissions, bring them inline with other gems
find %{buildroot}/usr/lib/ruby/gems/1.8/gems/sexp_processor-3.1.0/ -type f | \
  xargs chmod 0644



%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc %{gemdir}/gems/sexp_processor-3.1.0/History.txt
%doc %{gemdir}/gems/sexp_processor-3.1.0/Manifest.txt
%doc %{gemdir}/gems/sexp_processor-3.1.0/README.txt
%{gemdir}/gems/sexp_processor-3.1.0/Rakefile
%{gemdir}/gems/sexp_processor-3.1.0/lib/composite_sexp_processor.rb
%{gemdir}/gems/sexp_processor-3.1.0/lib/pt_testcase.rb
%{gemdir}/gems/sexp_processor-3.1.0/lib/sexp.rb
%{gemdir}/gems/sexp_processor-3.1.0/lib/sexp_processor.rb
%{gemdir}/gems/sexp_processor-3.1.0/lib/unique.rb
%{gemdir}/gems/sexp_processor-3.1.0/test/test_composite_sexp_processor.rb
%{gemdir}/gems/sexp_processor-3.1.0/test/test_environment.rb
%{gemdir}/gems/sexp_processor-3.1.0/test/test_sexp.rb
%{gemdir}/gems/sexp_processor-3.1.0/test/test_sexp_processor.rb
%{gemdir}/gems/sexp_processor-3.1.0/.gemtest


%doc %{gemdir}/doc/sexp_processor-3.1.0
%{gemdir}/cache/sexp_processor-3.1.0.gem
%{gemdir}/specifications/sexp_processor-3.1.0.gemspec

%changelog
