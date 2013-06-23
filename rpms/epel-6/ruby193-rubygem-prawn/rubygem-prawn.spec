%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name prawn
%global rubyabi 1.9.1

%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{upstream_version}
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{upstream_version}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{upstream_version}.gemspec
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{upstream_version}

%global upstream_version 1.0.0.rc1

Summary: A fast and nimble PDF generator for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.0
Release: 5.rc1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://prawn.majesticseacreature.com
# downloaded from https://github.com/prawnpdf/prawn/zipball/master
Source0: %{gem_name}-1.0.0.24d9a57fd2.zip
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems) >= 1.3.6
Requires: %{?scl_prefix}ruby >= 1.8.7
Requires: %{?scl_prefix}rubygem(pdf-reader) >= 0.9.0
Requires: %{?scl_prefix}rubygem(ttfunk) => 1.0.2
Requires: %{?scl_prefix}rubygem(ttfunk) < 1.1
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel >= 1.3.6
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
#for tests
#BuildRequires: %{?scl_prefix}rubygem(test-spec)
#BuildRequires: %{?scl_prefix}rubygem(ttfunk)
#BuildRequires: %{?scl_prefix}rubygem(pdf-reader)
#BuildRequires: %{?scl_prefix}rubygem(mocha)

%description
Prawn is a pure Ruby PDF generation library that provides a lot of great functionality while trying to remain simple and reasonably performant. Here are some of the important features we provide:

 * Vector drawing support, including lines, polygons, curves, ellipses, etc.
 * Extensive text rendering support, including flowing text and limited inline formatting options.
 * Support for both PDF builtin fonts as well as embedded TrueType fonts
 * A variety of low level tools for basic layout needs, including a simple grid system
 * PNG and JPG image embedding, with flexible scaling options
 * Reporting tools for rendering complex data tables, with pagination support
 * Security features including encryption and password protection
 * Tools for rendering repeatable content (i.e headers, footers, and page numbers)
 * Comprehensive internationalization features, including full support for UTF-8 based fonts, right-to-left text rendering, fallback font support, and extension points for customizable text wrapping.
 * Support for PDF outlines for document navigation
 * Low level PDF features, allowing users to create custom extensions by dropping down all the way to the PDF object tree layer. (Mostly useful to those with knowledge of the PDF specification).

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -q -n  prawnpdf-prawn-24d9a57

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
        --bindir ./%{_bindir} \
        --force \
        --rdoc \
        %{gem_name}-1.0.0.rc1.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/.yardoc

%check
%if 0%{?fedora} > 16
pushd .%{gem_instdir}
#sed -i '/undler/d' spec/spec_helper.rb 
%{?scl:scl enable %{scl} "}
#rspec spec/*_spec.rb
%{?scl:"}
popd
%endif

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/data
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/GPLv2
%doc %{gem_instdir}/GPLv3
%{gem_instdir}/spec
%{gem_instdir}/manual
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.0-5.rc1
- new package built with tito

* Fri Oct 19 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.0-4.rc1
- properly define gem_dir on F17 (msuchy@redhat.com)

* Wed Sep 19 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.0-3.rc1
- macro gem_libdir is not available on el6 (msuchy@redhat.com)

* Tue Sep 18 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.0-2.rc1
- BR rubygems (msuchy@redhat.com)

* Tue Sep 18 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.0-1.rc1
- Build from upstream head (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.12.0-2
- initial release

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> - 0.12.0-1
- Initial package
