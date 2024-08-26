import sys
from collections import deque

input = sys.stdin.readline

N, M, k = map(int, input().split())
student = list(map(int, input().split()))
friend = [[] for i in range(N+1)]
visited = [False] * (N+1)
resultMoney = 0

for _ in range(M) :
    a,b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    group_min_cost = student[start-1]
    
    while queue:
        node = queue.popleft()
        
        for neighbor in friend[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                group_min_cost = min(group_min_cost, student[neighbor-1])
    
    return group_min_cost

for i in range(1, N+1):
    if not visited[i]:
        resultMoney += bfs(i)

if resultMoney > k:
    print("Oh no")
else:
    print(resultMoney)