#!/bin/bash
begin='<!--RGD-START-->'
end='<!--RGD-END-->'

original_locale=$LC_COLLATE
export LC_COLLATE=en_GB.UTF-8
TEMP=$(mktemp)
trap "rm -f $TEMP" EXIT

for FILE in comps/comps-*.xml
do
  for G in $(egrep "%package\s+doc" packages/*/*/*spec | awk -F/ '{print $3}'); do
    grep "[>-]$G<" $FILE | sed 's/<\//-doc<\//'
  done | sort -u > $TEMP
  sed -i -e "/$begin/,/$end/{ /$begin/{p; r $TEMP
    }; /$end/p; d }" $FILE
done
export LC_COLLATE=$original_locale
