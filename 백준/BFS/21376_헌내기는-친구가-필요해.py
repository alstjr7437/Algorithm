from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

n, m = map(int, input().split())
campus = []
count = 0
for i in range(n):
    campus.append(list(input()))

queue = deque()

# 제일 처음 I 넣어주기 
for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            queue.append([i, j])

while queue:
    a = queue.pop()
    # 친구인지
    if campus[a[0]][a[1]] == "P":
        count += 1
    # 방문 처리 해주기
    campus[a[0]][a[1]] = "X"
    for i in range(4):
        new_x, new_y = a[0] + dx[i], a[1] + dy[i]
        # 범위 확인
        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
            continue
        # 못가는 곳이 아니거나 이미 방문한 곳이 아니면
        if campus[new_x][new_y] != "X":
            queue.append([new_x, new_y])

if count == 0 :
    print('TT')
else :
    print(count)