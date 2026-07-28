SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

RAILS_ENV=production
FOREMAN_HOME=/usr/share/foreman


# Run hourly Foreman cron jobs
30 * * * *      foreman    cd ${FOREMAN_HOME} && /usr/sbin/foreman-rake cron:hourly 2>&1 | gawk '{ print strftime("[\%Y-\%m-\%d \%H:\%M:\%S]"), $0 }' >>/var/log/foreman/cron.log

# Run daily Foreman cron jobs
0 2 * * *       foreman    cd ${FOREMAN_HOME} && /usr/sbin/foreman-rake cron:daily 2>&1 | gawk '{ print strftime("[\%Y-\%m-\%d \%H:\%M:\%S]"), $0 }' >>/var/log/foreman/cron.log

# Run weekly Foreman cron jobs
0 5 * * 0       foreman    cd ${FOREMAN_HOME} && /usr/sbin/foreman-rake cron:weekly 2>&1 | gawk '{ print strftime("[\%Y-\%m-\%d \%H:\%M:\%S]"), $0 }' >>/var/log/foreman/cron.log

# Run monthly Foreman cron jobs
0 3 1 * *       foreman    cd ${FOREMAN_HOME} && /usr/sbin/foreman-rake cron:monthly 2>&1 | gawk '{ print strftime("[\%Y-\%m-\%d \%H:\%M:\%S]"), $0 }' >>/var/log/foreman/cron.log
