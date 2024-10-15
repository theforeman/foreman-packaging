Name: foreman_ygg_migration
Version: 0.0.1
Summary: A helper package to ease transition from yggdrasil 0.2.z to 0.4.z
Release: 1%{?dist}
License: MIT

%if 0%{?rhel} >= 8
Supplements: yggdrasil >= 0.4.0
%endif
Conflicts:   yggdrasil  < 0.4.0

%description
A helper package to ease transition from yggdrasil 0.2.z to 0.4.z

%post
if systemctl is-enabled yggdrasild >/dev/null 2>/dev/null; then
	grep -Pq '^server'      /etc/yggdrasil/config.toml || sed -i 's/broker.*=/server =/' /etc/yggdrasil/config.toml
	grep -Pq '^path-prefix' /etc/yggdrasil/config.toml || echo 'path-prefix = "yggdrasil"' >>/etc/yggdrasil/config.toml
	grep -Pq '^data-host'   /etc/yggdrasil/config.toml || echo 'data-host = ""' >>/etc/yggdrasil/config.toml

	if grep -q FOREMAN_YGG_WORKER_WORKDIR /etc/systemd/system/yggdrasild.service.d/* 2>/dev/null; then
		mkdir -p /etc/systemd/system/com.redhat.Yggdrasil1.Worker1.foreman.service.d/
		cp -r /etc/systemd/system/yggdrasild.service.d/* /etc/systemd/system/com.redhat.Yggdrasil1.Worker1.foreman.service.d/
		systemctl daemon-reload
	fi

	systemctl disable --now yggdrasild
	systemctl enable  --now yggdrasil
fi

%files

%changelog
* Thu Oct 03 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.0.1-1
- Initial packaging
