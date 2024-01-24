"""
https://school.programmers.co.kr/learn/courses/30/lessons/250137
붕대 감기 level1
"""

def solution(bandage, health, attacks):
    answer = 0
    current_health = health
    cnt = 0
    attack_time = {}
    for i in range(len(attacks)):
        attack_time[attacks[i][0]] = attacks[i][1]
    
    for time in range(attacks[-1][0] + 1):
        if time in attack_time:
            current_health -= attack_time[time]
            cnt = 0
            if current_health <= 0:
                return -1
        
        elif current_health < health:
            current_health += bandage[1]
            cnt += 1
            if cnt == bandage[0]:
                current_health += bandage[2]
                cnt = 0
                
        if current_health > health :
            current_health = health
            
        print(time, current_health, cnt)

    return current_health