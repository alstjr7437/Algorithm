# 폰켓몬 
# 해시
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    dict = {}
    for i in nums:
        dict[i] = 1
    if len(nums) / 2 <= len(dict):
        result = len(nums) / 2
    else : 
        result = len(dict)
    return result

# 다른 사람의 코드 ㄷㄷ
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
