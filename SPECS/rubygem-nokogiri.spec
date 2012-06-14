%define rbname nokogiri
%define version 1.5.2
%define release 1

Summary: Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://nokogiri.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
Provides: rubygem(nokogiri) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser.  Among Nokogiri's
many features is the ability to search documents via XPath or CSS3 selectors.
XML is like violence - if it doesn’t solve your problems, you are not using
enough of it.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/nokogiri
%{gemdir}/gems/nokogiri-1.5.2/.autotest
%{gemdir}/gems/nokogiri-1.5.2/.gemtest
%doc %{gemdir}/gems/nokogiri-1.5.2/CHANGELOG.ja.rdoc
%doc %{gemdir}/gems/nokogiri-1.5.2/CHANGELOG.rdoc
%doc %{gemdir}/gems/nokogiri-1.5.2/Manifest.txt
%doc %{gemdir}/gems/nokogiri-1.5.2/README.ja.rdoc
%doc %{gemdir}/gems/nokogiri-1.5.2/README.rdoc
%{gemdir}/gems/nokogiri-1.5.2/Rakefile
%{gemdir}/gems/nokogiri-1.5.2/bin/nokogiri
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/depend
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/extconf.rb
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/html_document.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/html_document.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/html_element_description.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/html_element_description.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/html_entity_lookup.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/html_entity_lookup.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/html_sax_parser_context.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/html_sax_parser_context.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/html_sax_push_parser.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/html_sax_push_parser.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/nokogiri.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/nokogiri.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_attr.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_attr.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_attribute_decl.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_attribute_decl.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_cdata.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_cdata.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_comment.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_comment.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_document.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_document.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_document_fragment.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_document_fragment.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_dtd.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_dtd.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_element_content.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_element_content.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_element_decl.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_element_decl.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_encoding_handler.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_encoding_handler.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_entity_decl.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_entity_decl.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_entity_reference.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_entity_reference.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_io.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_io.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_libxml2_hacks.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_libxml2_hacks.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_namespace.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_namespace.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_node.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_node.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_node_set.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_node_set.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_processing_instruction.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_processing_instruction.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_reader.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_reader.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_relax_ng.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_relax_ng.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_sax_parser.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_sax_parser.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_sax_parser_context.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_sax_parser_context.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_sax_push_parser.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_sax_push_parser.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_schema.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_schema.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_syntax_error.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_syntax_error.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_text.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_text.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_xpath_context.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xml_xpath_context.h
%doc %{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xslt_stylesheet.c
%{gemdir}/gems/nokogiri-1.5.2/ext/nokogiri/xslt_stylesheet.h
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/css.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/css/node.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/css/parser.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/css/parser.y
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/css/parser_extras.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/css/syntax_error.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/css/tokenizer.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/css/tokenizer.rex
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/css/xpath_visitor.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/decorators/slop.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/html.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/html/builder.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/html/document.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/html/document_fragment.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/html/element_description.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/html/element_description_defaults.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/html/entity_lookup.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/html/sax/parser.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/html/sax/parser_context.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/html/sax/push_parser.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/syntax_error.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/version.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/attr.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/attribute_decl.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/builder.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/cdata.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/character_data.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/document.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/document_fragment.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/dtd.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/element_content.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/element_decl.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/entity_decl.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/namespace.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/node.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/node/save_options.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/node_set.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/notation.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/parse_options.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/pp.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/pp/character_data.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/pp/node.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/processing_instruction.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/reader.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/relax_ng.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/sax.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/sax/document.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/sax/parser.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/sax/parser_context.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/sax/push_parser.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/schema.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/syntax_error.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/text.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/xpath.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/xpath/syntax_error.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xml/xpath_context.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xslt.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/nokogiri/xslt/stylesheet.rb
%{gemdir}/gems/nokogiri-1.5.2/lib/xsd/xmlparser/nokogiri.rb
%{gemdir}/gems/nokogiri-1.5.2/nokogiri_help_responses.md
%{gemdir}/gems/nokogiri-1.5.2/tasks/cross_compile.rb
%{gemdir}/gems/nokogiri-1.5.2/tasks/nokogiri.org.rb
%{gemdir}/gems/nokogiri-1.5.2/tasks/test.rb
%{gemdir}/gems/nokogiri-1.5.2/test/css/test_nthiness.rb
%{gemdir}/gems/nokogiri-1.5.2/test/css/test_parser.rb
%{gemdir}/gems/nokogiri-1.5.2/test/css/test_tokenizer.rb
%{gemdir}/gems/nokogiri-1.5.2/test/css/test_xpath_visitor.rb
%{gemdir}/gems/nokogiri-1.5.2/test/decorators/test_slop.rb
%{gemdir}/gems/nokogiri-1.5.2/test/files/2ch.html
%{gemdir}/gems/nokogiri-1.5.2/test/files/address_book.rlx
%{gemdir}/gems/nokogiri-1.5.2/test/files/address_book.xml
%{gemdir}/gems/nokogiri-1.5.2/test/files/bar/bar.xsd
%{gemdir}/gems/nokogiri-1.5.2/test/files/dont_hurt_em_why.xml
%{gemdir}/gems/nokogiri-1.5.2/test/files/encoding.html
%{gemdir}/gems/nokogiri-1.5.2/test/files/encoding.xhtml
%{gemdir}/gems/nokogiri-1.5.2/test/files/exslt.xml
%{gemdir}/gems/nokogiri-1.5.2/test/files/exslt.xslt
%{gemdir}/gems/nokogiri-1.5.2/test/files/foo/foo.xsd
%{gemdir}/gems/nokogiri-1.5.2/test/files/metacharset.html
%{gemdir}/gems/nokogiri-1.5.2/test/files/noencoding.html
%{gemdir}/gems/nokogiri-1.5.2/test/files/po.xml
%{gemdir}/gems/nokogiri-1.5.2/test/files/po.xsd
%{gemdir}/gems/nokogiri-1.5.2/test/files/shift_jis.html
%{gemdir}/gems/nokogiri-1.5.2/test/files/shift_jis.xml
%{gemdir}/gems/nokogiri-1.5.2/test/files/snuggles.xml
%{gemdir}/gems/nokogiri-1.5.2/test/files/staff.dtd
%{gemdir}/gems/nokogiri-1.5.2/test/files/staff.xml
%{gemdir}/gems/nokogiri-1.5.2/test/files/staff.xslt
%{gemdir}/gems/nokogiri-1.5.2/test/files/tlm.html
%{gemdir}/gems/nokogiri-1.5.2/test/files/valid_bar.xml
%{gemdir}/gems/nokogiri-1.5.2/test/helper.rb
%{gemdir}/gems/nokogiri-1.5.2/test/html/sax/test_parser.rb
%{gemdir}/gems/nokogiri-1.5.2/test/html/sax/test_parser_context.rb
%{gemdir}/gems/nokogiri-1.5.2/test/html/test_builder.rb
%{gemdir}/gems/nokogiri-1.5.2/test/html/test_document.rb
%{gemdir}/gems/nokogiri-1.5.2/test/html/test_document_encoding.rb
%{gemdir}/gems/nokogiri-1.5.2/test/html/test_document_fragment.rb
%{gemdir}/gems/nokogiri-1.5.2/test/html/test_element_description.rb
%{gemdir}/gems/nokogiri-1.5.2/test/html/test_named_characters.rb
%{gemdir}/gems/nokogiri-1.5.2/test/html/test_node.rb
%{gemdir}/gems/nokogiri-1.5.2/test/html/test_node_encoding.rb
%{gemdir}/gems/nokogiri-1.5.2/test/test_convert_xpath.rb
%{gemdir}/gems/nokogiri-1.5.2/test/test_css_cache.rb
%{gemdir}/gems/nokogiri-1.5.2/test/test_encoding_handler.rb
%{gemdir}/gems/nokogiri-1.5.2/test/test_memory_leak.rb
%{gemdir}/gems/nokogiri-1.5.2/test/test_nokogiri.rb
%{gemdir}/gems/nokogiri-1.5.2/test/test_reader.rb
%{gemdir}/gems/nokogiri-1.5.2/test/test_soap4r_sax.rb
%{gemdir}/gems/nokogiri-1.5.2/test/test_xslt_transforms.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/node/test_save_options.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/node/test_subclass.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/sax/test_parser.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/sax/test_parser_context.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/sax/test_push_parser.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_attr.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_attribute_decl.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_builder.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_cdata.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_comment.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_document.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_document_encoding.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_document_fragment.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_dtd.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_dtd_encoding.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_element_content.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_element_decl.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_entity_decl.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_entity_reference.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_namespace.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_node.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_node_attributes.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_node_encoding.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_node_reparenting.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_node_set.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_node_inheritance.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_parse_options.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_processing_instruction.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_reader_encoding.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_relax_ng.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_schema.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_syntax_error.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_text.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_unparented_node.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_xpath.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xslt/test_custom_functions.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xslt/test_exception_handling.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_c14n.rb
%{gemdir}/gems/nokogiri-1.5.2/test/xml/test_xinclude.rb
%doc %{gemdir}/gems/nokogiri-1.5.2/C_CODING_STYLE.rdoc
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/Makefile
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/html_document.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/html_element_description.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/html_entity_lookup.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/html_sax_parser_context.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/html_sax_push_parser.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/mkmf.log
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/nokogiri.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/nokogiri.so
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_attr.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_attribute_decl.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_cdata.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_comment.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_document.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_document_fragment.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_dtd.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_element_content.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_element_decl.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_encoding_handler.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_entity_decl.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_entity_reference.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_io.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_libxml2_hacks.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_namespace.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_node.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_node_set.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_processing_instruction.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_reader.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_relax_ng.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_sax_parser.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_sax_parser_context.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_sax_push_parser.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_schema.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_syntax_error.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_text.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xml_xpath_context.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/ext/nokogiri/xslt_stylesheet.o
/usr/lib/ruby/gems/1.8/gems/nokogiri-1.5.2/lib/nokogiri/nokogiri.so


%doc %{gemdir}/doc/nokogiri-1.5.2
%{gemdir}/cache/nokogiri-1.5.2.gem
%{gemdir}/specifications/nokogiri-1.5.2.gemspec

%changelog
