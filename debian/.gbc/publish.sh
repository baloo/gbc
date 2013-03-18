#!/bin/sh -x

here=$(cd `dirname $0`; pwd)
dist=$1
shift

case $dist in
  stable)
    repo=gbc-stable
    ;;
  testing)
    repo=gbc-testing
    ;;
  unstable)
    repo=gbc-unstable
    ;;
  *)
    echo "$1 not handled"
    exit 1
esac


debsign -k707EFD41 $*

dput --config $here/dput.cf $repo $*
