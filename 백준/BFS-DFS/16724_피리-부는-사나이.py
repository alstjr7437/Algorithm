from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)] 
result = 0


def dfs(x,y):
    global result

    visited[y][x] = 1
    cycle.append([x, y])

    if graph[y][x] == "U":
        y -= 1
    elif graph[y][x] == "D":
        y += 1
    elif graph[y][x] == "L":
        x -= 1
    elif graph[y][x] == "R":
        x += 1

    if visited[y][x] == 1:
        if [x, y] in cycle:
            result += 1
    else :
        dfs(x,y)

for y in range(n):
    for x in range(m):
        if(visited[y][x] == 0): 
            cycle = []
            dfs(x, y)

print(result)

