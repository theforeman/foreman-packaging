<!--
If your package needs to be released within one or more release streams, and/or distributions, please open PRs to each of those branches respectively. The easiest way to do this is to make the initial commit for the mainline branch (e.g. rpm/develop or deb/develop) and then cherry pick the commit hash onto each subsequent branch.

The Foreman Community supports the `develop` branch for active development and the latest two releases.
You can view the currently supported versions on [theforeman.org](https://theforeman.org/).
 
RPM Example:

    git checkout -b rpm/develop-foreman-tasks-1.0.1 rpm/develop

    # Make changes to update package

    git commit -a -m 'Release foreman-tasks-1.0.1'
    COMMIT=`git rev-parse HEAD`

    git checkout -b rpm/1.20-foreman-tasks-1.0.1-1.20 rpm/1.20
    git cherry-pick -x $COMMIT

DEB Example:

    git checkout -b deb/develop-foreman-tasks-1.0.1 deb/develop

    # Make changes to update package

    git commit -a -m 'Release foreman-tasks-1.0.1'
    COMMIT=`git rev-parse HEAD`

    git checkout -b deb/1.20-foreman-tasks-1.0.1-1.20 deb/1.20
    git cherry-pick -x $COMMIT

See Foreman's [plugin maintainer documentation](https://projects.theforeman.org/projects/foreman/wiki/How_to_Create_a_Plugin#Release-strategies) for more information.
-->
