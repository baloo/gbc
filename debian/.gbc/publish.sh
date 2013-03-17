#!/bin/sh

echo "DIST: $1"

shift

debsign -k707EFD41 $*
