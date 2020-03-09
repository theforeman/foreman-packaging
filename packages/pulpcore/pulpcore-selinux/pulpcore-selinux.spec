%define selinux_variants mls strict targeted
%define selinux_modules pulpcore_port pulpcore
%define debug_package %{nil}

Name:           pulpcore-selinux
Version:        1.0.0
Release:        2%{?dist}
Summary:        SELinux policy for Pulp 3

License:        GPL2+
URL:            https://pulpproject.org
Source0:        https://codeload.github.com/pulp/%{name}/tar.gz/%{version}#/%{name}-%{version}.tar.gz

BuildRequires:  checkpolicy
BuildRequires:  selinux-policy-devel
Requires:       selinux-policy >= %{_selinux_policy_version}
Requires:       python3-pulpcore
Requires(post): policycoreutils, python3-pulpcore
Requires(postun): policycoreutils

%description
The SELinux policy for Pulp 3.Y releases.

%prep
%autosetup


%build
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  for selinuxmodule in %{selinux_modules}
  do
    mv ${selinuxmodule}.pp ${selinuxmodule}.pp.${selinuxvariant}
  done
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done


%install
for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  for selinuxmodule in %{selinux_modules}
  do
    install -p -m 644 ${selinuxmodule}.pp.${selinuxvariant} \
      %{buildroot}%{_datadir}/selinux/${selinuxvariant}/${selinuxmodule}.pp
  done
done

%post
for selinuxvariant in %{selinux_variants}
do
  for selinuxmodule in %{selinux_modules}
  do
    /usr/sbin/semodule -s ${selinuxvariant} -i \
      %{_datadir}/selinux/${selinuxvariant}/${selinuxmodule}.pp &> /dev/null || :
  done
done
/sbin/fixfiles -R python3-pulpcore restore || :

%postun
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do
    for selinuxmodule in %{selinux_modules}
    do
      /usr/sbin/semodule -s ${selinuxvariant} -r ${selinuxmodule} &> /dev/null || :
    done
  done
  /sbin/fixfiles -R python3-pulpcore restore || :
fi

%files
%defattr(-,root,root,0755)
%{_datadir}/selinux/*/pulpcore.pp
%{_datadir}/selinux/*/pulpcore_port.pp


%changelog
* Mon Mar 09 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.0-2
- Bump to build on el8 & define the debug package as null to prevent errors

* Wed Jan 15 2020 Evgeni Golov - 1.0.0-1
- Initial package
