#!/bin/sh

    bzcat $1 | tail -n +2 | awk -F "," '($2 == "Personenauto" || $2 == "auto") { print $1 }' | tr "A-Z" X | tr "0-9" 9 | sort | uniq
