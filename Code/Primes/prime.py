import json

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

refined = []
for i in range(1000,9999):
        if is_prime(i):
                refined.append(i)

wrtr= open('r1.txt', 'w')
json.dump(refined,wrtr)
wrtr.close()                          
