# Generated from nokogiri-1.5.2.gem by gem2rpm -*- rpm-spec -*-
%global gemname nokogiri

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser
Name: rubygem-%{gemname}
Version: 1.5.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://nokogiri.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby >= 1.8.7
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby >= 1.8.7
BuildRequires: libxslt-devel
BuildRequires: libxml2-devel
Provides: rubygem(%{gemname}) = %{version}

%description
Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser.  Among Nokogiri's
many features is the ability to search documents via XPath or CSS3 selectors.
XML is like violence - if it doesn’t solve your problems, you are not using
enough of it.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local --install-dir .%{gemdir} \
--bindir .%{_bindir} \
-V \
--force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
  %{buildroot}%{gemdir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
  %{buildroot}%{_bindir}/

find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x
# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{geminstdir}/ext

%files
%dir %{geminstdir}
%{_bindir}/nokogiri
%{geminstdir}/bin
%{geminstdir}/lib
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/.autotest
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/.gemtest
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/Rakefile
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/nokogiri_help_responses.md
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/tasks/cross_compile.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/tasks/nokogiri.org.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/tasks/test.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/css/test_nthiness.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/css/test_parser.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/css/test_tokenizer.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/css/test_xpath_visitor.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/decorators/test_slop.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/2ch.html
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/address_book.rlx
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/address_book.xml
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/bar/bar.xsd
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/dont_hurt_em_why.xml
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/encoding.html
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/encoding.xhtml
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/exslt.xml
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/exslt.xslt
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/foo/foo.xsd
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/metacharset.html
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/noencoding.html
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/po.xml
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/po.xsd
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/shift_jis.html
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/shift_jis.xml
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/snuggles.xml
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/staff.dtd
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/staff.xml
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/staff.xslt
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/tlm.html
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/files/valid_bar.xml
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/helper.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/html/sax/test_parser.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/html/sax/test_parser_context.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/html/test_builder.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/html/test_document.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/html/test_document_encoding.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/html/test_document_fragment.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/html/test_element_description.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/html/test_named_characters.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/html/test_node.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/html/test_node_encoding.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/test_convert_xpath.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/test_css_cache.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/test_encoding_handler.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/test_memory_leak.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/test_nokogiri.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/test_reader.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/test_soap4r_sax.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/test_xslt_transforms.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/node/test_save_options.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/node/test_subclass.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/sax/test_parser.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/sax/test_parser_context.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/sax/test_push_parser.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_attr.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_attribute_decl.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_builder.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_c14n.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_cdata.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_comment.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_document.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_document_encoding.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_document_fragment.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_dtd.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_dtd_encoding.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_element_content.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_element_decl.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_entity_decl.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_entity_reference.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_namespace.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_node.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_node_attributes.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_node_encoding.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_node_inheritance.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_node_reparenting.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_node_set.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_parse_options.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_processing_instruction.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_reader_encoding.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_relax_ng.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_schema.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_syntax_error.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_text.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_unparented_node.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_xinclude.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xml/test_xpath.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xslt/test_custom_functions.rb
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/test/xslt/test_exception_handling.rb

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/CHANGELOG.ja.rdoc
%doc %{geminstdir}/README.ja.rdoc
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/C_CODING_STYLE.rdoc
%doc %{geminstdir}/CHANGELOG.rdoc

%changelog
* Tue Apr 10 2012 jason - 1.5.2-1
- Initial package
