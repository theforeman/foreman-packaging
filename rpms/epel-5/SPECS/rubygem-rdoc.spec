%define rbname rdoc
%define version 3.12
%define release 2

Summary: RDoc produces HTML and command-line documentation for Ruby projects
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://docs.seattlerb.org/rdoc
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10

Requires: rubygem-json => 1.4
Requires: rubygem-json < 2
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
Provides: rubygem(rdoc) = %{version}
%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
RDoc produces HTML and command-line documentation for Ruby projects.  RDoc
includes the +rdoc+ and +ri+ tools for generating and displaying online
documentation.
See RDoc for a description of RDoc's markup and basic use.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0} --no-rdoc --no-ri
mkdir -p %{buildroot}/%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/rdoc-3.12/.autotest
%{gemdir}/gems/rdoc-3.12/.document
%doc %{gemdir}/gems/rdoc-3.12/DEVELOPERS.rdoc
%doc %{gemdir}/gems/rdoc-3.12/History.rdoc
%doc %{gemdir}/gems/rdoc-3.12/LEGAL.rdoc
%doc %{gemdir}/gems/rdoc-3.12/LICENSE.rdoc
%doc %{gemdir}/gems/rdoc-3.12/Manifest.txt
%doc %{gemdir}/gems/rdoc-3.12/README.rdoc
%doc %{gemdir}/gems/rdoc-3.12/RI.rdoc
%doc %{gemdir}/gems/rdoc-3.12/Rakefile
%doc %{gemdir}/gems/rdoc-3.12/TODO.rdoc
%{gemdir}/gems/rdoc-3.12/bin/rdoc
%{gemdir}/gems/rdoc-3.12/bin/ri
%{gemdir}/gems/rdoc-3.12/lib/gauntlet_rdoc.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/alias.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/anon_class.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/any_method.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/attr.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/class_module.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/code_object.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/code_objects.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/comment.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/constant.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/context.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/context/section.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/cross_reference.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/encoding.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/erbio.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/darkfish.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/json_index.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/markup.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/ri.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/.document
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/_footer.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/_head.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/_sidebar_VCS_info.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/_sidebar_classes.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/_sidebar_in_files.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/_sidebar_includes.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/_sidebar_methods.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/_sidebar_navigation.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/_sidebar_pages.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/_sidebar_parent.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/_sidebar_search.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/_sidebar_sections.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/class.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/add.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/brick.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/brick_link.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/bug.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/bullet_black.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/bullet_toggle_minus.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/bullet_toggle_plus.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/date.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/delete.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/find.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/loadingAnimation.gif
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/macFFBgHack.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/package.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/page_green.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/page_white_text.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/page_white_width.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/plugin.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/ruby.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/tag_blue.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/tag_green.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/transparent.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/wrench.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/wrench_orange.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/images/zoom.png
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/index.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/js/darkfish.js
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/js/jquery.js
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/js/search.js
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/page.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/rdoc.css
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/darkfish/table_of_contents.rhtml
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/json_index/js/navigation.js
%{gemdir}/gems/rdoc-3.12/lib/rdoc/generator/template/json_index/js/searcher.js
%{gemdir}/gems/rdoc-3.12/lib/rdoc/ghost_method.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/include.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/known_classes.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/attr_changer.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/attr_span.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/attribute.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/attribute_manager.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/blank_line.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/document.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/formatter.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/formatter_test_case.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/heading.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/include.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/indented_paragraph.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/inline.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/list.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/list_item.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/paragraph.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/parser.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/pre_process.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/raw.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/rule.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/special.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/text_formatter_test_case.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/to_ansi.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/to_bs.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/to_html.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/to_html_crossref.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/to_html_snippet.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/to_label.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/to_rdoc.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/to_table_of_contents.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/to_test.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/to_tt_only.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/markup/verbatim.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/meta_method.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/method_attr.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/normal_class.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/normal_module.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/options.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/parser.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/parser/c.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/parser/rd.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/parser/ruby.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/parser/ruby_tools.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/parser/simple.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/parser/text.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/rd.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/rd/block_parser.ry
%{gemdir}/gems/rdoc-3.12/lib/rdoc/rd/inline.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/rd/inline_parser.ry
%{gemdir}/gems/rdoc-3.12/lib/rdoc/rdoc.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/require.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/ri.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/ri/driver.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/ri/formatter.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/ri/paths.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/ri/store.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/ruby_lex.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/ruby_token.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/rubygems_hook.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/single_class.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/stats.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/stats/normal.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/stats/quiet.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/stats/verbose.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/task.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/test_case.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/text.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/token_stream.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/tom_doc.rb
%{gemdir}/gems/rdoc-3.12/lib/rdoc/top_level.rb
%{gemdir}/gems/rdoc-3.12/test/README
%{gemdir}/gems/rdoc-3.12/test/binary.dat
%{gemdir}/gems/rdoc-3.12/test/hidden.zip.txt
%{gemdir}/gems/rdoc-3.12/test/test.ja.large.rdoc
%{gemdir}/gems/rdoc-3.12/test/test.ja.rdoc
%{gemdir}/gems/rdoc-3.12/test/test.ja.txt
%{gemdir}/gems/rdoc-3.12/test/test.txt
%{gemdir}/gems/rdoc-3.12/test/test_attribute_manager.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_alias.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_any_method.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_attr.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_class_module.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_code_object.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_comment.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_constant.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_context.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_context_section.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_cross_reference.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_encoding.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_generator_darkfish.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_generator_json_index.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_generator_markup.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_generator_ri.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_include.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_attribute_manager.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_document.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_formatter.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_heading.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_include.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_indented_paragraph.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_paragraph.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_parser.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_pre_process.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_raw.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_to_ansi.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_to_bs.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_to_html.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_to_html_crossref.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_to_html_snippet.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_to_label.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_to_rdoc.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_to_table_of_contents.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_to_tt_only.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_markup_verbatim.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_method_attr.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_normal_class.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_normal_module.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_options.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_parser.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_parser_c.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_parser_rd.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_parser_ruby.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_parser_simple.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_rd.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_rd_block_parser.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_rd_inline.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_rd_inline_parser.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_rdoc.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_require.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_ri_driver.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_ri_paths.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_ri_store.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_ruby_lex.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_rubygems_hook.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_single_class.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_stats.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_task.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_text.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_token_stream.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_tom_doc.rb
%{gemdir}/gems/rdoc-3.12/test/test_rdoc_top_level.rb
%{gemdir}/gems/rdoc-3.12/test/xref_data.rb
%{gemdir}/gems/rdoc-3.12/test/xref_test_case.rb
%{gemdir}/gems/rdoc-3.12/.gemtest
%{gemdir}/bin/rdoc
%{gemdir}/bin/ri
%{gemdir}/cache/rdoc-3.12.gem
%{gemdir}/specifications/rdoc-3.12.gemspec

%changelog
* Tue May 08 2012 jmontleo@redhat.com - 3.12-2
- Cleaned up spec file

