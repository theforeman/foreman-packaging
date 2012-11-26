# Generated from ruby-libvirt-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-libvirt
%global rubyabi 1.9.1

Summary: Ruby bindings for LIBVIRT
Name: rubygem-%{gem_name}
Version: 0.4.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://libvirt.org/ruby/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby >= 1.8.1
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby >= 1.8.1
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby bindings for libvirt.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local --install-dir .%{gem_dir} \
            -V \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir}/lib
# TODO: move the extensions
##mv %{buildroot}%{gem_instdir}/lib/shared_object.so %{buildroot}%{gem_extdir}/lib/



# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{geminstdir}/ext

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems/gems/ruby-libvirt-0.4.0/
%files doc
%doc %{gem_docdir}

%changelog
* Thu Jun 14 2012 jason - 0.4.0-1
- Initial package
