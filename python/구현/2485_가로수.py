"""
https://www.acmicpc.net/problem/2485
"""
from math import gcd

n = int(input())
garosu = []
distance = []

for i in range(n):
    garosu.append(int(input()))

for i in range(0, n-1):
    distance.append(garosu[i+1] - garosu[i])

공약수 = distance[0]
for i in range(1, len(distance)):
    공약수 = gcd(공약수,distance[i])

print(((max(garosu) - min(garosu)) // 공약수 + 1) - len(garosu))