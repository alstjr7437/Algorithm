'''
https://school.programmers.co.kr/learn/courses/30/lessons/42898#
DP 문제 
문제 잘읽기 : 1,000,000,007로 나눈 나머지 리턴 하는거!
'''

def solution(m, n, puddles):
    answer = 0
    road = [[0] * m for i in range(n)]
    road[0][0] = 1
    for i in puddles:
        a,b = i
        road[a-1][b-1] = -1
    
    print(road)
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0 : 
                continue
            if road[i][j] == -1:
                continue
            elif road[i][j-1] == -1:
                road[i][j] = road[i-1][j]
            elif road[i-1][j] == -1:
                road[i][j] = road[i][j-1]
            else :
                road[i][j] = road[i][j-1] + road[i-1][j] 
    print(road)
    return road[n-1][m-1] %1000000007

print(solution(4,3, [[2,2]]))