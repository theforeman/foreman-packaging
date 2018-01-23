%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name safemode

Summary: A library for safe evaluation of Ruby code
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 1.3.4
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/svenfuchs/safemode
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(ruby2ruby) >= 2.4.0
Requires: %{?scl_prefix}rubygem(ruby_parser) >= 3.10.1
Requires: %{?scl_prefix}rubygem(sexp_processor) >= 4.10.0

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(rake)
BuildRequires: %{?scl_prefix_ruby}rubygem(rdoc)
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(safemode) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A library for safe evaluation of Ruby code based on RubyParser and Ruby2Ruby.
Provides Rails ActionView template handlers for ERB and Haml.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p .%{gem_dir}

# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} - <<EOF}
%gem_install
%{?scl:EOF}
rm -rf ./%{gem_instdir}/.yardoc

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
mv %{buildroot}%{gem_instdir}/{LICENCSE,README.markdown} ./
rm %{buildroot}%{gem_instdir}/{VERSION,.travis.yml}

%files
%doc LICENCSE
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/demo.rb
%{gem_instdir}/init.rb
%{gem_instdir}/safemode.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/test
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%{gem_docdir}

%changelog
* Tue Jan 23 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.4-1
- Update rubygem-safemode to 1.3.4 (dmitri@appliedlogic.ca)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.2-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Update safemode to 1.3.2 (tbrisker@gmail.com)

* Mon Feb 13 2017 Dominic Cleal <dominic@cleal.org> 1.3.1-1
- Update safemode to 1.3.1 (dominic@cleal.org)

* Wed Jan 25 2017 Dominic Cleal <dominic@cleal.org> 1.2.5-1
- Update rubygem-safemode to 1.2.5 (dmitri@appliedlogic.ca)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 1.2.4-2
- Use gem_install macro (dominic@cleal.org)

* Fri Apr 15 2016 Dominic Cleal <dominic@cleal.org> 1.2.4-1
- Update safemode to 1.2.4 (dominic@cleal.org)

* Wed Mar 09 2016 Dominic Cleal <dominic@cleal.org> 1.2.3-1
- Update safemode to 1.2.3 (mhulan@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.2.2-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.2.2-2
- Converted to tfm SCL (dcleal@redhat.com)
- Fixes #9703 - change %%{dist} to %%{?dist} (jmontleo@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 1.2.2-1
- Update safemode to 1.2.2 (dcleal@redhat.com)

* Wed Jul 30 2014 Dominic Cleal <dcleal@redhat.com> 1.2.1-1
- Update to v1.2.1 (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 1.2.0-5
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- remove unused BRs (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 1.2.0-3
- new package built with tito

* Wed Feb 20 2013 Lukas Zapletal <lzap+git@redhat.com> 1.2.0-2
- safemode 1.2

* Wed Feb 20 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.2.0-1
- new version

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.0-2
- require correct version of gems -namely ruby2ruby (msuchy@redhat.com)

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.0-1
- rebase to safemode-1.1.0.gem (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-6
- fix sed expression (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-5
- it should work even with older rdoc (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-4
- fix build requires (msuchy@redhat.com)

* Thu Aug 09 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-3
- fix filelist (msuchy@redhat.com)

* Thu Aug 09 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-2
- new package built with tito
