%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rcov

Summary: Code coverage analysis tool for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.9.9
Release: 9%{?dist}
Group: Development/Languages
License: GPLv2 or Ruby
URL: http://github.com/relevance/rcov
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: %{?scl_prefix}ruby-devel, %{?scl_prefix}rubygem-rake
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
rcov is a code coverage tool for Ruby. It is commonly used for viewing overall
test unit coverage of target code.  It features fast execution (20-300 times
faster than previous tools), multiple analysis modes, XHTML and several kinds
of text reports, easy automation with Rake via a RcovTask, fairly accurate
coverage information through code linkage inference using simple heuristics,
colorblind-friendliness...

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
This package contains documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}
sed -i '1,$s/s.cert_chain = nil/s.cert_chain = []/' %{gem_name}.gemspec

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
  --force --rdoc \
  %{gem_name}-%{version}.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gem_dir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gem_dir}/bin
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Arch dependent files go here
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{gem_instdir}/lib/*.so %{buildroot}%{ruby_sitearchdir}

pushd %{buildroot}%{gem_instdir}/ext/rcovrt
  make clean
popd

# lib is for libraries
chmod 644 %{buildroot}%{gem_instdir}/lib/rcov/rcovtask.rb
sed -i -e '/^#!\/usr\/bin\/env ruby/d' \
  %{buildroot}%{gem_instdir}/lib/rcov/rcovtask.rb

find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'

rm -rf %{buildroot}/usr/share/gems/gems/%{gem_name}-%{version}/.yardoc

%files
%{_bindir}/rcov
%doc %{gem_instdir}/[A-Z]*
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_instdir}/lib
%{ruby_sitearchdir}/*.so
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%{gem_instdir}/Rakefile
%{gem_instdir}/setup.rb
%{gem_instdir}/doc
%{gem_instdir}/ext
%{gem_instdir}/test
%{gem_instdir}/editor-extensions
%{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.9.9-9
- new package built with tito

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.9.9-8
- define ruby_sitearchdir for Fedora16 (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.9.9-7
- fix build errors (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.9.9-6
- do not generate gemspec (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.9.9-5
- edit spec for Fedora 17 (msuchy@redhat.com)

* Fri Jul 22 2011 Shannon Hughes <shughes@redhat.com> 0.9.9-4
- new version after syntax corrections (shughes@redhat.com)
- remove build require syntax error (shughes@redhat.com)
- adding rcov as a dependency of mime-types (jsherril@redhat.com)
- removing test/dev gems from rpmbuilds (shughes@redhat.com)

* Thu Nov 11 2010 Shannon Hughes <shughes@redhat.com> 0.9.9-3
- new gem, 0.9.9 (shughes@redhat.com)

* Thu Nov 11 2010 Shannon Hughes <shughes@redhat.com>
- new gem, 0.9.9 (shughes@redhat.com)

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 0.9.8-3
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Matthew Kent <shughes@redhat.com> - 0.9.8-2
- Initial Kalpana version 

* Tue May 04 2010 Matthew Kent <mkent@magoazul.com> - 0.9.8-1
- New upstream version - fix for occasional SEGV.
- Enable tests.

* Thu Dec 03 2009 Matthew Kent <mkent@magoazul.com> - 0.9.6-2
- Remove Requires for rubygem(rake) (#543337).
- Move ext to -doc (#543337).

* Tue Dec 01 2009 Matthew Kent <mkent@magoazul.com> - 0.9.6-1
- Initial package
