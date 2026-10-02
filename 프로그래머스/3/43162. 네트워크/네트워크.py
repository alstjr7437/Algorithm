from collections import deque

def solution(n, computers):
    answer = 0
    
    
    visited = [[False for _ in range(len(computers[0]))] for _ in range(len(computers))]
    
    for i in range(len(computers)):
        if visited[i][i] == True:
            continue
        queue = deque([i])
        while len(queue) > 0:
            current = queue.popleft()
            for j in range(len(computers[current])):
                if current != j and computers[current][j] == 1 and visited[current][j] == False:
                    queue.append(j)
                visited[current][j] = True
        answer += 1
    return answer