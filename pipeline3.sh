#!/bin/sh

    cat $1 | \
    bzcat Open_Data_RDW__Gekentekende_voertuigen.csv.bz2 | \
    tail -n +2 | \
    awk -F "," '($56 == "Ja" ) { print $1, $4}' | \ 
	sort | \ 
	uniq -c | \  
    sort -n | \
# haal aantal voorkomens weg
    head -n 10 | \