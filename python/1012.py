"""
틀린 부분
문제와 똑같이 x,y를 설정하려고 노력했는데
N과 M만 초기에 두개를 바꿔주면 따로 3*5가 아닌 5*3이 되지만
정답은 문제 없이 잘돌아가므로 맞게 된다.

하지만 따로 x,y의 그림 3*5의 그림까지 구현을 하고 싶어서
m과 n은 그대로 진행하고 baechu라는 배열에 넣는 부분의 x,y를 바꿔줬다.

문제점
따로 오래만에 BFS문제를 풀어서 어떻게 했는지 햇갈렸다..
dx,dy의 개념이 아직 완전히 확립이 되지 않아 코딩테스트에 많이 보이는 좌표 문제를
진행하려면 따로 dx,dy도 완벽히 숙지를 해야할 것 같다.
"""

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    start = [(x,y)]
    baechu[y][x] = 0
    while start:
        x,y = start.pop(0)
        baechu[y][x] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n :
                continue
            if baechu[ny][nx] == 1:
                start.append((nx,ny))
                baechu[ny][nx] = 0 


a = int(input())

for _ in range(a):
    m,n,k = map(int, input().split())
    count = 0  
    baechu = [[0] * m for _ in range (n)]

    for _ in range(k):
        x, y = map(int,input().split())
        baechu[y][x] = 1

    for i in range(m):
        for j in range(n):
            if baechu[j][i] == 1:
                BFS(i,j)
                count += 1
    print(count)
