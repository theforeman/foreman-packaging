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

%global gem_name ui_alchemy-rails
%global rubyabi 1.9.1


Name:          %{?scl_prefix}rubygem-%{gem_name}
Summary:       Mixing up the best that web technologies have to offer.
Group:         Applications/System
License:       MIT
Version:       1.0.4
Release:       3%{?dist}
URL:           http://www.ui-alchemy.org
Source0:       %{?scl_prefix}%{pkg_name}-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires:       %{?scl_prefix}ruby(rubygems) 
Requires:       %{?scl_prefix}rubygem(compass)
BuildRequires:  %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires:  %{?scl_prefix}ruby(rubygems) 
BuildRequires:  %{?scl_prefix}rubygems-devel
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A Rails engine providing a set of web assets.

%prep
%setup -n %{?scl_prefix}%{pkg_name}-%{version} -q

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
* Wed Apr 10 2013 Marek Hulan <ares@igloonet.cz> 1.0.4-3
- Fixed SCL prefixes

* Wed Apr 10 2013 Marek Hulan <ares@igloonet.cz> 1.0.4-3
- Fixed build root

* Tue Apr 09 2013 Marek Hulan <ares@igloonet.cz> 1.0.4-2
- fix name of tarball

* Tue Apr 09 2013 Marek Hulan <ares@igloonet.cz> 1.0.4-1
- SCL package built with tito

* Tue Apr 09 2013 Marek Hulan <ares@igloonet.cz> 1.0.4-1
- new package built with tito

* Tue Apr 09 2013 Marek Hulan <ares@igloonet.cz> 1.0.4-2
- SCL package built with tito

* Tue Apr 09 2013 Marek Hulan <ares@igloonet.cz> 1.0.4-2
- SCL package built with tito

* Tue Apr 09 2013 Marek Hulan <ares@igloonet.cz> 1.0.4-2
- SCL version of package built with tito

* Fri Mar 29 2013 Eric D Helms <ehelms@redhat.com> 1.0.4-1
- new package built with tito

* Thu Mar 28 2013 Eric D Helms <ehelms@redhat.com> 1.0.3-1
- Bumping to meet gem version.

* Thu Mar 28 2013 Eric D Helms <ehelms@redhat.com> 1.0.2-1
- Version bump. (ehelms@redhat.com)
- Merge pull request #151 from ehelms/flot-cleanup (ericdhelms@gmail.com)
- Removes Flot development cruft. (ehelms@redhat.com)
- Fix chosen-sprite relative path (hbrock@redhat.com)
- Merge pull request #147 from abenari/select (ericdhelms@gmail.com)
- Updates Normalize to the most recent version. (ehelms@redhat.com)
- Adds HandlebarsJS templating library (ehelms@redhat.com)
- make select box the same size and same border and background color as the
  edit box. (abenari@redhat.com)
- fixed latest comments. (abenari@redhat.com)
- Moves engine declaration into explicit file. Adds helper functions for
  stylesheets and javascript to ensure child views declaring a stylesheet or
  javascript requirement are appended. (ehelms@redhat.com)
- added danger button (jcoufal@redhat.com)
- Merge pull request #145 from abenari/minor-fixes (email@jaromircoufal.cz)
- Merge pull request #142 from mbacovsky/login_screen_padding
  (email@jaromircoufal.cz)
- fixed fieldset lable width. (abenari@redhat.com)
- removed clear after btn-group, because it brakes multiple btn-group in a
  single toolbar (abenari@redhat.com)
- seting the login logo size (abenari@redhat.com)
- fix image re-size for the logo. This fix enables using a large image for the
  logo that looks good in close-up. (abenari@redhat.com)
- Added btn-success (abenari@redhat.com)
- added support for single button in a button group (abenari@redhat.com)
- fixed var usage in url (abenari@redhat.com)
- added aliases for bootstrap compatibility: primary, btn-primary warning, btn-
  warning btn_group, btn-group lable, control-lable (abenari@redhat.com)
- Update alchemy.gemspec (jtomasek@redhat.com)
- make colors default in order to be easily overwritten (jcoufal@redhat.com)
- Avoid footer overlaping over login form on narrow screen
  (mbacovsk@redhat.com)
- Merge pull request #141 from xsuchy/pull-req-f18 (jrist@redhat.com)
- Version bump. (ehelms@redhat.com)
- allow to build under F18 (msuchy@redhat.com)
- Adds Media object as a component. (ehelms@redhat.com)

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

