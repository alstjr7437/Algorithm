def solution(name):
    answer = 0
    
    n = len(name)
    
    for i in name:
        answer += min(ord(i) - 65, 91 - ord(i))

    move = n - 1
    for i in range(n):
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
        move = min(move,
                   2 * i + (n - next),  
                   i + 2 * (n - next))
    answer += move

    
    return answer