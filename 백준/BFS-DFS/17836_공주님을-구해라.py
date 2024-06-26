import sys
from collections import deque

input = sys.stdin.readline
n, m, t = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)] 

queue = deque()

def bfs():
    gram = 10001
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        if (x, y) == (n-1, m-1):  # 목적지 (n-1, m-1)
            return min(visited[x][y] - 1, gram)
        if graph[x][y] == 2:  # 검을 찾은 경우
            gram = visited[x][y] - 1 + (n-1-x) + (m-1-y)
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return gram

res = bfs()

if res > t:
    print('Fail')
else:
    print(res)
