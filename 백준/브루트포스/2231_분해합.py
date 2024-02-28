"""
https://www.acmicpc.net/problem/2231
"""

import sys

n = int(input())

for i in range(n):
    temp = i
    li = list(map(int, str(i)))
    for j in li:
        temp += j
    if temp == n:
        print(i)
        sys.exit()

print(0)