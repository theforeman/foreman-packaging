# Generated from awesome_print-1.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name awesome_print
%global rubyabi 1.9.1

Summary: Pretty print Ruby objects with proper indentation and colors
Name: rubygem-%{gem_name}
Version: 1.0.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/michaeldv/awesome_print
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Great Ruby dubugging companion: pretty print Ruby objects to visualize their
structure. Supports custom object formatting via plugins


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
/usr/share/gems/gems/awesome_print-1.0.2/.gitignore
/usr/share/gems/gems/awesome_print-1.0.2/CHANGELOG
/usr/share/gems/gems/awesome_print-1.0.2/Gemfile
/usr/share/gems/gems/awesome_print-1.0.2/Gemfile.lock
/usr/share/gems/gems/awesome_print-1.0.2/LICENSE
/usr/share/gems/gems/awesome_print-1.0.2/README.md
/usr/share/gems/gems/awesome_print-1.0.2/Rakefile
/usr/share/gems/gems/awesome_print-1.0.2/spec/colors_spec.rb
/usr/share/gems/gems/awesome_print-1.0.2/spec/formats_spec.rb
/usr/share/gems/gems/awesome_print-1.0.2/spec/methods_spec.rb
/usr/share/gems/gems/awesome_print-1.0.2/spec/objects_spec.rb
/usr/share/gems/gems/awesome_print-1.0.2/spec/spec_helper.rb


%files doc
%doc %{gem_docdir}

%changelog
* Thu Jun 14 2012 jason - 1.0.2-1
- Initial package
