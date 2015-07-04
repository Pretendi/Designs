import math

def xslvr(j):
	if j == 0:
                return 0
	if j == 1:
		return 1	
	if((j%2)==0):
		k = j/2
		return ((3*xslvr(k) + 2*xslvr(math.floor(k/2)))%2**60)
	if((j%2)==1):
		k = (j-1)/2
		return ((2*xslvr(k) + 3*xslvr(math.floor(k/2)))%2**60)
	print "error"

def yslvr(n,j):
	if (j >= n):
		return xslvr(j)
	if (j < n):
		return (2**60 - 1 - max(yslvr(n,2*j),yslvr(n,2*j+1)))


def aslvr(n):
	return yslvr(n,1)

print aslvr(10**12)
