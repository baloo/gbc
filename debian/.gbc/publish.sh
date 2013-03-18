#!/bin/sh

here=$(cd `dirname $0`; pwd)

case $1 in
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

dist=$1
shift

debsign -k707EFD41 $*

dput --config $here/dput.cf $dist $*
