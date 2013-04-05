PACKAGE_NAME='foreman'

REPO='git://github.com/theforeman/foreman.git'
BRANCH='develop'

function setup_build {
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

}
