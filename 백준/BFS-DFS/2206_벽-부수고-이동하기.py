from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]

n, m = map(int, input().split())

map = []
for i in range(n):
    map.append(list(input()))

queue = deque()
queue.append((0, 0, 0))

result = [[[0] * 2 for _ in range(m)] for _ in range(n)]
result[0][0][0] = 1

def BFS():
    while queue:
        x, y, break_cnt = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return result[x][y][break_cnt]

        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue
            
            if map[new_x][new_y] == "0" and result[new_x][new_y][break_cnt] == 0:
                result[new_x][new_y][break_cnt] = result[x][y][break_cnt] + 1
                queue.append((new_x, new_y, break_cnt))
            elif map[new_x][new_y] == "1" and break_cnt == 0 :
                result[new_x][new_y][1] = result[x][y][0] + 1
                queue.append((new_x, new_y, 1))
    
    return -1

print(BFS())

"""
from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]

n, m = map(int, input().split())

map = []
for i in range(n):
    map.append(list(input()))

queue = deque()
queue.append((0, 0, 0))

result = [[0] * m  for _ in range(n)]
result[0][0] = 1

def BFS() :
    while queue:
        x, y, break_cnt = queue.pop()

        if x == n - 1 and y == m - 1:
            return result[x][y]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue
            if map[new_x][new_y] == "0" and result[new_x][new_y] == 0:
                result[new_x][new_y] = result[x][y] + 1
                queue.append([new_x, new_y, break_cnt])
            elif map[new_x][new_y] == "1" and break_cnt == 0 :
                result[new_x][new_y] = result[x][y] + 1
                queue.append([new_x, new_y, 1])
    return -1

print(BFS())
"""