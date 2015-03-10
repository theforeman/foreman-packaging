%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name safemode

Summary: A library for safe evaluation of Ruby code
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 1.2.2
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: http://github.com/svenfuchs/safemode
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(ruby2ruby) >= 2.0.6
Requires: %{?scl_prefix}rubygem(ruby_parser) >= 3.2.0
Requires: %{?scl_prefix}rubygem(sexp_processor) >= 4.3.0

BuildRequires: %{?scl_prefix}rubygems-devel
#BuildRequires: %{?scl_prefix}rubygem(jeweler) >= 1.8.3
BuildRequires: %{?scl_prefix}rubygem(rake)
BuildRequires: %{?scl_prefix}rubygem(rdoc)
BuildRequires: %{?scl_prefix}rubygems

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(safemode) = %{version}

%description
A library for safe evaluation of Ruby code based on RubyParser and Ruby2Ruby.
Provides Rails ActionView template handlers for ERB and Haml.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
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

%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:"}
rm -rf ./%{gem_dir}/gems/%{gem_name}-%{version}/.yardoc

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
mv %{buildroot}%{gem_instdir}/{LICENCSE,README.markdown} ./
rm %{buildroot}%{gem_instdir}/VERSION

%files
%doc LICENCSE
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/demo.rb
%{gem_instdir}/init.rb
%{gem_instdir}/safemode.gemspec
%{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/test
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%{gem_docdir}

%changelog
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

