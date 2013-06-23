%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fssm

Summary: File system state monitor
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.2.7
Release: 6%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/ttilley/fssm
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
The File System State Monitor keeps track of the state of any number of paths
and will fire events when said state changes (create/update/delete).
FSSM supports using FSEvents on MacOS (with ruby 1.8), Inotify on GNU/Linux,
and polling anywhere else. 


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

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
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm %{buildroot}/%{gem_instdir}/.gitignore

%check
pushd .%{gem_instdir}

# Remove Bundler dependency
sed -i '4,+1d' spec/spec_helper.rb

%{?scl:scl enable %{scl} "}
rspec spec/
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/lib/
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.markdown
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%{gem_instdir}/example.rb
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/profile/
%{gem_instdir}/spec/
%doc %{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.7-6
- use rspec instead of rspec-core (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.7-5
- BR rubygems-devel (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.7-4
- new package built with tito

* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.7-3
- initial build

* Tue Dec 13 2011 Vít Ondruch <vondruch@redhat.com> - 0.2.7-1
- Update to fssm 0.2.7.

* Tue Apr 05 2011 Vít Ondruch <vondruch@redhat.com> - 0.2.6.1-1
- Updated to fssm 0.2.6.1
- Removed obsolete BuildRoot.
- Removed unnecessary cleanup.
- Testsuite executed using RSpec 2.x.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 07 2011 Vít Ondruch <vondruch@redhat.com> - 0.2.2-3
- Removed explicit RubyGems version

* Fri Dec 17 2010 Vít Ondruch <vondruch@redhat.com> - 0.2.2-2
- Documentation moved into subpackage

* Fri Dec 17 2010 Vít Ondruch <vondruch@redhat.com> - 0.2.2-1
- Initial package
