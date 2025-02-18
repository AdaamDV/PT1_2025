#!/bin/sh

    cat $1 | tail -n +2 | awk -F "," '($2 == "Personenauto" || $2 == "auto") { print $1, $4}' | sort | uniq -c | sort -n | awk '{print $2, $3}' |head -n 10