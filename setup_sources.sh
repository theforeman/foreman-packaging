#!/bin/bash

dir='./packages/*/*'
if [ -n "$1" ]
then
  dir=$1
  if ! [ -d "$1" ]
  then
    [ -d "./packages/foreman/$1" ] && dir="./packages/foreman/$1"
    [ -d "./packages/plugins/$1" ] && dir="./packages/plugins/$1"
    [ -d "./packages/katello/$1" ] && dir="./packages/katello/$1"
  fi
fi

for spec in $dir/*.spec; do
  d=$(dirname $spec)
  for source in $(spectool --list-files $spec | awk '{print $2}'); do
    sourcebase=$(basename "$source")
    [ -h $d/$sourcebase ] || continue
    git annex whereis "$d/$sourcebase" 2>/dev/null | grep -q " web:" && continue
    git annex addurl --file "$d/$sourcebase" "$source"
  done
done
