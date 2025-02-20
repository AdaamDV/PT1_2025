from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import sys

aantaldagen = [0 for x in range(7)]

#datum inlezen per line en aantal weekdagen tellen
for line in sys.stdin:
	if line != "\n": #negeer alle regels zonder datum
		dt = datetime.strptime(line.rstrip(), '%d/%m/%Y')
		aantaldagen[dt.weekday()] += 1

#barplot
f = plt.figure()
objects = ('Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za', 'Zo')
y_pos = np.arange(len(objects))
plt.bar(y_pos, aantaldagen, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Aantal tenaamstellingen')
plt.title('Tenaamstellingen per dag')

#barplot opslaan
f.savefig("barplot.pdf", bbox_inches='tight')
