%define rbname ruby_parser
%define version 3.0.1
%define release 2

Summary: ruby_parser (RP) is a ruby parser written in pure ruby (utilizing racc--which does by default use a C extension)
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/seattlerb/ruby_parser
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby
Requires: rubygems >= 1.8.10

Requires: rubygem-sexp_processor >= 4.1.2
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(ruby_parser) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
racc--which does by default use a C extension). RP's output is
the same as ParseTree's output: s-expressions using ruby's arrays and
base types.
As an example:
def conditional1(arg1)
if arg1 == 0 then
return 1
end
return 0
end
becomes:
s(:defn, :conditional1,
s(:args, :arg1),
s(:scope,
s(:block,
s(:if,
s(:call, s(:lvar, :arg1), :==, s(:arglist, s(:lit, 0))),
s(:return, s(:lit, 1)),
nil),
s(:return, s(:lit, 0)))))


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

# Drop the standalone mode for tests - won't run that way due to missing 
# rubygems require anyway. One instance in lib as well
find %{buildroot}/usr/lib/ruby/gems/1.8/gems/ruby_parser-%{version}/{test,lib} -type f | \
  xargs -n 1 sed -i  -e '/^#!\/usr\/.*\/ruby.*/d'

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/ruby_parse
%{_bindir}/ruby_parse_extract_error
%{gemdir}/gems/ruby_parser-%{version}/.autotest
%doc %{gemdir}/gems/ruby_parser-%{version}/History.txt
%doc %{gemdir}/gems/ruby_parser-%{version}/Manifest.txt
%doc %{gemdir}/gems/ruby_parser-%{version}/README.txt
%{gemdir}/gems/ruby_parser-%{version}/Rakefile
%{gemdir}/gems/ruby_parser-%{version}/bin/ruby_parse
%{gemdir}/gems/ruby_parser-%{version}/lib/gauntlet_rubyparser.rb
%{gemdir}/gems/ruby_parser-%{version}/lib/ruby_lexer.rb
%{gemdir}/gems/ruby_parser-%{version}/bin/ruby_parse_extract_error
%{gemdir}/gems/ruby_parser-%{version}/lib/ruby18_parser.rb
%{gemdir}/gems/ruby_parser-%{version}/lib/ruby18_parser.y
%{gemdir}/gems/ruby_parser-%{version}/lib/ruby19_parser.rb
%{gemdir}/gems/ruby_parser-%{version}/lib/ruby19_parser.y
%{gemdir}/gems/ruby_parser-%{version}/lib/ruby_parser.rb
%{gemdir}/gems/ruby_parser-%{version}/lib/ruby_parser_extras.rb
%{gemdir}/gems/ruby_parser-%{version}/test/test_ruby_lexer.rb
%{gemdir}/gems/ruby_parser-%{version}/test/test_ruby_parser.rb
%{gemdir}/gems/ruby_parser-%{version}/test/test_ruby_parser_extras.rb
%{gemdir}/gems/ruby_parser-%{version}/.gemtest


%doc %{gemdir}/doc/ruby_parser-%{version}
%{gemdir}/cache/ruby_parser-%{version}.gem
%{gemdir}/specifications/ruby_parser-%{version}.gemspec

%changelog
