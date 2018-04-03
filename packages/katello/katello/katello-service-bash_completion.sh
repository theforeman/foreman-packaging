# Opts for every command
_katelloservice_help_opts="-h --help"
_katello_action_opts="restart stop start status list enable disable"
_katello_services="rh-mongodb34-mongod postgresql qpidd qdrouterd squid tomcat tomcat6 pulp_workers pulp_celerybeat pulp_resource_manager pulp_streamer foreman-proxy smart_proxy_dynflow_core httpd puppetserver foreman-tasks goferd"

_katello-service_exclude-only()
{
  local opts="${_katello_services}"
  COMPREPLY=($(compgen -W "${opts}" -- ${1}))
}

# Main function
_katello-service()
{
    local first second cur prev opts base line
    COMPREPLY=()
    first=${COMP_WORDS[1]}
    second=${COMP_WORDS[2]}
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    line=${COMP_LINE}

    # top-level commands and options
    if [[ $cur == -* ]]
    then
    opts="--only --exclude ${_katelloservice_help_opts}"
    else
    opts="${_katello_action_opts}"
    fi

    case "${prev}" in
        *--exclude*|*--only*)
        "_katello-service_exclude-only" "${cur}" "${prev}" "${line}"
        return 0
        ;;
    esac
    COMPREPLY=($(compgen -W "${opts}" -- ${cur}))
    return 0
}
complete -F _katello-service -o filenames katello-service words
