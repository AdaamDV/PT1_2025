#!/bin/sh

	bzcat $1 | tail -n +2 | awk -F"," -v OFS="" '($2 == "Personenauto" || $2 == "auto") {print $6}' | python3 O5.py