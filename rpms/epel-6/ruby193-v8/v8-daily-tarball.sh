#!/bin/bash

# This script checks out v8 source from svn.

LOCALDIR=`pwd`
TODAYSDATE=`date +%Y%m%d`
USAGE="Usage: v8-daily-tarball.sh [-hrv]"
VERBOSE=false

while getopts "hv" opt; do
   case $opt in
      h  ) printf "$USAGE\n"
           printf "\nAvailable command line options:\n"
           printf "%b\t-h\t\tthis help\n"
           printf "%b\t-v\t\tverbose output\n\n"
           exit 1 ;;
      v  ) VERBOSE=true
           printf "[VERBOSE]: Enabled\n" ;;
      \? ) printf "$USAGE\n"
           exit 1 ;;
   esac
done

# If the directory is there, just nuke it and continue.
if [ -d v8-$TODAYSDATE ]; then
   if [ "$VERBOSE" = "true" ]; then
      printf "[VERBOSE]: Conflicting directory found, removing v8-$TODAYSDATE/\n"
   fi
   rm -rf v8-$TODAYSDATE/
   if [ "$VERBOSE" = "true" ]; then
      printf "[VERBOSE]: Removed conflicting directory: v8-$TODAYSDATE/\n"
   fi
fi

printf "Checking out the source tree. This will take some time.\n"

if [ "$VERBOSE" = "true" ]; then
   svn checkout http://v8.googlecode.com/svn/trunk/ v8-$TODAYSDATE
else
   svn --quiet checkout http://v8.googlecode.com/svn/trunk v8-$TODAYSDATE
fi

# Determine SVN rev and Version of v8 
cd v8-$TODAYSDATE/
SVNREV=`svnversion`   
V8_VERSION=`head -n1 ChangeLog |cut -f2 -d: |sed 's| Version ||g'`
cd ..

printf "V8 ($V8_VERSION) svn$SVNREV [$TODAYSDATE] checked out\n"

FULLVER=`echo ${V8_VERSION}-${TODAYSDATE}svn${SVNREV}`

# Get rid of .svn bits to save space
if [ "$VERBOSE" = "true" ]; then
   printf "[VERBOSE]: Removing unnecessary .svn bits\n"
fi
find v8-$TODAYSDATE -depth -name .svn -type d -exec rm -rf {} \;

# Now, lets look for the final target directory, without svnrev.
if [ -d v8-$FULLVER ]; then
   if [ "$VERBOSE" = "true" ]; then
      printf "[VERBOSE]: Removing conflicting directory: v8-$FULLVER/\n"
   fi
   rm -rf v8-$FULLVER/
   if [ "$VERBOSE" = "true" ]; then
      printf "[VERBOSE]: Removed conflicting directory: v8-$FULLVER/\n"
   fi
fi

# At this point, we know the v8 target directory does not exist, time to rename the checkout
if [ "$VERBOSE" = "true" ]; then
   printf "[VERBOSE]: Renaming checkout directory from: v8-$TODAYSDATE/ to: v8-$FULLVER/\n"
fi
mv v8-$TODAYSDATE/ v8-$FULLVER/

# Now, lets look for the tarball.
if [ -f v8-$FULLVER.tar.bz2 ]; then
   if [ "$VERBOSE" = "true" ]; then
      printf "[VERBOSE]: Found existing tarball matching v8-$FULLVER.tar.bz2, removing.\n"
   fi
   rm -f v8-$FULLVER.tar.bz2
   if [ "$VERBOSE" = "true" ]; then
      printf "[VERBOSE]: Removed conflicting file: v8-$FULLVER.tar.bz2\n"
   fi
fi
         
if [ "$VERBOSE" = "true" ]; then
   printf "[VERBOSE]: Creating tarball: v8-$FULLVER.tar.bz2\n"
fi
tar cfj v8-$FULLVER.tar.bz2 v8-$FULLVER

# All done.
printf "Daily v8 source processed and ready: v8-$FULLVER.tar.bz2\n"
exit 0
