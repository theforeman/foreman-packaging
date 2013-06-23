%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name daemons

Summary: A toolkit to create and control daemons in different ways
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.4
Release: 7%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://daemons.rubyforge.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel

%description
Daemons provides an easy way to wrap existing ruby scripts (for example a
self-written server)  to be run as a daemon and to be controlled by simple
start/stop/restart commands.  You can also call blocks as daemons and control
them from the parent or just daemonize the current process.  Besides this
basic functionality, daemons offers many advanced features like exception
backtracing and logging (in case your ruby script crashes) and monitoring and
automatic restarting of your processes if they crash.

%prep
%setup -q -c -T -n  %{gem_name}-%{version}

%build
mkdir -p .%{gem_dir}

%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{SOURCE0}
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README
%doc %{gem_instdir}/Releases
%doc %{gem_instdir}/TODO
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.4-7
- BR rubygems-devel (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.4-6
- do not regenerate gemspec (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.4-5
- wrap up generating gemspec in SC environment (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.4-4
- new package built with tito

* Mon Jul 16 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.4-3
- edit spec for fedora (msuchy@redhat.com)

* Mon Jul 11 2011 Mike McCune <mmccune@redhat.com> 1.1.4-2
- fixed new-lines in daemon.spec (dmitri@redhat.com)

* Wed Jul 06 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.1.4-1
- new package built with tito

* Wed Jul 06 2011  <wb@killing-time.appliedlogic.ca> - 1.1.4-1
- Initial package
