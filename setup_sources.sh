#!/bin/bash

dir='*'
[ -n "$1" ] && dir=$1

for spec in $dir/*.spec; do
  d=$(dirname $spec)
  source0=$(spectool --list-files $spec | awk '{print $2}' | head -n1)
  sourcebase=$(basename "$source0")
  [ -h $d/$sourcebase ] || continue
  git annex whereis "$d/$sourcebase" 2>/dev/null | grep -q " web" && continue
  git annex addurl --file "$d/$sourcebase" "$source0"
done
