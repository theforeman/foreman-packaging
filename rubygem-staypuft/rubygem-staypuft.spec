%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name staypuft

%define _version 0.3.9
%define _summary OpenStack Foreman Installer
%define _url https://github.com/theforeman/staypuft
%define _license GPLv3

%define desc OpenStack Foreman Installer

%if "%{?scl}" == "ruby193"
    %global scl_prefix %{scl}-
    %global scl_ruby /usr/bin/ruby193-ruby
    %global scl_rake /usr/bin/ruby193-rake
%else
    %global scl_ruby /usr/bin/ruby
    %global scl_rake /usr/bin/rake
%endif

Requires: %{?scl_prefix}rubygem(foreman_discovery)
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.6.4
Requires: %{?scl_prefix}rubygem(wicked)
Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(dynflow) >= 0.7.0

%if 0%{?rhel} == 6 || 0%{?fedora} < 17
%if "%{?scl}" == "ruby193"
%define rubyabi 1.9.1
%else
%define rubyabi 1.8
%endif
%else
%define rubyabi 1.9.1
%endif

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d


%if 0%{?rhel} == 6 &&  "%{?scl}" != "ruby193"
%global gem_dir %(ruby -rubygems -e 'puts Gem.dir' 2>/dev/null)
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_libdir %{gem_dir}/gems/%{gem_name}-%{version}/lib
%endif

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   %{_version}
Release:   1%{?dist}  
Summary:   %{_summary}
Group:     Development/Languages
License:   %{_license}
URL:       %{_url}
Source0:   http://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides:  foreman-plugin-staypuft

%if 0%{?fedora} > 18 || 0%{?rhel} > 6
Requires:  %{?scl_prefix}ruby(release)
%else 
Requires:  %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires:  %{?scl_prefix}rubygems

%if 0%{?fedora} || "%{?scl}" == "ruby193"
BuildRequires: %{?scl_prefix}rubygems-devel
%endif
%if 0%{?fedora} > 18 || 0%{?rhel} > 6
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: foreman
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem(sass-rails)
BuildRequires: %{?scl_prefix}rubygem(uglifier)
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks)
BuildRequires: %{?scl_prefix}rubygem(foreman_discovery)
BuildRequires: %{?scl_prefix}rubygem(wicked)

%description
%{desc}

%package   doc
BuildArch: noarch
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:   Documentation for %{pkg_name}

%description doc
This package contains documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%if 0%{?fedora} > 18
%gem_install
%else
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install -V --local --install-dir .%{gem_dir} --force --rdoc \
    %{gem_name}-%{version}.gem
%{?scl:"}
%endif

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}


# compile <assets>
mkdir -p ./usr/share
cp -r %{foreman_dir} ./usr/share || echo 0

pushd ./usr/share/foreman
export GEM_PATH=%{gem_dir}:%{buildroot}%{gem_dir}
cat <<GEMFILE > ./bundler.d/%{gem_name}.rb
group :%{gem_name} do
  gem '%{gem_name}'
  gem 'sass-rails'
  gem 'bootstrap-sass'
  gem 'jquery-ui-rails'
end
GEMFILE
cat ./bundler.d/%{gem_name}.rb

unlink tmp

export BUNDLER_EXT_NOSTRICT=1
export BUNDLER_EXT_GROUPS="default assets %{gem_name}"
%{scl_rake} plugin:assets:precompile[%{gem_name}] RAILS_ENV=production --trace

popd
rm -rf ./usr
# </assets>

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/%{gem_name}.rb
group :%{gem_name} do
  gem '%{gem_name}'
end
GEMFILE

%files 
%dir %{gem_instdir}
%exclude %{gem_cache}
%{gem_spec}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/db
%{gem_instdir}/config
%{gem_instdir}/public
%{gem_instdir}/Rakefile
%{foreman_bundlerd_dir}/staypuft.rb
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_instdir}/test
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}/rdoc
%doc %{gem_docdir}/ri

%changelog
* Wed Sep 10 2014 Marek Hulan <mhulan@redhat.com> 0.3.4-1
- Update staypuft to 0.3.4 (mhulan@redhat.com)

* Tue Sep 09 2014 Marek Hulan <mhulan@redhat.com> 0.3.2-1
- Update staypuft to 0.3.2 (mhulan@redhat.com)

* Thu Sep 04 2014 Marek Hulan <mhulan@redhat.com> 0.3.1-1
- Update staypuft to 0.3.1 (mhulan@redhat.com)

* Mon Aug 25 2014 Marek Hulan <mhulan@redhat.com> 0.3.0-1
- new package built with tito

* Tue Jul 22 2014 Marek Hulan <mhulan@redhat.com> 0.1.19-1
- Update staypuft (mhulan@redhat.com)

* Tue Jul 22 2014 Marek Hulan <mhulan@redhat.com> 0.1.18-1
- Update staypuft (mhulan@redhat.com)

* Wed Jul 16 2014 Marek Hulan <mhulan@redhat.com> 0.1.17-1
- Update staypuft (mhulan@redhat.com)

* Thu Jul 10 2014 Marek Hulan <mhulan@redhat.com> 0.1.9-1
- Update staypuft (mhulan@redhat.com)

* Thu Jul 03 2014 Marek Hulan <mhulan@redhat.com> 0.1.7-1
- Update staypuft (mhulan@redhat.com)

* Fri Jun 27 2014 Marek Hulan <mhulan@redhat.com> 0.1.5-2
- Add staypuft deps (mhulan@redhat.com)

* Thu Jun 26 2014 Marek Hulan <mhulan@redhat.com> 0.1.5-1
- Update staypuft (mhulan@redhat.com)

* Thu Jun 19 2014 Marek Hulan <mhulan@redhat.com> 0.1.4-2
- Update release (mhulan@redhat.com)
- Add missing gem (mhulan@redhat.com)

* Thu Jun 19 2014 Marek Hulan <mhulan@redhat.com> 0.1.4-1
- Update staypuft (mhulan@redhat.com)

* Mon Jun 16 2014 Marek Hulan <mhulan@redhat.com> 0.1.3-1
- Update staypuft (mhulan@redhat.com)

* Fri Jun 13 2014 Marek Hulan <mhulan@redhat.com> 0.1.2-1
- Update staypuft (mhulan@redhat.com)

* Fri Jun 06 2014 Marek Hulan <mhulan@redhat.com> 0.1.1-1
- Update staypuft to 0.1.1 (mhulan@redhat.com)

* Wed Jun 04 2014 Marek Hulan <mhulan@redhat.com> 0.1.0-1
- Update staypuft to 0.1.0 (mhulan@redhat.com)

* Thu May 22 2014 Marek Hulan <mhulan@redhat.com> 0.0.16-1
- Update staypuft (mhulan@redhat.com)

* Thu May 22 2014 Marek Hulan <mhulan@redhat.com> 0.0.15-1
- Update staypuft (mhulan@redhat.com)

* Tue May 20 2014 Marek Hulan <mhulan@redhat.com> 0.0.14-1
- Staypuft update (mhulan@redhat.com)

* Thu May 15 2014 Marek Hulan <mhulan@redhat.com> 0.0.13-1
- Update staypuft to 0.0.13 (mhulan@redhat.com)

* Fri May 02 2014 Marek Hulan <mhulan@redhat.com> 0.0.12-1
- Update staypuft (mhulan@redhat.com)

* Wed Apr 23 2014 Marek Hulan <mhulan@redhat.com> 0.0.11-5
- Update staypuft to official 0.0.11 (mhulan@redhat.com)

* Tue Apr 22 2014 Eric D. Helms <ericdhelms@gmail.com> 0.0.11-4
- Staypuft update to 0.0.11 (ericdhelms@gmail.com)

* Tue Apr 22 2014 Marek Hulan <mhulan@redhat.com> 0.0.10-3
- Update staypuft gem to released version (mhulan@redhat.com)

* Mon Apr 21 2014 Eric D. Helms <ericdhelms@gmail.com> 0.0.10-2
- Staypuft update to 0.0.10 (ericdhelms@gmail.com)

* Tue Apr 15 2014 Marek Hulan <mhulan@redhat.com> 0.0.9-1
- Staypuft update to 0.0.9 (mhulan@redhat.com)

* Mon Apr 14 2014 Marek Hulan <mhulan@redhat.com> 0.0.8-1
- Update staypuft to 0.0.8 (mhulan@redhat.com)

* Thu Apr 10 2014 Marek Hulan <mhulan@redhat.com> 0.0.7-1
- Update staypuft (mhulan@redhat.com)

* Thu Apr 10 2014 Marek Hulan <mhulan@redhat.com> 0.0.6-1
- Update staypuft (mhulan@redhat.com)

* Tue Apr 08 2014 Marek Hulan <mhulan@redhat.com> 0.0.4-3
- Fix requirement for packaged staypuft gemfile (mhulan@redhat.com)

* Tue Apr 08 2014 Marek Hulan <mhulan@redhat.com> 0.0.4-2
- Fix staypuft doc dependency (mhulan@redhat.com)
- Add foreman-plugin-staypuft provides (dcleal@redhat.com)
- Remove superfluous quotes (dcleal@redhat.com)

* Tue Apr 08 2014 Marek Hulan <mhulan@redhat.com> 0.0.4-1
- Update staypuft to 0.0.4 (mhulan@redhat.com)
- Precompile assets of staypuft (mhulan@redhat.com)

* Mon Apr 07 2014 Marek Hulan <mhulan@redhat.com> 0.0.3-1
- Update staypuft to 0.0.3 (mhulan@redhat.com)

* Fri Apr 04 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-4
- Hopefully last hack staypuft 0.0.2 version (mhulan@redhat.com)

* Fri Apr 04 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-3
- Another hacked version of staypuft (mhulan@redhat.com)

* Fri Apr 04 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-2
- Hacked staypuft version without oj dependency (mhulan@redhat.com)

* Fri Apr 04 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-1
- Update staypuft to 0.0.2 (mhulan@redhat.com)

* Wed Apr 02 2014 Marek Hulan <mhulan@redhat.com> 0.0.1-2
- Integrate staypuft into foreman (mhulan@redhat.com)

* Wed Apr 02 2014 Marek Hulan <mhulan@redhat.com> 0.0.1-1
- new package built with tito


