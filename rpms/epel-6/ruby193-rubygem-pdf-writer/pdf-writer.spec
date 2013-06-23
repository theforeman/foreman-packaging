%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name pdf-writer

Summary: A pure Ruby PDF document creation library
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.8
Release: 7%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyforge.org/projects/ruby-pdf
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(transaction-simple) >= 1.3
Requires: %{?scl_prefix}rubygem(color) >= 1.4.0

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This library provides the ability to create PDF documents using only native Ruby libraries. There are several demo programs available in the demo/ directory. The canonical documentation for PDF::Writer is "manual.pdf", which can be generated using bin/techbook (just "techbook" for RubyGem users) and the manual file "manual.pwd".

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

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
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

# If there were programs installed:
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%{_bindir}/techbook
%{gem_dir}/gems/%{gem_name}-%{version}/

%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/LICENCE

%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.8-7
- new package built with tito

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.8-6
- cert_chain could not be nil (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.8-5
- do not generate gemspec (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.8-4
- edit spec for Fedora 17 (msuchy@redhat.com)

* Thu Oct 27 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.1.8-3
- added color and transaction-simple dependencies to pdf-writer spec
  (dmitri@redhat.com)

* Thu Oct 06 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.1.8-2
- bumped up the version of pdf-writer spec file (dmitri@redhat.com)

* Thu Oct 06 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.1.8-1
- new package built with tito

* Thu Oct 06 2011  <wb@killing-time.appliedlogic.ca> - 1.1.8-1
- Initial package
