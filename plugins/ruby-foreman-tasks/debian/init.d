#!/bin/bash
#! /bin/sh
### BEGIN INIT INFO
# Provides:          foreman-tasks
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Init script for foreman-tasks
# Description:       Init script for foreman-tasks service used by foreman-tasks foreman plugin
### END INIT INFO

# Author: Marek Hulan <mhulan@redhat.com>

PATH=/sbin:/usr/sbin:/bin:/usr/bin
DESC="Foreman-tasks start dynflow executor"
NAME=foreman-tasks
DAEMON=/usr/bin/$NAME
SCRIPTNAME=/etc/init.d/$NAME

# Exit if the package is not installed
[ -x "$DAEMON" ] || exit 0

# Read configuration variable file if it is present
[ -r /etc/default/$NAME ] && . /etc/default/$NAME

# Load the VERBOSE setting and other rcS variables
. /lib/init/vars.sh

# Define LSB log_* functions.
# Depend on lsb-base (>= 3.2-14) to ensure that this file is present
# and status_of_proc is working.
. /lib/lsb/init-functions

RETVAL=0
FOREMAN_USER=${FOREMAN_USER:-foreman}
FOREMAN_HOME=${FOREMAN_HOME:-/usr/share/foreman}
FOREMAN_DATA_DIR=${FOREMAN_DATA_DIR:-/var/lib/foreman}
FOREMAN_ENV=${FOREMAN_ENV:-production}
FOREMAN_TASK_PARAMS=${FOREMAN_TASK_PARAMS:--p foreman}
FOREMAN_PID_DIR=$FOREMAN_HOME/tmp/pids
FOREMAN_LOG_DIR=${FOREMAN_LOG_DIR:-/var/log/foreman}
DAEMON="/usr/bin/foreman-tasks"
PID_FILE=$FOREMAN_PID_DIR/dynflow_executor_monitor.pid
export RAILS_ENV=$FOREMAN_ENV
export FOREMAN_LOGGING=${FOREMAN_LOGGING:-warn}
export FOREMAN_LOGGING_SQL=${FOREMAN_LOGGING_SQL:-warn}
export RAILS_RELATIVE_URL_ROOT=$FOREMAN_PREFIX

print_higher() {
    if [ 0$1 -gt 0$2 ]; then
        echo $1
    else
        echo $2
    fi
}

print_lower() {
    if [ 0$1 -gt 0$2 ]; then
        echo $2
    else
        echo $1
    fi
}

__pids_var_run() {
        local base=${1##*/}
        local pid_file=${2:-/var/run/$base.pid}

        pid=
        if [ -f "$pid_file" ] ; then
                local line p
                read line < "$pid_file"
                for p in $line ; do
                        [ -z "${p//[0-9]/}" -a -d "/proc/$p" ] && pid="$pid $p"
                done
                if [ -n "$pid" ]; then
                        return 0
                fi
                return 1 # "Program is dead and /var/run pid file exists"
        fi
        return 3 # "Program is not running"
}

# Output PIDs of matching processes, found using pidof
__pids_pidof() {
        pidof -c -o $$ -o $PPID -o %PPID -x "$1" || \
                pidof -c -o $$ -o $PPID -o %PPID -x "${1##*/}"
}

status_of_one() {
    PID_FILE="$1"
    local RC
    local RETVAL
    if [ -f "$PID_FILE" ]; then
        # set $pid
        __pids_var_run NOT_USED $PID_FILE
        RC=$?
        if [ -n "$pid" -o 0$RC -gt 0 ]; then
            RETVAL=2 # Program is dead and pid file exists
        fi
        #check if proces with pid from the file is running
        if status_of_proc -p $PID_FILE /usr/bin/$NAME $NAME; then
            echo "running."
            RETVAL=0
        else
            echo "not running."
            RETVAL=1
        fi
    else
        echo "not running."
        RETVAL=3
    fi
    return $RETVAL
}

kstatus() {
    RETVAL=0
    SECONDVAL=256
    echo -n "dynflow_executor is "
    status_of_one $FOREMAN_PID_DIR/dynflow_executor.pid
    RC=$?
    RETVAL=$( print_higher $RC $RETVAL )
    SECONDVAL=$( print_lower $RC $SECONDVAL )
    echo -n "dynflow_executor_monitor is "
    status_of_one $FOREMAN_PID_DIR/dynflow_executor_monitor.pid
    RC=$?
    RETVAL=$( print_higher $RC $RETVAL )
    SECONDVAL=$( print_lower $RC $SECONDVAL )
    if [  0$SECONDVAL -eq 0  -a  0$RETVAL -gt 0 ]; then
       # some is running, some not
       return 10
    else
       return $RETVAL
    fi
}

status_q() {
    kstatus &> /dev/null
    return $?
}

start() {

    echo -n $"Starting $NAME: "
    status_q
    STATUS=$?
    if [ 0$STATUS -eq 0 ]; then
        echo -n $"$NAME is already running. "
        RETVAL=0
        echo_success
    elif [ 0$STATUS -eq 10 ]; then
        echo -n $"Some processes of $NAME is already running. Some not. Please stop $NAME first."
        RETVAL=10
        log_end_msg 1
    else
        # rails expects you to run from the root of the app
        pushd ${FOREMAN_HOME} >/dev/null
        # start jobs
        su -s /bin/bash - ${FOREMAN_USER} -c "\
            RAILS_RELATIVE_URL_ROOT='$RAILS_RELATIVE_URL_ROOT' \
            RAILS_ENV='$RAILS_ENV' \
            FOREMAN_LOGGING='$FOREMAN_LOGGING' \
            FOREMAN_LOGGING_SQL='$FOREMAN_LOGGING_SQL' \
            $DAEMON $FOREMAN_TASK_PARAMS -m -n $FOREMAN_TASK_WORKERS start &>>${FOREMAN_LOG_DIR}/jobs-startup.log"
        RETVAL=$?
        if [ $RETVAL = 0 ]; then
            log_success_msg $NAME start
        else
            log_failure_msg $NAME start
        fi
        popd >/dev/null
    fi

    echo
    return $RETVAL
}

stop() {

    status_q
    STATUS=$?
    if [ 0$STATUS -eq 0 -o 0$STATUS -eq 10 ]; then
        # rails expects you to run from the root of the app
        pushd ${FOREMAN_HOME} >/dev/null
        su -s /bin/bash - ${FOREMAN_USER} -c "\
            RAILS_RELATIVE_URL_ROOT='$RAILS_RELATIVE_URL_ROOT' \
            RAILS_ENV='$RAILS_ENV' \
            FOREMAN_LOGGING='$FOREMAN_LOGGING' \
            FOREMAN_LOGGING_SQL='$FOREMAN_LOGGING_SQL' \
            $DAEMON $FOREMAN_TASK_PARAMS -m -n $FOREMAN_TASK_WORKERS stop &>>${FOREMAN_LOG_DIR}/jobs-startup.log"
        if [ -f $FOREMAN_PID_DIR/dynflow_executor_monitor.pid ]; then
            echo -n $"Stopping dynflow_executor_monitor: "
            killproc -p $FOREMAN_PID_DIR/dynflow_executor_monitor.pid
            echo
        fi
        if [ -f $FOREMAN_PID_DIR/dynflow_executor.pid ]; then
            echo -n $"Stopping dynflow_executor: "
            killproc -p $FOREMAN_PID_DIR/dynflow_executor.pid
            echo
        fi
       popd >/dev/null
        RETVAL=0
    else
        RETVAL=0
        echo -n "Stopping $NAME: "
        echo_failure
        echo
    fi

    return $RETVAL
}

restart() {
    stop
    start
}

condstop() {
    status_q
    STATUS=$?
    if [ 0$STATUS -eq 0 -o 0$STATUS -eq 10 ]; then
        stop
    else
        RETVAL=0
    fi
}

condrestart() {
    status_q
    STATUS=$?
    if [ 0$STATUS -eq 0 -o 0$STATUS -eq 10 ]; then
        restart
    else
        RETVAL=0
    fi
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    condrestart|try-restart)
        condrestart
        ;;
    condstop)
        condstop
        ;;
    status)
        kstatus
        RETVAL=$?
        ;;
    *)
        echo "Usage: {start|stop|restart|condrestart|condstop|status}"
        exit 1
        ;;
esac

exit $RETVAL

# vim:set sw=4 ts=4 et:
