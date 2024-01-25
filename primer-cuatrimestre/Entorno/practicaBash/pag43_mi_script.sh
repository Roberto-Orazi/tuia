#!/usr/bin/env bash

echo '$0 ->' $0
echo '$1 ->' $1
echo '$2 ->' $2
echo '$# ->' $#
echo '$@ ->' $@
printf "%s\n" "$@"
echo '$* ->' $*
printf "%s\n" "$*"

exit 0
