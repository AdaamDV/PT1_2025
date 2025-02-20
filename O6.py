import sys
import numpy
import matplotlib.pyplot as plt 

catalogustotaal= {}
catalogusnummer = {}
somvermogen = {}
aantalvermogen = {}
aantalmerk1 = {}
aantalmerk2 = {}

#loopt over elke line 
for line in sys.stdin:
	splitten = line.split(", ")
	
	#negeert regels zonder cataloguswaarde
	if splitten[1] != "":

		#telt catalogustotaal en catalogusnummer	
		if splitten[0] not in catalogusnummer:
			catalogusnummer[splitten[0]] = 0
			catalogustotaal[splitten[0]] = 0.0
		catalogusnummer[splitten[0]] += 1
		catalogustotaal[splitten[0]] += float(splitten[1])
	
	#negeert regels zonder vermogen
	if splitten[2] != "\n":

		#telt somvermogen en aantalvermogen	
		if splitten[0] not in aantalvermogen:
			aantalvermogen[splitten[0]] = 0
			somvermogen[splitten[0]] = 0.0
		aantalvermogen[splitten[0]] += 1
		somvermogen[splitten[0]] += float(splitten[2])

	#telt aantal autos per merk
	if splitten[0] not in aantalmerk1:
		aantalmerk1[splitten[0]] = 0
	aantalmerk1[splitten[0]] += 1	

#lege arrays aanmaken voor scatterplot
x = numpy.empty(0);
y = numpy.empty(0)
area = numpy.empty(0)

#merken zonder enkele waarde niet meenemen in plot
for key in aantalmerk1:
	if key in catalogustotaal and key in somvermogen:
		aantalmerk2[key] = aantalmerk1[key]
		
#gemiddelde uitrekenen en plotten
i = 0
for key in aantalmerk2:	
	if aantalmerk2[key] >= 10000:
		i += 1
		x = numpy.append(x, catalogustotaal[key]/catalogusnummer[key])
		y = numpy.append(y, somvermogen[key]/aantalvermogen[key])
		area = numpy.append(area, aantalmerk2[key]/1000)
colors = numpy.random.rand(i)
f = plt.figure()
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
f.savefig("scatterplot.pdf")

