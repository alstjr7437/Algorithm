"""

"""
"""
1. 정렬을 위해 set 이용
    lost = [2,4] reserve = [3,1] 이 있는데 정렬을 안하고 진행 시 3이 2를 빼버리고 1이 2로 되서 3개만 된다
        정렬을 하면 2, 4 / 1, 3으로 1이 2를 제거 3이 4를 제거 하게 된다.
2. 중복 부분 제거 
    -를 이용해서 빼주기 → 잃어버렸지만 여분이 있는 사람의 체육복을 위해
3. 제거~~
"""
def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    print(set_lost, set_reserve)
    
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i-1)
        elif i + 1 in set_lost :
            set_lost.remove(i+1)
    print(set_lost)
    
    return n - len(set_lost)