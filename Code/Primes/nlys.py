import json

with open('r1.txt', 'rU') as in_file:
    data = in_file.read().split(', ')
    data2 = data[:]

for i in range(0, len(data)):
	tmp  = sorted(data[i])
	data[i] = ''.join(tmp)

bgg = {}
for i in range(0, len(data)):
	bgg.setdefault(data[i], [])
	bgg[data[i]].append(i)
	
bgg2 = {}
for i in bgg:
	if len(bgg[i])>2:
		bgg2[i]=bgg[i]
		for j in range(0,len(bgg2[i])):
			bgg2[i][j] = int(data2[int(bgg2[i][j])])

def lstrdr(lst=[]):#do this recursively
	if(len(lst) == 2):
		return False
	tmplst = []
	for i in range(1, len(lst)):
		tmplst.append(lst[i]-lst[0])
	for i in range(0, len(tmplst)):
		for j in range(0, len(tmplst)):
			if(tmplst[j] == 2*tmplst[i]):
				return True 	
	lst = lst[1:]
	return lstrdr(lst)

sccss = []
for i in bgg2:
	if(lstrdr(bgg2[i])):
		sccss.append(i)

#print type(bgg2), type(bgg2["1789"]), type(bgg2["1789"][0])
print sccss
print bgg2['2699']
