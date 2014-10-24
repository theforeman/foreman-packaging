#!/bin/bash
begin='<!--RGD-START-->'
end='<!--RGD-END-->'

TEMP=$(mktemp)
trap "rm -f $TEMP" EXIT

for FILE in comps/comps-*.xml
do
  for G in $(egrep "%package\s+doc" rubygem-*/*spec | awk -F/ '{print $1}'); do
    grep "[>-]$G<" $FILE | sed 's/<\//-doc<\//'
  done | sort -u > $TEMP
  sed -i -e "/$begin/,/$end/{ /$begin/{p; r $TEMP
    }; /$end/p; d }" $FILE
done
