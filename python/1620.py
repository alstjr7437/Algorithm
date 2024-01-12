# 나는야 포켓몬 마스터 
# 해시
# https://www.acmicpc.net/problem/1620
import sys
n, m = map(int, input().split())

dict_int = {}
dict_name = {}

for i in range(1, n+1):
    pocket = sys.stdin.readline().strip()
    dict_int[i] = pocket
    dict_name[pocket] = i

for i in range(m):
    result = sys.stdin.readline().strip()
    if result.isnumeric():
        print(dict_int[int(result)])
    else : 
        print(dict_name[result])


"""
# list로 코드 구현시 시간 초과 에러 발생
result = []
for i in range(n):
    result.append(sys.stdin.readline().rstrip())

for i in range(m):
    b = sys.stdin.readline().rstrip()
    if b.isnumeric() :
        print(result[i])
    else :
        print(result.index(b)+1)
"""

