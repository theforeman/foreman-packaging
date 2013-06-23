%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name yui-compressor

Summary: JavaScript and CSS minification library
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.9.6
Release: 6%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/sstephenson/ruby-yui-compressor/
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}rubygem-POpen4
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A Ruby interface to YUI Compressor for minifying JavaScript and CSS assets.

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p .%{gem_dir}

%{?scl:scl enable %{scl} "}
# Create the gem as gem install only works on a gem file
%{?scl:"}
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.9.6-6
- new package built with tito

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.9.6-5
- edit spec for Fedora 17 (msuchy@redhat.com)

* Mon Jul 02 2012 Miroslav Suchý <msuchy@redhat.com> 0.9.6-4
- rebase to 0.9.6

* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 0.9.5-3
- correctly set gem_dir on rhel6 (msuchy@redhat.com)

* Thu Jun 28 2012 Miroslav Suchý <msuchy@redhat.com> 0.9.5-2
- in rhel6 there is no package rubygems-devel (msuchy@redhat.com)

* Thu Jun 28 2012 Miroslav Suchý <msuchy@redhat.com> 0.9.5-1
- revert to 0.9.5, which does not need POpen4 (msuchy@redhat.com)

* Wed Jun 27 2012 Miroslav Suchý <msuchy@redhat.com> 0.9.6-3
- macros ruby_sitelib and geminstdir are not used
- gem_dir macro is defined in ruby-devel

* Wed Jun 27 2012 Miroslav Suchý <msuchy@redhat.com> 0.9.6-2
- require rubygem-POpen4

* Wed Jun 27 2012 Miroslav Suchý <msuchy@redhat.com> 0.9.6-1
- allow to build on Fedora17
- buildroot is not needed since el5
- defattr are not needed since rhel5
- rebase to yui-compressor 0.9.6

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 0.9.1-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 0.9.1-1
- Initial package
