import sys
aantalmerk = {}
aantaldatum = {}
somleeftijd = {}
leeftijdgem = {}


for line in sys.stdin:
    splitten = line.split(", ")
    if splitten[0] not in aantalmerk:
        aantalmerk[splitten[0]] = 0
    aantalmerk[splitten[0]] += 1

    #als er geen datum is negeert hij hem hier
    if splitten[1] == '\n':
        pass
    
    #per merk en datum totaal aantal auto's
    if splitten [0] not in aantaldatum:
        aantaldatum[splitten[0]] = 0
    aantaldatum[splitten[0]] += 1

    #leeftijd optellen per merk
    datum = splitten[1].split("/")
    if splitten[0] not in somleeftijd:
        somleeftijd[splitten[0]] = 0
    somleeftijd[splitten[0]] += 2021 - int(datum[2])

#berekent gemiddelde en daarna print hij alles
for var in aantalmerk:
    if aantalmerk[var] >= 100000:
        leeftijdgem[var] = round(somleeftijd[var] / aantaldatum[var])
        print (" " + str(leeftijdgem[var]) + " " + var)