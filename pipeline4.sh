#!/bin/sh
cat $1 | tail -n +2 | awk -F "," '($2 == "Personenauto" || $2 == "auto") {print $3,", ",$21}' | python3 O4.py | sort -n