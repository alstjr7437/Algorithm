"""
https://www.acmicpc.net/problem/2630
"""
N = int(input())
paper = []
result = [0, 0]
def solution(x,y,n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                solution(x,y,n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2,y,n//2)
                solution(x+n//2,y+n//2,n//2)
                return 0
    if color == 0:
        result[0] += 1
    else :
        result[1] += 1

for i in range(N):
    paper.append(list(map(int, input().split())))

solution(0,0,N)
print(result[0])
print(result[1])

