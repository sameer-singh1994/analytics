import re, math
from collections import Counter
import csv

WORD = re.compile(r'\w+')

def texttovec(txt):
	return Counter(WORD.findall(txt))

def getcosine(v1, v2):
	intersection = set(v1.keys()) & set(v2.keys())
	n = sum([v1[x] * v2[x] for x in intersection])
	sum1 = sum([v1[x]**2 for x in v1.keys()])
	sum2 = sum([v2[x]**2 for x in v2.keys()])
	d = math.sqrt(sum1) * math.sqrt(sum2)

	if not d:
	    return 0.0
	else:
	    return float(n) / d

words = []
with open('Deduplication Problem - Sample Dataset.csv','rU') as f:
	reader = csv.reader(f)
	words = list(reader)
	words = words[1:]

dob = dict()
for i in words:
	if str(i[1])+"#"+str(i[2])+"#"+str(i[3]) not in dict.keys(dob):
		dob[str(i[1])+"#"+str(i[2])+"#"+str(i[3])] = []
	dob[str(i[1])+"#"+str(i[2])+"#"+str(i[3])].append(i)

for z in dob:
	temp = []
	temp = dob[z]
	ans = []
	for i in temp:
		set1 = set()
		set1.add(i[0])
		for j in temp:
			if getcosine(texttovec(i[0].strip().lower()), texttovec(j[0].strip().lower())) > 0.5:
				set1.add(j[0])
		ans.append(set1)
		
	ans = [set(item) for item in set(frozenset(item) for item in ans)]
	tokri = []
	for m in ans:
		for n in ans:
			if m.issubset(n) and m != n:
				tokri.append(m)
				break
	ans = [item for item in ans if item not in tokri]
	disc = z.split('#')
	for i in ans:
		print list(i)[0]+" "+disc[0]+" "+disc[1]+" "+disc[2]
	