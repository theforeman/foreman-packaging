#!/bin/sh
#
# start_mysqld_and_auto_install.sh - starts an instance of mysqld before
# auto_installing and running do_mysql's test suite. It is inspired by
# debian/test_mysql.sh from libdbi-drivers source package.



set -e

MYTEMP_DIR=`mktemp -d`
ME=`whoami`

export MYSQL_UNIX_PORT=${MYTEMP_DIR}/mysql.sock
DO_MYSQL_USER=root
DO_MYSQL_PASS=
DO_MYSQL_DBNAME=test
DO_MYSQL_DATABASE=/${DO_MYSQL_DBNAME}

mysql_install_db --no-defaults --datadir=${MYTEMP_DIR} --force --skip-name-resolve --user=${DO_MYSQL_USER}
/usr/sbin/mysqld --no-defaults --user=${DO_MYSQL_USER} --socket=${MYSQL_UNIX_PORT} --datadir=${MYTEMP_DIR} --skip-networking &
echo -n pinging mysqld.
attempts=0
while ! /usr/bin/mysqladmin --socket=${MYSQL_UNIX_PORT} ping ; do
  sleep 3
  attempts=$((attempts+1))
  if [ ${attempts} -gt 10 ] ; then
    echo "skipping test, mysql server could not be contacted after 30 seconds"
    exit 0
  fi
done
mysql --socket=${MYSQL_UNIX_PORT} --execute "CREATE DATABASE ${DO_MYSQL_DBNAME};"
mysql --socket=${MYSQL_UNIX_PORT} --execute "GRANT ALL PRIVILEGES ON ${DO_MYSQL_DBNAME}.* TO '${DO_MYSQL_USER}'@'localhost' IDENTIFIED BY '${DO_MYSQL_PASS}';"


dh_auto_install

/usr/bin/mysqladmin --socket=${MYSQL_UNIX_PORT} shutdown
rm -rf ${MYTEMP_DIR}


