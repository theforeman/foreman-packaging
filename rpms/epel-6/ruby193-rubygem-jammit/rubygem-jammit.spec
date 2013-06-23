%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name jammit

Summary: Industrial Strength Asset Packaging for Rails
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.6.5
Release: 10%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://documentcloud.github.com/jammit/
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}rubygem(yui-compressor) >= 0.9.1
Requires: %{?scl_prefix}rubygem(closure-compiler) >= 0.1.0
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Jammit is an industrial strength asset packaging library for Rails,
providing both the CSS and JavaScript concatenation and compression that
you'd expect, as well as YUI Compressor and Closure Compiler compatibility,
ahead-of-time gzipping, built-in JavaScript template support, and optional
Data-URI / MHTML image embedding.

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}
%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p ./%{gem_dir}
mkdir -p  ./%{_bindir}

%{?scl:scl enable %{scl} "}
# Create the gem as gem install only works on a gem file
%{?scl:"}
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --bindir ./%{_bindir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

# If there were programs installed:
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}


mkdir -p %{buildroot}%{gem_dir}

%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gem_dir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gem_dir}/bin
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
find %{buildroot}%{gem_instdir} --name .yardoc | xargs rm -f

%files
%{_bindir}/jammit
%{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.6.5-10
- generate spec in SC env (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.6.5-9
- new package built with tito

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.6.5-8
- edit spec for Fedora 17 (msuchy@redhat.com)

* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 0.6.5-7
- correctly set gem_dir on rhel6 (msuchy@redhat.com)

* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 0.6.5-6
- rebuild

* Thu Jun 28 2012 Miroslav Suchý 0.6.5-5
- in rhel6 there is no package rubygems-devel (msuchy@redhat.com)

* Wed Jun 27 2012 Miroslav Suchý <msuchy@redhat.com> 0.6.5-4
- macro gem_instdir expect gem_name and not gemname

* Wed Jun 27 2012 Miroslav Suchý <msuchy@redhat.com> 0.6.5-3
- gem_instdir is defined in ruby-devel
- gem_dir macro is defined in ruby-devel
- macro ruby_sitelib is not used

* Wed Jun 27 2012 Miroslav Suchý <msuchy@redhat.com> 0.6.5-2
- rebase to 0.6.5
- buildroot is not needed since el5
- defattr are not needed since rhel5
- allow to build on Fedora17

* Thu Nov 11 2010 Shannon Hughes <shughes@redhat.com> 0.5.4-1
- new gem 0.5.4 (shughes@redhat.com)

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 0.5.3-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 0.5.3-1
- Initial package
