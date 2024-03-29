"""
https://school.programmers.co.kr/learn/courses/30/lessons/43162
Level3
"""
"""
1. 방문했는지 기록을 위한 배열 만들어두기
2. 각 컴퓨터로 돌기
    False일 경우 count++
    DFS로 들어가서 연결된 부분 방문 처리 해주기
    전부 돌면 종료
3. DFS부분 방문 True로 바꿔주기
4. 각 컴퓨터 개수로 연결 되어 있는지 확인(DFS 반복문 부분)
    i와 visit이 같으면 같은 컴퓨터 패스
    방문 안했던 곳인지
    컴퓨터 연결 되어 있는지 computers 배열 확인
5. 다 돌고 answer 리턴
"""

def solution(n, computers):
    answer = 0
    # 1
    visited = [False for i in range(n)]
    # 2
    for visit in range(n):
        if visited[visit] == False:
            DFS(n, computers, visit, visited)
            answer += 1
    # 5
    return answer


def DFS(n, computers, visit, visited):
    # 3
    visited[visit] = True
    # 4
    for i in range(n):
        if i != visit and visited[i] == False and computers[i][visit]:
            DFS(n, computers, i, visited)

"""

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(land):
    answer = 0
    visited = [[False for i in range(len(land[0]))] for j in range(len(land))]
    result = [0] * len(land[0])
    print(visited)
    
    for i in range(len(land[0])):
        for j in range(len(land)):
            if land[j][i] == 1 and visited[j][i] == False:
                # print(i,j)
                # print(land[j][i])
                count = 0
                DFS(i, j, land, visited, count)
                print("hello, ", count)
    return answer

def DFS(x, y, land, visited, count):
    # print(x,y)
    count += 1
    print(count)
    visited[y][x] = True
    # print(visited)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= len(land[0]) or ny < 0 or ny >= len(land) :
            continue
        if land[ny][nx] == 1 and visited[ny][nx] == False:
            print("--------------------")
            print(nx,ny)
            DFS(nx, ny, land, visited, count)
    
    """