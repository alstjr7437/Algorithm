import math

def solution(progresses, speeds):
    answer = []
    temp = []
    for i in range(len(progresses)):
        temp.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    print(temp)
    current = 0
    for i in range(1, max(temp) + 1):
        count = 0
        print(temp[current], i)
        while temp[current] < i :
            count += 1
            current += 1
            print("test")
        if count > 0 :
            answer.append(count)
    
    answer.append(len(progresses) - sum(answer))
    return answer