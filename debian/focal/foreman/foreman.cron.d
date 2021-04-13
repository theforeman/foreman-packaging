SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

RAILS_ENV=production
FOREMAN_HOME=/usr/share/foreman

# Clean up the session entries in the database
15 23 * * *     foreman    cd ${FOREMAN_HOME} && /usr/sbin/foreman-rake db:sessions:clear | gawk '{ print strftime("[%Y-%m-%d %H:%M:%S]"), $0 }' >>/var/log/foreman/cron.log 2>&1

# Send out recurring notifications
0 7 * * *       foreman    cd ${FOREMAN_HOME} && /usr/sbin/foreman-rake reports:daily | gawk '{ print strftime("[%Y-%m-%d %H:%M:%S]"), $0 }' >>/var/log/foreman/cron.log 2>&1
0 5 * * 0       foreman    cd ${FOREMAN_HOME} && /usr/sbin/foreman-rake reports:weekly | gawk '{ print strftime("[%Y-%m-%d %H:%M:%S]"), $0 }' >>/var/log/foreman/cron.log 2>&1
0 3 1 * *       foreman    cd ${FOREMAN_HOME} && /usr/sbin/foreman-rake reports:monthly | gawk '{ print strftime("[%Y-%m-%d %H:%M:%S]"), $0 }' >>/var/log/foreman/cron.log 2>&1

# Expire old reports
30 7 * * *      foreman    cd ${FOREMAN_HOME} && /usr/sbin/foreman-rake reports:expire | gawk '{ print strftime("[%Y-%m-%d %H:%M:%S]"), $0 }' >>/var/log/foreman/cron.log 2>&1

# Refreshes ldap usergroups. Can be disabled if you're not using LDAP authentication.
*/30 * * * *    foreman    cd ${FOREMAN_HOME} && /usr/sbin/foreman-rake ldap:refresh_usergroups | gawk '{ print strftime("[%Y-%m-%d %H:%M:%S]"), $0 }' >>/var/log/foreman/cron.log 2>&1
# Clean expired notifications
0 6 * * 0       foreman    cd ${FOREMAN_HOME} && /usr/sbin/foreman-rake notifications:clean | gawk '{ print strftime("[%Y-%m-%d %H:%M:%S]"), $0 }' >>/var/log/foreman/cron.log 2>&1
