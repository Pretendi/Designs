import math

def p3(n):#returns a list of the prime factors
    prim = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            prim.append(d)
            n //= d
        d += 1
    if n > 1:
       prim.append(n)
    return prim


def p10(n):#returns the sum of all primes less than this number
	tota = 0
	for i in range(1,n):
		if(len(p3(i))==1):
			tota += i
	print tota

p10(2000000)
