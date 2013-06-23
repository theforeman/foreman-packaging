%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name transaction-simple

Summary: Simple object transaction support for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.4.0.2
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: http://trans-simple.rubyforge.org/
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Transaction::Simple provides a generic way to add active transaction support
to objects. The transaction methods added by this module will work with most
objects, excluding those that cannot be Marshal-ed (bindings, procedure
objects, IO instances, or singleton objects).

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
sed -i '/s.cert_chain = nil/d' %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p .%{gem_dir}

%{?scl:scl enable %{scl} "}
# Create the gem as gem install only works on a gem file
%{?scl:"}
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

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
mv %{buildroot}%{gem_instdir}/{History.rdoc,Licence.rdoc,README.rdoc,Manifest.txt} ./
rm -rf %{buildroot}%{gem_instdir}/.yardoc
rm %{buildroot}%{gem_instdir}/.gemtest
chmod a-x %{buildroot}%{gem_instdir}/test/test_broken_graph.rb

%check
%{?scl:scl enable %{scl} "}
testrb -Ilib test/test_*.rb
%{?scl:"}

%files
%doc Licence.rdoc
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
#https://github.com/halostatue/transaction-simple/issues/4
%exclude %{gem_instdir}/research

%files doc
%doc History.rdoc README.rdoc Manifest.txt
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Fri Mar 01 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.0.2-4
- new package built with tito

* Fri Aug 17 2012 Miroslav Suchý <msuchy@redhat.com> 1.4.0.2-3
- 847457 - test script do not have shebang anymore (msuchy@redhat.com)
- 847457 - home page of transaction-simple changed (msuchy@redhat.com)
- 847457 - remove dot files consistently (msuchy@redhat.com)

* Thu Aug 16 2012 Miroslav Suchý <msuchy@redhat.com> 1.4.0.2-2
- fix changes after rebase (msuchy@redhat.com)
- setup.rb do not exist anymore (msuchy@redhat.com)

* Thu Aug 16 2012 Miroslav Suchý <msuchy@redhat.com> 1.4.0.2-1
- rebase to transaction-simple 1.4.0.2 (msuchy@redhat.com)
- 847457 - drop cert_chain completly (msuchy@redhat.com)
- 847457 - set executable bit on scripts (msuchy@redhat.com)
- 847457 - mark gem_docdir as as %%doc (msuchy@redhat.com)
- 847457 - remove CONFIGURE_ARGS (msuchy@redhat.com)
- 847457 - move some files to -doc package and exclude gem_cache
  (msuchy@redhat.com)
- 847457 - gem hoe is not needed (msuchy@redhat.com)
- 847457 - use global instead of define (msuchy@redhat.com)

* Sat Aug 11 2012 Miroslav Suchý <msuchy@redhat.com> 1.4.0-8
- change license to MIT (msuchy@redhat.com)
- use test suite (msuchy@redhat.com)
- fix filelist (msuchy@redhat.com)
- remove yardoc (msuchy@redhat.com)
- wrap description to 80 chars (msuchy@redhat.com)
- use macros (msuchy@redhat.com)
- buildroot is not needed (msuchy@redhat.com)
- mv transaction-simple.spec rubygem-transaction-simple.spec
  (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.4.0-7
- cert_chain could not be nil (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.4.0-6
- edit spec for Fedora 17 (msuchy@redhat.com)

* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 1.4.0-5
- rebuild

* Thu Oct 27 2011 Shannon Hughes <shughes@redhat.com> 1.4.0-4
- fixing version to match gem (shughes@redhat.com)

* Thu Oct 27 2011 Shannon Hughes <shughes@redhat.com> 1.4.2-1
- add dep for rubygem-hoe (shughes@redhat.com)

* Thu Oct 27 2011 Shannon Hughes <shughes@redhat.com>
- add dep for rubygem-hoe (shughes@redhat.com)

* Wed Oct 12 2011 Shannon Hughes <shughes@redhat.com> 1.4.0-3
- fixing tag (shughes@redhat.com)
- fix up gem version and tags (shughes@redhat.com)

* Wed Oct 12 2011 Shannon Hughes <shughes@redhat.com>
- fix up gem version and tags (shughes@redhat.com)

* Wed Oct 12 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.4.1-1
- Automatic commit of package [rubygem-transaction-simple] release [1.4.0-2].
  (dmitri@redhat.com)
- bumped up the version on transaction-simple.spec (dmitri@redhat.com)
- fixed transaction-simple spec file (dmitri@redhat.com)
- Automatic commit of package [rubygem-transaction-simple] release [1.4.0-1].
  (dmitri@redhat.com)

* Wed Oct 12 2011 Dmitri Dolguikh <dmitri@redhat.com>
- Automatic commit of package [rubygem-transaction-simple] release [1.4.0-2].
  (dmitri@redhat.com)
- bumped up the version on transaction-simple.spec (dmitri@redhat.com)
- fixed transaction-simple spec file (dmitri@redhat.com)
- Automatic commit of package [rubygem-transaction-simple] release [1.4.0-1].
  (dmitri@redhat.com)

* Tue Oct 11 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.4.0-2
- bumped up the version on transaction-simple.spec (dmitri@redhat.com)
- fixed transaction-simple spec file (dmitri@redhat.com)

* Tue Oct 11 2011 Dmitri Dolguikh <dmitri@redhat.com>
- fixed transaction-simple spec file (dmitri@redhat.com)

* Tue Oct 11 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.4.0-1
- new package built with tito

* Tue Oct 11 2011  <wb@killing-time.appliedlogic.ca> - 1.4.0-1
- Initial package
