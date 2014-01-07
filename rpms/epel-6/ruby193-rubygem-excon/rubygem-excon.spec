%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name excon

Summary: Http(s) EXtended CONnections
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.31.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/geemus/excon
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: ca-certificates
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: ca-certificates
# For the tests
#BuildRequires: %{?scl_prefix}rubygem(activesupport)
#BuildRequires: %{?scl_prefix}rubygem(delorean)
#BuildRequires: %{?scl_prefix}rubygem(open4)
#BuildRequires: %{?scl_prefix}rubygem(shindo)
#BuildRequires: %{?scl_prefix}rubygem(sinatra)
#BuildRequires: %{?scl_prefix}rubygem(eventmachine)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
EXtended http(s) CONnections

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# kill bundled cacert.pem
ln -sf /etc/pki/tls/cert.pem \
	%{buildroot}%{gem_instdir}/data/cacert.pem

%check
#pushd .%{gem_instdir}
## we need to remove the dependency on bundler and add the missing requires (workaround for not using the Rakefile)
## do not require bundler
#sed -i -e "s/'bundler'/'open4'\nrequire 'delorean'/" -e '/Bundler.require(:default, :development)/d' tests/test_helper.rb
#
## require the other needed libs
## https://github.com/geemus/excon/issues/135#issuecomment-7181061
#RUBYOPT="-r./lib/excon -rsecurerandom" shindo
#popd

%files
%dir %{gem_instdir}
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Gemfile.lock
%{gem_spec}
%doc %{gem_instdir}/README.md

%files doc
%{gem_instdir}/benchmarks
%{gem_instdir}/tests
%{gem_instdir}/excon.gemspec
%{gem_instdir}/Rakefile
%doc %{gem_docdir}
%doc %{gem_instdir}/changelog.txt

%changelog
* Tue Jan 07 2014 Dominic Cleal <dcleal@redhat.com> 0.31.0-1
- Rebase to excon 0.31.0 (dcleal@redhat.com)

* Wed Nov 06 2013 Dominic Cleal <dcleal@redhat.com> 0.28.0-1
- Rebase to excon 0.28.0 (dcleal@redhat.com)

* Tue Aug 13 2013 Dominic Cleal <dcleal@redhat.com> 0.25.3-2
- Don't use SCL prefixes on cacert.pem path (dcleal@redhat.com)

* Mon Jul 22 2013 Dominic Cleal <dcleal@redhat.com> 0.25.3-1
- Rebase to excon 0.25.3 (dcleal@redhat.com)

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 0.23.0-2
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Tue Jun 11 2013 Dominic Cleal <dcleal@redhat.com> 0.23.0-1
- Rebase to excon 0.23.0 (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Fri May 03 2013 Ivan Necas <inecas@redhat.com> 0.20.1-1
- Update the version due to Foreman dependency (inecas@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 0.14.3-3
- disable tests (msuchy@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 0.14.3-2
- new package built with tito

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.3-1
- Update to Excon 0.14.3.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.1-1
- Update to Excon 0.14.1
- Removed no longer needed patch for downgrading dependencies.
- Remove newly bundled certificates and link to system ones.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.5-2
- Fixed the changelog.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.5-1
- Update to version 0.9.5
- Fixed the dependencies for the new version.

* Mon Dec 05 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.12-1
- Update to version 0.7.12.

* Mon Nov 28 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.8-1
- Update to version 0.7.8.
- Replaced defines with more appropriate globals.
- Added Build dependency on rubygem-eventmachine.
- Fixed running tests for the new version.

* Wed Oct 12 2011 bkabrda <bkabrda@redhat.com> - 0.7.6-1
- Update to version 0.7.6
- Introduced doc subpackage
- Introduced check section

* Tue Jul 05 2011 Chris Lalancette <clalance@redhat.com> - 0.6.3-1
- Initial package
