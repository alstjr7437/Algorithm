"""
https://school.programmers.co.kr/learn/courses/30/lessons/148653
마법의 엘리베이터 Lv2
핵심 10의 나머지에 따른 처리 다르게 하기
1. 4 이하일때 : 그냥 answer에 나머지만큼 더해주기
2. 6 이상일때 : answer에 10을 뺀 나머지 만큼 더해주고 10이 올라갔으니 storey + 10
3. 5 일때 : 그 뒤에 부분의 숫자에 따른 1,2번 처리 똑같이 해주기
"""

def solution(storey):
    answer = 0
    
    while storey > 0:
        current = storey % 10
        if current < 5:
            answer += current
        elif current > 5:
            answer += 10 - current
            storey += 10
        else:
            if (storey//10) % 10 >= 5 :
                storey += 10
            answer += 5
        storey //= 10
        print(f"남은수 : {storey}, 나머지 수 : {current}, 현재 누른 돌 : {answer}")
        
    return answer