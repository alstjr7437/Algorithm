from collections import deque

def solution(maps):
    answer = 0
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    queue = deque([[0, 0]])
    
    while len(queue) > 0:
        nx, ny = queue.popleft()
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if x >= len(maps[0]) or x < 0 or y >= len(maps) or y < 0 or maps[y][x] == 0:
                continue    
            if maps[y][x] == 1:
                queue.append([x,y])
                maps[y][x] = maps[ny][nx] + 1
    
    result = maps[len(maps)-1][len(maps[0])-1]
    return result if maps[len(maps)-1][len(maps[0])-1] != 1 else -1