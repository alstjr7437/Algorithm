"""
https://www.acmicpc.net/problem/1931
"""

from collections import deque

n = int(input())

result = []
for i in range(n):
    result.append(list(map(int, input().split())))
result.sort(key=lambda x:(x[1],x[0]))

room = result[0][1]
count = 1

for i in range(1,n):
    if result[i][0] >= room:
        room = result[i][1]
        count += 1

print(count)
