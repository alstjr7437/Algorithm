"""
https://www.acmicpc.net/problem/11478
"""

s = input()
hello = []
a = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        # if s[i:j+1] not in hello:
        #     hello.append(s[i:j+1])
        a.add(s[i:j+1]) # i번째 문자부터 부분문자열 구하기

print(len(a))
