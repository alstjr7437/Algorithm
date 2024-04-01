"""
https://www.acmicpc.net/problem/16234
"""
from collections import deque
import sys

def BFS(y,x) :
    queue = deque()
    result = []
    queue.append((x,y))
    result.append((x,y))
    while queue : 
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
                if L <= abs(ground[y][x] - ground[ny][nx]) <= R:     # L,R로 동맹 찾기
                    visited[ny][nx] = 1
                    queue.append((nx,ny))
                    result.append((nx,ny))
    return result

dx = [0,0,-1,1]
dy = [1,-1,0,0]

N,L,R = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(N)]

day = 0 

while 1:
    visited = [[0] * (N+1) for _ in range(N+1)]
    stop = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                result = BFS(i,j)       # 동맹을 맺은 나라 가져오기
                if len(result) > 1:     # 동맹이 있으면 평균값 넣기
                    stop = 1
                    num = sum([ground[y][x] for x, y in result]) // len(result)
                    for x,y in result:
                        ground[y][x] = num
    if stop == 0:       # 동맹을 맺을 수 없다면
        break
    day += 1

print(day)