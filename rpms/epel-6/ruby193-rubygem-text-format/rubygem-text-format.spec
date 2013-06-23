%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name text-format

Summary: Text::Format formats fixed-width text nicely
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.0
Release: 8%{?dist}
Group: Development/Languages
License: Ruby
URL: http://rubyforge.org/projects/text-format
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

# text-hyphen currently has an ugly license situation
# (not necessarily unacceptable for Fedora, but needs
#  looking into, remove dependency for now)
Patch0: remove-text-hyphen-dep.patch

Requires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
BuildRequires: %{?scl_prefix}rubygem-minitest

%description
Text::Format is provides the ability to nicely format fixed-width text with
knowledge of the writeable space (number of columns), margins, and indentation
settings. Text::Format can work with either TeX::Hyphen or Text::Hyphen to
hyphenate words when formatting.


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            -V \
            --force --rdoc %{SOURCE0}
%{?scl:"}

pushd .%{gem_dir}
%patch0 -p0

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

# remove installer as its not needed
pushd %{buildroot}%{gem_instdir}
rm pre-setup.rb setup.rb metaconfig

# remove dos end of line encoding
tr -d '\r' < Rakefile > Rakefile.new
mv Rakefile.new Rakefile

iconv -f iso8859-1 -t utf-8 README > README.conv && mv -f README.conv README
pushd %{buildroot}%{gem_dir}
rm -f specifications/%{gem_name}-%{version}.gemspec.orig
popd

%check
pushd %{buildroot}%{gem_instdir} 
%{?scl:scl enable %{scl} "}
ruby tests/tc_*
%{?scl:"}

%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README
%doc %{gem_instdir}/Changelog
%doc %{gem_instdir}/Install
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/ToDo
%doc %{gem_instdir}/tests
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.0-8
- add BR rubygem(minitest) (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.0-7
- new package built with tito

* Mon Jul 02 2012 Lukas Zapletal <lzap+git@redhat.com> 1.0.0-6
- new package built with tito

* Thu Mar 22 2012 Steve Linabery <slinaber@redhat.com> - 1.0.0-5
- remove {gem_dir}/specifications/{gem_name}-{version}.gemspec.orig file as part of install

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Mo Morsi <mmorsi@redhat.com> - 1.0.0-3
- remove 'file-not-utf8' rpmlint error

* Tue Feb 01 2011 Mo Morsi <mmorsi@redhat.com> - 1.0.0-2
- Updates based on review feedback

* Tue Jan 11 2011 Mo Morsi <mmorsi@redhat.com> - 1.0.0-1
- Initial package
