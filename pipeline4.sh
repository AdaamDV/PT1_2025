#!/bin/sh
cat $1 | tail -n +2 | awk -F"," -v OFS="" '{print $3,", ",$21}' | python3 O4.py | sort -n