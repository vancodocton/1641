# To add a new cell, type ''
# To add a new markdown cell, type ' [markdown]'

import math
import numpy


# maxN = 2**31
maxN = 10000
arr = numpy.random.randint(-maxN, maxN, size = 100)
print(arr)



# 2.a
posArr = [abs(x) for x in arr]
print(posArr)



def isPrime(num):
    if (num < 2): return False
    sqrtNum = int(math.sqrt(num))
    
    for i in range(2, sqrtNum + 1):
        if (num % i == 0):
            return False
    return True



# 2.b
# primes = []
# for x in posArr:
#     if (isPrime(x)):
#         primes.append(x)
# print(primes)
primes = [x for x in filter(isPrime, posArr)]
print(primes)



# 2.c
# res = []
# for prime in primes:
#     res = []
#     for number in posArr:
#         if (number % prime == 0):
#             res.append(number)
#     print(prime, res)

for prime in primes:
    res = [x for x in filter(lambda y: y % prime == 0, posArr)]
    print(prime, res)


