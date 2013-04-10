%define rbname wirb
%define version 0.4.2
%define release 1

Summary: Wavy IRB: Colorizes irb results.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/janlelis/wirb
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(wirb) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Wavy IRB: Colorizes irb results. It originated from Wirble, but only provides
result highlighting. Just call Wirb.start and enjoy the colors in your IRB ;).
You can use it with your favorite colorizer engine. See README.rdoc for more
details.


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
%{gemdir}/gems/wirb-0.4.2/lib/wirb/version.rb
%{gemdir}/gems/wirb-0.4.2/lib/wirb/wp.rb
%{gemdir}/gems/wirb-0.4.2/lib/wirb/colorizer.rb
%{gemdir}/gems/wirb-0.4.2/lib/wirb/colorizer/wirb0_paint.rb
%{gemdir}/gems/wirb-0.4.2/lib/wirb/colorizer/wirble.rb
%{gemdir}/gems/wirb-0.4.2/lib/wirb/colorizer/wirb0.rb
%{gemdir}/gems/wirb-0.4.2/lib/wirb/colorizer/highline.rb
%{gemdir}/gems/wirb-0.4.2/lib/wirb/colorizer/paint.rb
%{gemdir}/gems/wirb-0.4.2/lib/wirb/colorizer/wirb0_highline.rb
%{gemdir}/gems/wirb-0.4.2/lib/wirb/tokenizer.rb
%{gemdir}/gems/wirb-0.4.2/lib/wirb/irb.rb
%{gemdir}/gems/wirb-0.4.2/lib/wirb.rb
%{gemdir}/gems/wirb-0.4.2/spec/spec_helper.rb
%{gemdir}/gems/wirb-0.4.2/spec/colorizer_highline_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_rails_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_enumerator_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_array_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_hash_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/colorizer_paint_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_misc_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/colorizer_wirb0_paint_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/colorizer_wirb0_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_object_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/colorizer_wirb0_highline_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_symbol_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/colorizer_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_string_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_rubyvm_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_rubygems_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_set_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_nested_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_number_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_regexp_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/colorizer_wirble_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_nil_false_true_spec.rb
%{gemdir}/gems/wirb-0.4.2/spec/tokenizer_time_spec.rb
%doc %{gemdir}/gems/wirb-0.4.2/COPYING.txt
%{gemdir}/gems/wirb-0.4.2/CHANGELOG.rdoc
%doc %{gemdir}/gems/wirb-0.4.2/README.rdoc
%{gemdir}/gems/wirb-0.4.2/data/wirb/classic_paint.yml
%{gemdir}/gems/wirb-0.4.2/data/wirb/colorless.yml
%{gemdir}/gems/wirb-0.4.2/data/wirb/classic_wirb0.yml
%{gemdir}/gems/wirb-0.4.2/Rakefile
%{gemdir}/gems/wirb-0.4.2/wirb.gemspec
%{gemdir}/gems/wirb-0.4.2/.gemtest


%doc %{gemdir}/doc/wirb-0.4.2
%{gemdir}/cache/wirb-0.4.2.gem
%{gemdir}/specifications/wirb-0.4.2.gemspec

%changelog
