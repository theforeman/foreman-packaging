# template: default
%global gem_name sexp_processor

Name: rubygem-%{gem_name}
Version: 4.17.4
Release: 1%{?dist}
Summary: sexp_processor branches from ParseTree bringing all the generic sexp processing tools with it
License: MIT
URL: https://github.com/seattlerb/sexp_processor
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6
Requires: ruby < 4
BuildRequires: ruby >= 2.6
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
sexp_processor branches from ParseTree bringing all the generic sexp
processing tools with it. Sexp, SexpProcessor, Environment, etc... all
for your language processing pleasure.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/Manifest.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Wed Sep 03 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.17.4-1
- Update to 4.17.4

* Tue Nov 12 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.17.3-1
- Update to 4.17.3

* Sun Jul 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.17.2-1
- Update to 4.17.2

* Thu Jan 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.17.1-1
- Update to 4.17.1

* Fri May 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 4.17.0-1
- Update to 4.17.0

* Sun Jul 24 2022 Foreman Packaging Automation <packaging@theforeman.org> 4.16.1-1
- Update to 4.16.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.10.0-7
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.10.0-6
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 4.10.0-5
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Jan 17 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.10.0-4
- Bump rubygem-sexp_processor to 4.10.0 (dmitri@appliedlogic.ca)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.4.4-4
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 4.4.4-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 4.4.4-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 4.4.4-1
- Update sexp_processor to 4.4.4 (dcleal@redhat.com)
- Build for Fedora 19 (dcleal@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 4.1.3-4
- rebase to sexp_processor-4.1.3 (msuchy@redhat.com)

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 4.1.3-3
- define libdir for el6 (msuchy@redhat.com)

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 4.1.3-2
- tune up spec (msuchy@redhat.com)
- rebase to sexp_processor-4.1.3.gem (msuchy@redhat.com)

* Fri Oct 26 2012 Dmitri Dolguikh <dmitri@appliedlogic.ca> 4.1.0-1
- new package built with tito

* Fri Oct 26 2012 wb - 4.1.0-1
- Initial package
