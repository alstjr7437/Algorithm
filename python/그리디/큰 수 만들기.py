"""
큰 수 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/42883
"""

def solution(number, k):
    result = []
    for i in number:
        while result and result[-1] < i and k > 0:
            result.pop()
            k -= 1
        result.append(i)
        
    return ''.join(result[:len(number)-k])