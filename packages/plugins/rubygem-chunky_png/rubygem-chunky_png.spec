%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name chunky_png

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.10
Release: 1%{?dist}
Summary: Pure ruby library for read/write, chunk-level access to PNG files
Group: Development/Languages
License: MIT
URL: https://wiki.github.com/wvanbergen/chunky_png
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This pure Ruby library can read and write PNG images without depending on an
external image library, like RMagick. It tries to be memory efficient and
reasonably fast.  It supports reading and writing all PNG variants that are
defined in the specification, with one limitation: only 8-bit color depth is
supported. It supports all transparency, interlacing and filtering options the
PNG specifications allows. It can also read and write textual metadata from PNG
files. Low-level read/write access to PNG chunks is also possible.  This
library supports simple drawing on the image canvas and simple operations like
alpha composition and cropping. Finally, it can import from and export to
RMagick for interoperability.  Also, have a look at OilyPNG at
http://github.com/wvanbergen/oily_png. OilyPNG is a drop in mixin module that
implements some of the ChunkyPNG algorithms in C, which provides a massive
speed boost to encoding and decoding.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_instdir}/benchmarks
%exclude %{gem_instdir}/chunky_png.gemspec
%{gem_libdir}
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/BENCHMARKING.rdoc
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/CONTRIBUTING.rdoc
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
