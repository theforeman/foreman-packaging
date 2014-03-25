#!/bin/bash

for spec in */*.spec; do
  d=$(dirname $spec)
  source0=$(spectool --list-files $spec | awk '{print $2}' | head -n1)
  sourcebase=$(basename "$source0")
  [ -h $d/$sourcebase ] || continue
  git annex whereis "$d/$sourcebase" | grep -q " web" && continue
  git annex addurl --file "$d/$sourcebase" "$source0"
done
