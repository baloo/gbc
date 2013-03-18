#!/bin/sh

here=$(cd `dirname $0`; pwd)

case $1 in
  squeeze)
    repo=gbc-stable
    ;;
  squeeze-testing)
    repo=gbc-testing
    ;;
  squeeze-unstable)
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
