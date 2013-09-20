PACKAGE_NAME='foreman-installer'

REPO='git://github.com/theforeman/foreman-installer.git'
if [[ "$2" == "nightly" ]] ; then
  BRANCH="develop"
else
  BRANCH='d18811d0592e54c9d35e72401c726af24c027029'
fi

function setup_build {
  if [[ "$2" == "nightly" ]] ; then
    LAST_COMMIT=$($GIT rev-list HEAD|/usr/bin/head -n 1)

    # Add 'nightly' to changelog

    DATE=$(date -R)
    UNIXTIME=$(date +%s)
    RELEASE="9999+debian1~nightlybuild${UNIXTIME}"
    MAINTAINER="Greg Sutcliffe <gsutclif@redhat.com>"

    mv debian/changelog debian/changelog.tmp

    echo "$PACKAGE_NAME ($RELEASE) UNRELEASED; urgency=low

  * Automatically built package based on the state of
    $REPO at commit $LAST_COMMIT

 -- $MAINTAINER  $DATE
" > debian/changelog

    cat debian/changelog.tmp >> debian/changelog
    rm -f debian/changelog.tmp

    # Add 'nightly' to VERSION
    echo "`cat VERSION`-${LAST_COMMIT}" > VERSION
  else
    echo "not nightly: skipped setup_build"
  fi
}
