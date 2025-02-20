#!/bin/sh

cat $1 | tail -n +2 | awk -F"," -v OFS="" '{print $3, ", " $24, ", " $51}' | python3 O6.py