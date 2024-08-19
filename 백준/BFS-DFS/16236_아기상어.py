from collections import deque

dx, dy = [0,0,-1,1], [1,-1,0,0]

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

baby_shark = 2
shark_eaten = 0

for i in range(N):
    for j in range(N):
        if map[i][j] == 9:
            now_x, now_y = i, j
            map[i][j] = 0

def bfs():
    global now_x, now_y, baby_shark, shark_eaten

    queue = deque()
    queue.append((now_x, now_y))
    visited = [[False] * N for _ in range(N)]
    visited[now_x][now_y] = True
    distance = [[0] * N for _ in range(N)]
    temp = []

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and map[nx][ny] <= baby_shark:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    if 0 < map[nx][ny] < baby_shark:
                        temp.append((nx, ny, distance[nx][ny]))

    if temp:
        # 가장 가까운 물고기 찾기
        temp.sort(key=lambda x: (x[2], x[0], x[1]))
        target_x, target_y, dist = temp[0]

        # 물고기 먹기
        map[target_x][target_y] = 0
        shark_eaten += 1
        if shark_eaten == baby_shark:
            baby_shark += 1
            shark_eaten = 0

        now_x, now_y = target_x, target_y
        return dist  # 이동한 거리 반환

    return 0  # 더 이상 먹을 물고기가 없을 때

total_time = 0

while True:
    time = bfs()
    if time == 0:
        break
    total_time += time

print(total_time)