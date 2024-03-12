def solution(gems):
    N = len(gems)
    answer = [0, N-1]
    kind = len(set(gems))  
    dict = {gems[0]:1,}  
    head,tail = 0,0  
    while head<N and tail<N:
        # print(head,tail, dict)
        # 종류 부족하면
        if len(dict) < kind:  
            tail += 1
            if tail == N:
                break
            dict[gems[tail]] = dict.get(gems[tail], 0) + 1
        
        # 종류 같으면
        else:  
            if (tail-head+1) < (answer[1]-answer[0]+1):
                print("Hello")
                answer = [head,tail]
            if dict[gems[head]] == 1:
                del dict[gems[head]]
            else:
                dict[gems[head]] -= 1
            head += 1

    answer[0] += 1
    answer[1] += 1
    
    return answer