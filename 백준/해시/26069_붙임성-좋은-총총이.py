import sys
input = sys.stdin.readline

n = int(input())
result = {'ChongChong'}

for i in range(1, n+1):
    a, b = input().split()

    if a in result:
        result.add(b)

    if b in result:
        result.add(a)

print(len(result))

"""
from collections import deque

n = int(input())

graph = {}
visited = []
queue = deque()
temp = 0 

for _ in range(n):
    a,b = input().split()
    if a == "ChongChong" and b == "ChongChong":
        continue
    if a == "ChongChong" or b == "ChongChong":
        temp = 1 
    if temp == 1:
        if a != "ChongChong" and b != "ChongChong":
            if a not in graph and b not in graph :
                continue
        if a not in graph:
            graph[a] = [b]
        else :
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else :
            graph[b].append(a)

print(graph)

if "ChongChong" in graph:
    queue.append("ChongChong")
    result = 1
    while queue:
        cur = queue.popleft()
        visited.append(cur)
        temp = graph[cur]
        if temp in visited:
            continue
        for i in temp:
            if i not in visited:
                result += 1   
                queue.append(i)
    print(result)
else :
    print(1)
"""
