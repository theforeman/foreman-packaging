SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

RAILS_ENV=production
FOREMAN_HOME=/usr/share/foreman

# Clean up the session entries in the database
15 23 * * *     foreman    /usr/sbin/foreman-rake db:sessions:clear >>/var/log/foreman/cron.log 2>&1

# Send out recurring notifications
0 7 * * *       foreman    /usr/sbin/foreman-rake reports:daily >>/var/log/foreman/cron.log 2>&1
0 5 * * 0       foreman    /usr/sbin/foreman-rake reports:weekly >>/var/log/foreman/cron.log 2>&1
0 3 1 * *       foreman    /usr/sbin/foreman-rake reports:monthly >>/var/log/foreman/cron.log 2>&1

# Expire old reports
30 7 * * *      foreman    /usr/sbin/foreman-rake reports:expire >>/var/log/foreman/cron.log 2>&1

# Refreshes ldap usergroups. Can be disabled if you're not using LDAP authentication.
*/30 * * * *    foreman    /usr/sbin/foreman-rake ldap:refresh_usergroups >>/var/log/foreman/cron.log 2>&1

# Clean expired notifications
0 6 * * 0       foreman    /usr/sbin/foreman-rake notifications:clean >>/var/log/foreman/cron.log 2>&1
