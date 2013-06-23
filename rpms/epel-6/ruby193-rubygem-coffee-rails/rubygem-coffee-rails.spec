%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from coffee-rails-3.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name coffee-rails
%global rubyabi 1.9.1

Summary: Coffee Script adapter for the Rails asset pipeline
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.2.2
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/rails/coffee-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# failing test: https://github.com/rails/coffee-rails/issues/27
Patch0: %{gem_name}-test-fix.patch
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(coffee-script) >= 2.2.0
Requires: %{?scl_prefix}rubygem(railties) => 3.2.0
Requires: %{?scl_prefix}rubygem(railties) < 3.3
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(coffee-script) >= 2.2.0
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(railties) => 3.2.0
BuildRequires: %{?scl_prefix}rubygem(railties) < 3.3
BuildRequires: %{?scl_prefix}rubygem(sprockets)
BuildRequires: %{?scl_prefix}rubygem(therubyracer)
BuildRequires: %{?scl_prefix}rubygem(tzinfo)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Coffee Script adapter for the Rails asset pipeline.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
ruby -I.:test:lib -e 'Dir.glob("test/**/*_test.rb").each {|t| require t}'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Fri Mar 01 2013 Miroslav Suchý <msuchy@redhat.com> 3.2.2-3
- new package built with tito

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.2-2
- Imported from Fedora again.
- Specfile cleanup

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.2-1
- Initial package
