%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from pg-0.11.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name pg
%global rubyabi 1.9.1

Summary: A Ruby interface to the PostgreSQL RDBMS
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.12.2
Release: 8%{?dist}
Group: Development/Languages
# Upstream license clarification (https://bitbucket.org/ged/ruby-pg/issue/72/)
#
# The portions of the code that are BSD-licensed are licensed under
# the BSD 3-Clause license; the contents of the BSD file are incorrect.
#
License: (GPLv2 or Ruby) and BSD
URL: http://bitbucket.org/ged/ruby-pg/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix_ruby}ruby-devel
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: postgresql-server postgresql-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(rspec)
# Introduced in F17.
Obsoletes: %{?scl_prefix}ruby(postgres) <= 0.7.9-2010.01.28.2
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This is the extension library to access a PostgreSQL database from Ruby.
This library works with PostgreSQL 7.4 and later.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            -V --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{gem_extdir}/lib
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mv %{buildroot}%{gem_libdir}/pg_ext.so %{buildroot}%{gem_extdir}/lib

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext

# Remove useless shebangs.
sed -i -e '/^#!\/usr\/bin\/env/d' %{buildroot}%{gem_libdir}/pg.rb
sed -i -e '/^#!rake/d' %{buildroot}%{gem_instdir}/Rakefile

# Fix spec shebangs.
# https://bitbucket.org/ged/ruby-pg/issue/74/
for file in `find %{buildroot}%{gem_instdir}/spec -type f ! -perm /a+x -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ] \
        && sed -i -e 's/^#!\/usr\/bin\/env spec/#!\/usr\/bin\/env rspec/' $file \
        && chmod -v 755 $file
done

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} "}
#rspec spec
%{?scl:"}
popd

%files
%exclude %{gem_instdir}/.gemtest
%{gem_extdir}
%dir %{gem_instdir}
%doc %{gem_instdir}/BSD
%doc %{gem_instdir}/GPL
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/Contributors.rdoc
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/Manifest.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/Rakefile.cross
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/README.ja.rdoc
%doc %{gem_instdir}/README.OS_X.rdoc
%doc %{gem_instdir}/README.windows.rdoc
%{gem_instdir}/misc
%{gem_instdir}/sample
%{gem_instdir}/spec

%changelog
* Wed Mar 06 2013 Lukas Zapletal <lzap+git@redhat.com> 0.12.2-8
- disabling tests for ruby193-rubygem-pg

* Wed Mar 06 2013 Lukas Zapletal <lzap+git@redhat.com> 0.12.2-7
- importing rspec for pg

* Wed Mar 06 2013 Lukas Zapletal <lzap+git@redhat.com> 0.12.2-6
- new package built with tito

* Wed Mar 06 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.12.2-5
- rebuilt with prefix

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Vít Ondruch <vondruch@redhat.com> - 0.12.2-2
- Obsolete ruby-postgress, which was retired.

* Tue Jan 24 2012 Vít Ondruch <vondruch@redhat.com> - 0.12.2-1
- Rebuilt for Ruby 1.9.3.
- Upgrade to pg 0.12.2.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 03 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-5
- Pass CFLAGS to extconf.rb.

* Fri Jun 03 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-4
- Binary extension moved into ruby_sitearch dir.
- -doc subpackage made architecture independent.

* Wed Jun 01 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-3
- Quoted upstream license clarification.

* Mon May 30 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-2
- Removed/fixed shebang in non-executables.
- Removed sources.

* Thu May 26 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-1
- Initial package
