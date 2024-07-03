from collections import deque
import sys

dx = [0,0,-1,1]
dy = [1,-1,0,0]

input = sys.stdin.readline

n = int(input())
visited = [[False] * n for _ in range(n)] 
graph = [list(input().rstrip()) for _ in range(n)]
queue = deque()
result = 0


def bfs():
    global result 
    while queue:
        x, y, color = queue.popleft()
        for i in range(4):
            nx, ny= x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if color == graph[ny][nx] and not visited[ny][nx] :
                queue.append((nx, ny, color))
                visited[ny][nx] = True
    result += 1

def resultCount():
    global result 
    for y in range(n):
        for x in range(n):
            if not visited[y][x] :
                queue.append((x, y, graph[y][x]))
                visited[y][x] = True
                bfs()
    print(result, end=" ")
    result = 0

resultCount()

# 적록색약 적용 부분
for y in range(n):
    for x in range(n):
        visited[y][x] = False
        if graph[y][x] == "G":
            graph[y][x] = "R"

resultCount()      
