import collections

def swapchars (s) :
	c = collections.Counter(s.lower())
	del c[' ']
	del c['\'']
	del c['.']
	del c[',']
	del c['-']
	clist = c.most_common()

	(m,_) = clist[0]
	(l,_) = clist[-1]

	slist = list(s)

	for i in range(0,len(slist)):
		if slist[i] == m:
			slist[i] = l
		elif slist[i] == l:
			slist[i] = m

	output = "".join(slist)

	return output


def sortcat (n, *args) :
	output = ""
	slist = []

	for arg in args:
		slist.append(arg)

	slist.sort(key = len)
	slist.reverse()

	if n == -1:
		output = "".join(slist)
	else:
		for i in range(0,n):
			output += slist[i]

	print output

def bluesclues (s):
	d = {}
	with open("states.txt") as f:
		for line in f:
			(val,key) = line.split(',')
			d[key] = val

	s += '\n'
	return d[s]

def bluesbooze (s):
	d = {}
	with open("states.txt") as f:
		for line in f:
			(key,val) = line.split(',')
			d[key] = val

	output = d[s]
	output = output[:-1]
	return (output)





