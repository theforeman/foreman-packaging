# template: default
%global gem_name concurrent-ruby-edge

Name: rubygem-%{gem_name}
Version: 0.7.2
Release: 1%{?dist}
Summary: Edge features and additions to the concurrent-ruby gem
License: MIT
URL: https://www.concurrent-ruby.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3
BuildRequires: ruby >= 2.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
These features are under active development and may change frequently. They
are expected not to
keep backward compatibility (there may also lack tests and documentation).
Semantic versions will
be obeyed though. Features developed in `concurrent-ruby-edge` are expected to
move to `concurrent-ruby` when final.
Please see http://concurrent-ruby.com for more information.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Oct  7 04:28:05 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 1:0.7.2-1
- Update to 0.7.2

* Mon Jul 27 2026 Zach Huntington-Meath <zhunting@redhat.com> - 1:0.6.0-5
- Rebuild for EL10

* Wed Jun 04 2025 Zach Huntington-Meath <zhunting@redhat.com> - 1:0.6.0-4
- Removed unversioned obsoletes

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1:0.6.0-3
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1:0.6.0-2
- Bump to release for EL8

* Wed Mar 04 2020 Adam Ruzicka <aruzicka@redhat.com> 1:0.6.0-1
- Update to 0.6.0

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1:0.4.1-2
- Update spec to remove the ror scl

* Fri Jan 04 2019 Ivan Nečas <inecas@redhat.com> 1:0.4.1-1
- Update to 0.4.1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1:0.2.4-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Jan 04 2018 Eric D. Helms <ericdhelms@gmail.com> 0.2.4-1
- Bump concurrent-ruby-edge to 0.2.4 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue Mar 21 2017 Dominic Cleal <dominic@cleal.org> 0.2.3-1
- Update dynflow to 0.8.21 (me@daniellobato.me)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.2.0-4
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.2.0-3
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Jan 05 2016 Dominic Cleal <dcleal@redhat.com> 0.2.0-2
- Add foremandist to plugin dependencies (dcleal@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- Update concurrent-ruby-edge to 0.2.0 (stbenjam@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-5
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-4
- Package concurrent-ruby for non-SCL el7 (stbenjam@redhat.com)

* Thu Aug 06 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-3
- Fix dep to include epoch between -doc and main package (dcleal@redhat.com)

* Wed Aug 05 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-2
- Increase the epoch number for the concurrent-ruby gems (inecas@redhat.com)

* Mon Aug 03 2015 Ivan Nečas <inecas@redhat.com> 0.1.0-1
- Update concurrent-ruby-edge to 0.1.0 (inecas@redhat.com)
- Automatic commit of package [rubygem-concurrent-ruby-edge] minor release
  [0.1.0.pre3-1]. (dcleal@redhat.com)
- Initial build of concurrent-ruby library (inecas@redhat.com)

* Thu Jul 02 2015 Ivan Nečas <inecas@redhat.com>
- new package built with tito
