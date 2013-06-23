# vim: sw=4:ts=4:et
#
# Copyright 2011 Red Hat, Inc.
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name alchemy

%define rubyabi 1.9.1

Name:          %{?scl_prefix}rubygem-%{gem_name}
Summary:       Mixing up the best that web technologies have to offer.
Group:         Applications/System
License:       MIT
Version:       1.0.1
Release:       5%{?dist}
URL:           http://www.ui-alchemy.org
Source0:       %{pkg_name}-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       %{?scl_prefix}rubygems
Requires:       %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires:  %{?scl_prefix}rubygems-devel
BuildRequires:  %{?scl_prefix}rubygems

Requires:       %{?scl_prefix}rubygem(compass)

BuildArch:      noarch

Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A Rails engine providing a set of web assets.

%prep
%setup -n %{pkg_name}-%{version} -q

%build
%{?scl:scl enable %{scl} - << \EOF}
LANG=en_US.utf-8 gem build %{gem_name}.gemspec
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} "}
gem install \
     --local \
     --install-dir %{buildroot}%{gem_dir} \
     --force \
     %{gem_name}-%{version}.gem
%{?scl:"}

mkdir -p %{buildroot}%{gem_dir}

rm -rf %{buildroot}%{gem_instdir}/.yardoc

%files
%dir %{gem_instdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/lib
%{gem_instdir}/app
%{gem_instdir}/vendor
%exclude %{gem_cache}
%exclude %{gem_instdir}/test
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md


%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}

%files doc
%doc %{gem_docdir}

%changelog
* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 1.0.1-5
- fixing alchemy (lzap+git@redhat.com)

* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 1.0.1-4
- fixing alchemy (lzap+git@redhat.com)

* Wed Mar 06 2013 Lukas Zapletal <lzap+git@redhat.com> 1.0.1-3
- fixing alchemy
- require ruby193-build for tagging

* Mon Feb 25 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.1-2
- new package built with tito

* Tue Jan 15 2013 Eric D Helms <ehelms@redhat.com> 1.0.1-1
- Spec - Updates to use any version of compass available. (ehelms@redhat.com)
- Added default to component variables + fixed btn primary color at hover
  (jcoufal@redhat.com)
- Templates - Updates to make templates more usuable outside alchemy.
  (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)
- Removes the jquery ui development bundle. (ehelms@redhat.com)
- Encoding - A character exists in the comments that causes Rails asset
  pipeline to explode. (ehelms@redhat.com)
- SCSS - Moves from relative pathing in SCSS imports to be based off the
  alchemy namespacing for proper imports by parent applications using the
  engine. (ehelms@redhat.com)
- Removing redundant string. (jrist@redhat.com)
- Fix for get_string to translate for gettext properly (jrist@redhat.com)

* Thu Dec 06 2012 Eric D Helms <ehelms@redhat.com> 1.0.0-1
- new package built with tito

