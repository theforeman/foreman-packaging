%define rbname rack-mount
%define version 0.6.14
%define release 1

Summary: Stackable dynamic tree based Rack router
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/josh/rack-mount
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-rack >= 1.0.0
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(rack-mount) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
A stackable dynamic tree based Rack router.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/analysis/frequency.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/analysis/histogram.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/analysis/splitting.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/code_generation.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/generatable_regexp.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/multimap.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/prefix.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/regexp_with_named_groups.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/route.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/route_set.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/strexp.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/strexp/parser.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/strexp/parser.y
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/strexp/tokenizer.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/strexp/tokenizer.rex
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/utils.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/multimap/multimap.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/multimap/multiset.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/multimap/nested_multimap.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin/alternation.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin/anchor.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin/atom.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin/character.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin/character_class.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin/collection.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin/expression.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin/group.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin/options.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin/parser.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin/tokenizer.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/vendor/regin/regin/version.rb
%{gemdir}/gems/rack-mount-0.6.14/lib/rack/mount/version.rb
%{gemdir}/gems/rack-mount-0.6.14/LICENSE
%{gemdir}/gems/rack-mount-0.6.14/README.rdoc


%doc %{gemdir}/doc/rack-mount-0.6.14
/usr/lib/ruby/gems/1.8/cache/rack-mount-0.6.14.gem
/usr/lib/ruby/gems/1.8/specifications/rack-mount-0.6.14.gemspec

%changelog
