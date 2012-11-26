# Generated from audited-3.0.0.rc1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name audited
%global rubyabi 1.9.1

Summary: Log all changes to your models
Name: rubygem-%{gem_name}
Version: 3.0.0.rc1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/collectiveidea/audited
Source0: %{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) > 1.3.1
Requires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel > 1.3.1
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Log all changes to your models


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/





%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems/gems/audited-3.0.0.rc1/spec/
/usr/share/gems/gems/audited-3.0.0.rc1/test/
/usr/share/gems/gems/audited-3.0.0.rc1/.gitignore
/usr/share/gems/gems/audited-3.0.0.rc1/.travis.yml
/usr/share/gems/gems/audited-3.0.0.rc1/.yardopts
/usr/share/gems/gems/audited-3.0.0.rc1/Appraisals
/usr/share/gems/gems/audited-3.0.0.rc1/CHANGELOG
/usr/share/gems/gems/audited-3.0.0.rc1/Gemfile
/usr/share/gems/gems/audited-3.0.0.rc1/LICENSE
/usr/share/gems/gems/audited-3.0.0.rc1/README.md
/usr/share/gems/gems/audited-3.0.0.rc1/Rakefile
/usr/share/gems/gems/audited-3.0.0.rc1/audited-activerecord.gemspec
/usr/share/gems/gems/audited-3.0.0.rc1/audited-mongo_mapper.gemspec
/usr/share/gems/gems/audited-3.0.0.rc1/audited.gemspec
/usr/share/gems/gems/audited-3.0.0.rc1/gemfiles/rails30.gemfile
/usr/share/gems/gems/audited-3.0.0.rc1/gemfiles/rails31.gemfile
/usr/share/gems/gems/audited-3.0.0.rc1/gemfiles/rails32.gemfile

%files doc
%doc %{gem_docdir}

%changelog
* Thu Jun 21 2012 jason - 3.0.0.rc1-1
- Initial package
