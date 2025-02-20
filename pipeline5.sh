#!/bin/sh

cat $1 | tail -n +2 | awk -F"," -v OFS="" '{print $6}' | python3 O5.py