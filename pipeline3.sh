#!/bin/sh

    bzcat $1 | tail -n +2 | awk -F "," '($56 == "Ja" ) { print $3, $4}' | sort | uniq -c | sort -n -r | awk '{print $2, ",", $3}' | head -n 10