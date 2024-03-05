"""
https://www.acmicpc.net/problem/1260
"""
from collections import deque

n, m, v = map(int, input().split())
graph = { i : [] for i in range(1, n+1)}
visited = [False] * (n + 1)
visited2 = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1):
    graph[i].sort()

def bfs():
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        temp = queue.popleft()
        print(temp, end = " ")
        for i in graph[temp]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

def dfs(v):
    print(v, end = " ")
    for i in graph[v]:
        if visited2[i] == False:
            visited2[i] = True
            dfs(i)
    

visited2[v] = True
dfs(v)
print()
bfs()

