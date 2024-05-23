import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
unique = [list(map(int, input().split())) for _ in range(N+M)]
game = [i for i in range(1,101)]
visited = [0 for _ in range(100)]
q = deque()

q.append((1,0))
visited[0] = 1

while q:
    cur, dice = q.popleft()
    if cur == 100:
        print(dice)
        break
    for i in range(1, 7):
        check = 0
        
        if cur + i > 100: continue

        # 사다리 또는 뱀 검사
        for start, end in unique:
            if cur + i == start:
                if visited[end-1] == 0:
                    q.append((end, dice+1))
                    visited[end-1] = 1
                check = 1
                break

        if check: continue

        # 그 외 
        if visited[cur + i-1] == 0:
            q.append((cur + i, dice + 1))
            visited[cur + i-1] = 1