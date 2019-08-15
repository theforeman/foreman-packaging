#!/bin/bash
# :vim:sw=2:ts=2:et:
#
# This file is installed in /usr/share/foreman/script/foreman-debug.d where
# it is picked by foreman-debug reporting tool. This file contains rules for
# both Katello server and Katello proxy (Satellite 6 / Capsule nodes).
#

# error out if called directly
if [ $BASH_SOURCE == $0 ]
then
  echo "This script should not be executed directly, use foreman-debug instead."
  exit 1
fi

TEMP_DIR=$(mktemp -d) # no trap - foreman-debug cleans automatically

# foreman-debug will truncate any file beyond fixed size limit,
# for larger files we need to copy the entire file.
copy_files() {
  for FILE in $*; do
    printv "Copying entire file: $FILE"
    if [ \( -f "$FILE" -o -h "$FILE" \) -a \( -r "$FILE" -a -s "$FILE" \) ]; then
      printv " - $FILE"
      SUBDIR=$(dirname $FILE)
      [ ! -d "$DIR$SUBDIR" ] && mkdir -p "$DIR$SUBDIR"
      cp "$FILE" "$DIR$FILE"
    fi
  done
}

# Installer
add_files /var/log/foreman-installer/*
add_files /etc/foreman-installer/*
add_cmd "find /root/ssl-build -ls | sort -k 11" "katello_ssl_build_dir"
add_cmd "find /etc/pki -ls | sort -k 11" "katello_pki_dir"

# Katello
add_files /etc/pulp/server/plugins.d/*
add_files /etc/foreman/plugins/katello.yaml
add_files /var/log/httpd/katello-reverse-proxy_access_ssl.log*
add_files /var/log/httpd/katello-reverse-proxy_error_ssl.log*

# Candlepin
add_files /var/log/candlepin/audit*.log*
add_files /var/log/candlepin/candlepin*.log*
add_files /var/log/candlepin/cpdb*.log*
add_files /var/log/candlepin/cpinit*.log*
add_files /var/log/candlepin/error*.log*
add_files /var/log/tomcat*/catalina*.log*
add_files /var/log/tomcat*/host-manager*.log*
add_files /var/log/tomcat*/localhost*.log*
add_files /var/log/tomcat*/manager*.log*
add_files /etc/candlepin/candlepin.conf
add_files /etc/tomcat*/server.xml

# RHSM
add_files /var/log/rhsm/*

# Pulp
add_files /etc/pulp/*.conf
add_files /etc/httpd/conf.d/pulp.conf
add_files /etc/pulp/server/plugins.conf.d/*
add_files /var/log/httpd/pulp-http{s,}_access_ssl.log*
add_files /var/log/httpd/pulp-http{s,}_error_ssl.log*
add_files /etc/default/pulp*

# MongoDB (*)
if [ $NOGENERIC -eq 0 ]; then
  add_files /var/log/mongodb/*
  add_files /var/lib/mongodb/mongodb.log*
fi

# Qpidd (*)
if [ $NOGENERIC -eq 0 ]; then
  add_files /etc/qpid/*
  add_files /etc/qpidd.conf
  add_files /etc/qpid-dispatch/qdrouterd.conf
  add_files /var/log/qdrouterd/qdrouterd.log
fi

if [ -f /etc/pki/katello/qpid_client_striped.crt ]; then
  add_cmd "qpid-stat -q --ssl-certificate=/etc/pki/katello/qpid_client_striped.crt -b amqps://localhost:5671" "qpid-stat-q"
  add_cmd "qpid-stat -u --ssl-certificate=/etc/pki/katello/qpid_client_striped.crt -b amqps://localhost:5671" "qpid-stat-u"
  add_cmd "qpid-stat -c --ssl-certificate=/etc/pki/katello/qpid_client_striped.crt -b amqps://localhost:5671" "qpid-stat-c"
else
  add_cmd "qpid-stat -q --ssl-certificate=/etc/pki/pulp/qpid/client.crt -b amqps://localhost:5671" "qpid-stat-q"
  add_cmd "qpid-stat -u --ssl-certificate=/etc/pki/pulp/qpid/client.crt -b amqps://localhost:5671" "qpid-stat-u"
  add_cmd "qpid-stat -c --ssl-certificate=/etc/pki/pulp/qpid/client.crt -b amqps://localhost:5671" "qpid-stat-c"
fi
add_cmd "ps -awfux" "ps-awfux"
add_cmd "ps -efLm" "ps-elfm"

# FreeIPA (*)
if [ $NOGENERIC -eq 0 ]; then
  add_files /var/log/ipa*-install.log
  add_files /var/log/ipaupgrade.log
  add_files /var/log/dirsrv/slapd-*/logs/access
  add_files /var/log/dirsrv/slapd-*/logs/errors
  add_files /etc/dirsrv/slapd-*/dse.ldif
  add_files /etc/dirsrv/slapd-*/schema/99user.ldif
fi

# Squid (*)
if [ $NOGENERIC -eq 0 ]; then
  add_files /etc/squid/squid.conf
  add_files /var/log/squid/access*.log*
  add_files /var/log/squid/cache*.log*
  add_files /var/log/squid/store*.log*
  add_files /var/log/squid/squid*.out*
fi

# Disk Space Checks
add_cmd "du -sh /var/lib/pgsql" "postgres_disk_space"
add_cmd "du -sh /var/lib/mongodb" "mongodb_disk_space"
add_cmd "df -h" "disk_space_output"
add_cmd "du -sh /var/lib/qpid" "qpid_jrnl_disk_space"
add_cmd "du -sh /var/lib/candlepin/hornetq" "hornetq_disk_space"

# Proxy ENV Vars
add_cmd "echo $http_proxy" "http_proxy_var"
add_cmd "echo $https_proxy" "https_proxy_var"
add_files /etc/profile.d/*


add_cmd "mongo pulp_database --eval \"db.reserved_resources.find().pretty().shellPrint()\"" "mongo-reserved_resources"
add_cmd "mongo pulp_database --eval \"DBQuery.shellBatchSize = ${FOREMAN_DEBUG_MONGOTASKS:-200};; db.task_status.find().sort({finish_time: -1}).pretty().shellPrint()\"" "mongo-task_status"

echo "db.task_status.find({state:{\$ne: \"finished\"}}).pretty().shellPrint()" > $TEMP_DIR/pulp_running_tasks.js
add_cmd "mongo pulp_database $TEMP_DIR/pulp_running_tasks.js" "pulp-running_tasks"

add_cmd "echo 'select id, name, checksum_type, updated_at from katello_root_repositories' | su postgres -c 'psql foreman'" katello_repositories
add_cmd "echo \"SELECT table_name, pg_size_pretty(total_bytes) AS total, pg_size_pretty(index_bytes) AS INDEX , pg_size_pretty(toast_bytes) AS toast, pg_size_pretty(table_bytes) AS TABLE FROM ( SELECT *, total_bytes-index_bytes-COALESCE(toast_bytes,0) AS table_bytes FROM (SELECT c.oid,nspname AS table_schema, relname AS TABLE_NAME, c.reltuples AS row_estimate, pg_total_relation_size(c.oid) AS total_bytes, pg_indexes_size(c.oid) AS index_bytes, pg_total_relation_size(reltoastrelid) AS toast_bytes FROM pg_class c LEFT JOIN pg_namespace n ON n.oid = c.relnamespace WHERE relkind = 'r') a) a order by total_bytes DESC\" | su postgres -c 'psql foreman'" "db_table_size"

add_cmd "hammer ping" "hammer-ping"
add_cmd "foreman-maintain service status" "foreman-maintain_service_status"

# Legend:
# * - already collected by sosreport tool (skip when -g option was provided)
