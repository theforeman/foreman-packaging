%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global	gem_name	levenshtein
%global	rubyabi	1.9.1

Summary:	Calculates the Levenshtein distance between two byte strings
Name:		%{?scl_prefix}rubygem-%{gem_name}
Version:	0.2.2
Release:	2%{?dist}

Group:		Development/Languages
# LICENSE file
License:	GPLv2
URL:		http://www.erikveen.dds.nl/levenshtein/doc/index.html
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	%{?scl_prefix}ruby(abi) = %{rubyabi}
Requires:	%{?scl_prefix}ruby(rubygems) 
Requires:	%{?scl_prefix}ruby
BuildRequires:	%{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires:	%{?scl_prefix}rubygems-devel 
BuildRequires:	%{?scl_prefix}ruby-devel
BuildRequires:	%{?scl_prefix}rubygem(minitest)
Provides:	%{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Calculates the Levenshtein distance between two byte strings.

The Levenshtein distance is a metric for measuring the amount
of difference between two sequences (i.e., the so called edit
distance). The Levenshtein distance between two sequences is
given by the minimum number of operations needed to transform
one sequence into the other, where an operation is an
insertion, deletion, or substitution of a single element.

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T

TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
cd %{gem_name}-%{version}

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

%{?scl:scl enable %{scl} "}
gem specification -l --ruby %{SOURCE0}
%{?scl:"} > %{gem_name}.gemspec

%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
mkdir -p .%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %{scl} "}
gem install \
	--local \
	--install-dir .%{gem_dir} \
	-V \
	--force \
	%{gem_name}-%{version}.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir}/lib
mv \
	%{buildroot}%{gem_instdir}/lib/levenshtein \
	%{buildroot}%{gem_extdir}/lib/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} "}
ruby -Ilib test/test.rb
%{?scl:"}
popd

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*

%{gem_libdir}/
%{gem_extdir}/
%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%exclude	%{gem_instdir}/test/

%changelog
* Tue May 14 2013 Dominic Cleal <dcleal@redhat.com> 0.2.2-2
- new package built with tito

* Sat Jan  5 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-1
- Initial package
