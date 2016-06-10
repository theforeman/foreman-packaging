SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

RAILS_ENV=production
FOREMAN_HOME=/usr/share/foreman

# Send out notifications about expired hosts
45 7 * * *      foreman    /usr/sbin/foreman-rake expired_hosts:deliver_notifications >>/var/log/foreman/expired_hosts.log 2>&1
