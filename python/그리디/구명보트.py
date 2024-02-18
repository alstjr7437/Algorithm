"""
https://school.programmers.co.kr/learn/courses/30/lessons/42885
2명씩 제한!

풀이 : https://github.com/AlgoLeadMe/AlgoLeadMe-6/pull/30
"""
def solution(people, limit):
    people.sort()
    start = 0
    end = len(people) -1
    answer = 0
    while(start<=end):             
        if(people[start]+people[end] <= limit): 
            start += 1   
        end-=1
        answer +=1
    return answer