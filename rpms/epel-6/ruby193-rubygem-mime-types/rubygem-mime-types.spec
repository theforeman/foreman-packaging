%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

# Generated from mime-types-1.16.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mime-types

%global rubyabi 1.9.1

Summary: Return the MIME Content-Type for a given filename
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.19
Release: 2%{?dist}
Group: Development/Languages
License: GPL+ or Ruby or Artistic
URL: http://mime-types.rubyforge.org/
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
MIME::Types for Ruby manages a MIME Content-Type database that will return the
Content-Type for a given filename.

MIME::Types was originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copyright 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
This package contains documentation for %{pkg_name}.

%prep
%setup -q -c -T

mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gem_dir} \
  --force --rdoc \
  %{SOURCE0}
%{?scl:"}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# These aren't executables
find %{buildroot}%{gem_instdir}/{Rakefile,test} -type f | \
  xargs -n 1 sed -i  -e '/^#! \/usr\/bin\/env .*/d'

%clean
rm -rf %{buildroot}

%check
pushd .%{gem_instdir}
%{?scl:scl enable %scl "}
# apply test fix from upstream:
# https://github.com/halostatue/mime-types/commit/134cab8ffdbd337bf0b8bb67b5097222f6f15769#diff-1
sed -i 's|linux|d9d172f608|' test/test_mime_type.rb
testrb -Ilib test/*
%{?scl:"}
popd

%files
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/Licence.rdoc
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/mime-types.gemspec
%doc %{gem_instdir}/Manifest.txt
%{gem_instdir}/test

%changelog
* Thu Feb 21 2013 Miroslav Suchý <msuchy@redhat.com> 1.19-2
- new package built with tito

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.19-1
- Update to Mime-Types 1.19.
- Specfile cleanup

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.18-1
- Rebuilt for scl.
- Updated to 1.18.

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.16-7
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 1.16-5
- Replace BR(check) with BR

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 30 2009 Matthew Kent <mkent@magoazul.com> - 1.16-3
- Remove needless rcov task in Rakefile causing issue (#544964).

* Sun Dec 27 2009 Matthew Kent <mkent@magoazul.com> - 1.16-2
- Fix license (#544964).
- Add note about rcov warning in test phase (#544964).

* Sun Dec 06 2009 Matthew Kent <mkent@magoazul.com> - 1.16-1
- Initial package
