"""
기능개발 - 큐 이용
1번. date변수를 통해 계속 비교
2번. 진행일을 미리 계산해두고 하기
https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""

def solution(progresses, speeds):
    answer = []
    date = 0
    cnt = 0
    
    while progresses:
        if (progresses[0] + date * speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            date += 1
    answer.append(cnt)
    return answer

# import math

# def solution(progresses, speeds):
#     answer = []
#     for i in range(len(progresses)):
#         answer.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
#     max = answer.pop(0)
#     cnt = 1
#     result = []
    
#     while answer :
#         now = answer.pop(0)
#         if max >= now:
#             cnt += 1
#             continue    
#         max = now
#         result.append(cnt)
#         cnt = 1
        
#     result.append(cnt)
    
#     return result