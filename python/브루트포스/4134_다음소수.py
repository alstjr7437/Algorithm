import sys
import math

def nextPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False  
    return True

n = int(sys.stdin.readline())

for i in range(n) :
    a = int(sys.stdin.readline())
    while True :
        if nextPrime(a) :
            print(a)
            break
        else : 
            a += 1