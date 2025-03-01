#!/bin/sh

	bzcat $1 | tail -n +2 | awk -F"," -v OFS="" '($2 == "Personenauto" || $2 == "auto") {print $3, ", " $24, ", " $51}' | python3 O6.py