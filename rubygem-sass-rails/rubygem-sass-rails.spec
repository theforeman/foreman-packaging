%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name sass-rails

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 5.0.4
Release: 2%{?dist}
Summary: Sass adapter for the Rails asset pipeline
Group: Development/Languages
License: MIT
URL: https://github.com/rails/sass-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/sass-rails.git && cd sass-rails
# # git checkout v5.0.4 && tar czvf sass-rails-5.0.4-tests.tgz ./test
Source1: sass-rails-%{version}-tests.tgz
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(sass) >= 3.1
Requires: %{?scl_prefix}rubygem(sass) < 4
Requires: %{?scl_prefix_ror}rubygem(railties) >= 4
Requires: %{?scl_prefix_ror}rubygem(railties) < 5
Requires: %{?scl_prefix_ror}rubygem(tilt) >= 1.1
Requires: %{?scl_prefix_ror}rubygem(tilt) < 3
Requires: %{?scl_prefix}rubygem(sprockets) >= 2.8
Requires: %{?scl_prefix}rubygem(sprockets) < 4
Requires: %{?scl_prefix}rubygem(sprockets-rails) >= 2
Requires: %{?scl_prefix}rubygem(sprockets-rails) < 4
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygem(bundler)
BuildRequires: %{?scl_prefix_ror}rubygem(sqlite3)
BuildRequires: %{?scl_prefix_ror}rubygem(tilt)
BuildRequires: %{?scl_prefix_ror}rubygem(rails)
BuildRequires: %{?scl_prefix}rubygem(sass)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Sass adapter for the Rails asset pipeline.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar xf %{SOURCE1}

# Copy in .gemspec and use the sass-rails sources
cp %{buildroot}%{gem_spec} sass-rails.gemspec
echo 'gem "sass-rails", :path => "."' >> Gemfile

%{?scl:scl enable %{scl} - << \EOF}
ruby -I.:test -e 'Dir.glob "test/**/*_test.rb", &method(:require)'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Sun Jan 10 2016 Daniel Lobato <elobatocs@gmail.com> 5.0.4-2
- Update to tfm SCL

* Wed Sep 16 2015 Vít Ondruch <vondruch@redhat.com> - 5.0.4-1
- Update to sass-rails 5.0.4.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Vít Ondruch <vondruch@redhat.com> - 5.0.3-1
- Update to sass-rails 5.0.3.

* Mon Feb 16 2015 Josef Stribny <jstribny@redhat.com> - 5.0.1-1
- Update to 5.0.1

* Tue Jul 01 2014 Vít Ondruch <vondruch@redhat.com> - 4.0.3-1
- Update to sass-rails 4.0.3.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-1
- Update to sass-rails 4.0.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.6-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to sass-rails 3.2.6.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.5-1
- Initial package
