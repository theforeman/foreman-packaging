# Generated from ruby_parser-%{version}.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby_parser
%global rubyabi 1.9.1

Summary: ruby_parser (RP) is a ruby parser written in pure ruby (utilizing racc--which does by default use a C extension)
Name: rubygem-%{gem_name}
Version: 3.0.1
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/seattlerb/ruby_parser
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: rubygem(sexp_processor) => 4.1.2
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

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
	    --bindir .%{_bindir} \
	    --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
	%{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Drop the standalone mode for tests - won't run that way due to missing
# rubygems require anyway. One instance in lib as well
find %{buildroot}/usr/share/gems/gems/ruby_parser-%{version}/{test,lib} -type f | \
  xargs -n 1 sed -i -e '/^#!\/usr\/.*\/ruby.*/d'

%files
%dir %{gem_instdir}
%{_bindir}/ruby_parse
%{_bindir}/ruby_parse_extract_error
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems/gems/ruby_parser-%{version}/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt

%changelog
* Thu Jun 14 2012 jason - %{version}-1
- Initial package
