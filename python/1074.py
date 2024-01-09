N, r, c = map(int, input().split())
dx = [1,-1,1,1]
dy = [0,1,0,-1]
result = [[0] * (2**N) for _ in range(2**N)]
x,y = 0, 0

for i in range(4**N):
    result[y][x] = i
    if dx[i%4] + x >= 2**N :
        x = 0
        y += 1
    else : 
        x = dx[i%4] + x 
        y = dy[i%4] + y

print(result[r][c])
