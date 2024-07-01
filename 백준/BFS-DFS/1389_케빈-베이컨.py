import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    num = [0] * (n+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if i not in visited:
                num[i] = num[now] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)

result = []
for i in range(1, n+1):
    result.append(bfs(i))

print(result.index(min(result))+1)
