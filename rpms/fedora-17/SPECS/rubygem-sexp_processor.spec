# Generated from sexp_processor-%{version}.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sexp_processor
%global rubyabi 1.9.1

Summary: sexp_processor branches from ParseTree bringing all the generic sexp processing tools with it
Name: rubygem-%{gem_name}
Version: 4.1.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/seattlerb/sexp_processor
Source0: %{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
sexp_processor branches from ParseTree bringing all the generic sexp
processing tools with it. Sexp, SexpProcessor, Environment, etc... all
for your language processing pleasure.


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

# Drop the standalone mode - won't run that way due to missing rubygems require
# anyway
find %{buildroot}/usr/share/gems/gems/sexp_processor-%{version}/test/ -type f | \
  xargs -n 1 sed -i -e '/^#!\/usr\/.*\/ruby.*/d'
# Ships with extremely tight permissions, bring them inline with other gems
find %{buildroot}/usr/share/gems/gems/sexp_processor-%{version}/ -type f | \
  xargs chmod 0644



%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems/gems/sexp_processor-%{version}/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt

%changelog
* Thu Jan 3 2012 shk@redhat.com - 4.1.2-1
- Updated to 4.1.2
* Thu Jun 14 2012 jason - 3.1.0-1
- Initial package
