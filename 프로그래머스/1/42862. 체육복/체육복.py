def solution(n, lost, reserve):
    answer = 0
    
    current = 0
    list = [0] + [1] * n + [0] 
    
    for i in lost: list[i] -= 1
    for i in reserve: list[i] += 1
    
    print(list)
    for i in range(1, n+1):
        if list[i] == 1 or list[i] == 2:
            answer += 1
        elif list[i] == 0:
            if list[i-1] == 2:
                answer += 1
                list[i-1] = 1
            elif list[i+1] == 2:
                answer += 1
                list[i+1] = 1
        print(i, answer)
        
    return answer