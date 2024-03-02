"""
https://www.acmicpc.net/problem/18111
"""
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

ground = []
for i in range(n):
    ground.append(list(map(int, input().split())))

answer = int(1e9)
idx = 0

for i in range(257):
    current = 0
    take = 0
    for j in range(n):
        for z in range(m):
            if ground[j][z] > i:
                take += ground[j][z] - i 
            else:
                current += i - ground[j][z]
    if current > take + b:
        continue
    count = take * 2 + current
    if count <= answer:
        answer = count
        idx = i

print(answer, idx)