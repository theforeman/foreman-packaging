%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name chunky_png

Summary: Pure ruby library for read/write, chunk-level access to PNG files
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.0
Release: 7%{?dist}
Group: Development/Languages
License: MIT
URL: http://wiki.github.com/wvanbergen/chunky_png
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

Requires: %{?scl_prefix}rubygem(rake) >= 0

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This pure Ruby library can read and write PNG images without depending on
an external image library, like RMagick. It tries to be memory efficient and
reasonably fast.
It supports reading and writing all PNG variants that are defined in the
specification, with one limitation: only 8-bit color depth is supported. It
supports all transparency, interlacing and filtering options the PNG
specifications allows. It can also read and write textual metadata from PNG
files. Low-level read/write access to PNG chunks is also possible.
This library supports simple drawing on the image canvas and simple operations
like alpha composition and cropping. Finally, it can import from and export to
RMagick for interoperability.
Also, have a look at OilyPNG at http://github.com/wvanbergen/oily_png. OilyPNG
is a drop in mixin module that implements some of the ChunkyPNG algorithms in C,
which provides a massive speed boost to encoding and decoding.

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} --force --rdoc %{SOURCE0}
%{?scl:"}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 1.2.0-7
- fixing ruby193 scl package (lzap+git@redhat.com)

* Wed Mar 06 2013 Lukas Zapletal <lzap+git@redhat.com> 1.2.0-6
- new package built with tito

* Wed Mar 06 2013 Lukas Zapletal <lzap+git@redhat.com> 1.2.0-5
- new package built with tito

* Wed Mar 06 2013 Lukas Zapletal <lzap+git@redhat.com> 1.2.0-4
- fixing chunky_png
- require ruby193-build for tagging

* Mon Feb 25 2013 Miroslav Suchý <msuchy@redhat.com> 1.2.0-3
- new package built with tito

* Mon Jul 25 2011 Shannon Hughes <shughes@redhat.com> 1.2.0-2
- new package built with tito

* Fri Jul 22 2011 Shannon Hughes <shughes@redhat.com> - 1.2.0-2
- cleanup package
* Fri Jul 08 2011 Chris Lalancette <clalance@redhat.com> - 1.2.0-1
- Initial package
