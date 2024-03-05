"""
https://www.acmicpc.net/problem/14940
"""
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

n, m = map(int, input().split())

graph = []
visited = [[-1] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            first_x,first_y = j, i

queue = deque()
queue.append([first_x, first_y])
visited[first_y][first_x] = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx >= m or nx < 0 or ny >= n or ny < 0:
            continue

        if visited[ny][nx] == -1 and graph[ny][nx] == 1:
            visited[ny][nx] = visited[y][x] + 1
            queue.append([nx,ny])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end = " ")
        else : 
            print(visited[i][j], end =" ")
    print()