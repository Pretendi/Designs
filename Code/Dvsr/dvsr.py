import math
import time
from collections import Counter

def ghtst(n):#returns 1 if a number has 8 divisors, 0 otherwise
	rt = int(math.ceil(math.sqrt(n)))
	dvsrs = 0
	for i in range(2, rt+1):
		if(n%i==0):
			dvsrs += 1  
	if(dvsrs == 3):
		return 1
	return 0

def primes(n):#returns a list of the prime factors
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def tstr(s,f):#finds the number of numbers that have 8 divisors s.t. they are between s and f
	rslt = 0
	for i in range(s,f):
		tmpdct = Counter(primes(i))
		cntr = 1 
		for j in tmpdct:
			cntr *= (tmpdct[j]+1)
		if cntr == 8:
			rslt += 1
	return rslt

def chunker():
	final= 0
	
	for i in range(0,1):
		final += tstr(i*10**6,(i+1)*10**6)
	print final

print tstr(1,10000000)

















