%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name pdf-reader

Summary: Ruby library to parse PDF files
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.1
Release: 7%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/yob/pdf-reader
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
# git clone git://github.com/yob/pdf-reader.git && cd pdf-reader/
# git archive --format=tar --prefix=spec/ 3121f26db2:spec | gzip > pdf-reader-spec.tar-1.1.1.gz
Source1: pdf-reader-spec-%{version}.tar.gz
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
%if 0%{?fedora} > 16
BuildRequires: %{?scl_prefix}rubygem-rspec
%endif
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Requires: %{?scl_prefix}rubygem(Ascii85) >= 1.0.0
Requires: %{?scl_prefix}rubygem(Ascii85) < 1.1.0
BuildRequires: %{?scl_prefix}rubygem(Ascii85) >= 1.0.0
BuildRequires: %{?scl_prefix}rubygem(Ascii85) < 1.1.0
Requires: %{?scl_prefix}rubygem(ruby-rc4)
BuildRequires: %{?scl_prefix}rubygem(ruby-rc4)
BuildRequires: %{?scl_prefix}rubygem(minitest)

%description
The PDF::Reader library implements a PDF parser conforming as much as possible
to the PDF specification from Adobe.

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
tar -xzf %{SOURCE1}

%build
mkdir -p .%{gem_dir}

%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --bindir ./%{_bindir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

mv %{buildroot}%{gem_instdir}/{TODO,README.rdoc,MIT-LICENSE,CHANGELOG} ./
rm -rf %{buildroot}%{gem_instdir}/.yardoc

chmod a+x %{buildroot}%{gem_instdir}/examples/*.rb

%check
%if 0%{?fedora} > 16
cp -pr spec/ ./%{gem_instdir}
pushd ./%{gem_instdir}
sed -i '/require.*bundler/d' spec/spec_helper.rb
sed -i '/Bundler.setup/d' spec/spec_helper.rb
%{?scl:scl enable %{scl} "}
rspec spec
%{?scl:"}
rm -rf spec
popd
%endif

%files
%{_bindir}/pdf_*
%doc MIT-LICENSE
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/bin
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc README.rdoc TODO CHANGELOG
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/examples

%changelog
* Fri Mar 01 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.1-7
- new package built with tito

* Wed Sep 05 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-6
- 850679 - add rubygem(minitest) to BR (msuchy@redhat.com)
- 850679 - include version in file name with spec tests (msuchy@redhat.com)

* Mon Sep 03 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-5
- 850679 - run test suite (msuchy@redhat.com)
- 850679 - flag examples as executables (msuchy@redhat.com)

* Thu Aug 23 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-4
- 850679 - add rubygems to BR (msuchy@redhat.com)
- 850679 - fix BR and do not remove %%{gem_instdir}/bin (msuchy@redhat.com)

* Wed Aug 22 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-3
- add runtime dependencies (msuchy@redhat.com)

* Wed Aug 22 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-2
- new package built with tito

* Tue Aug 21 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-1
- new package built with tito

