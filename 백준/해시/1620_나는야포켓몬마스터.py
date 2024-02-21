"""
나는야 포켓몬 마스터 
해시
https://www.acmicpc.net/problem/1620
"""
import sys
n,m = map(int, sys.stdin.readline().split())
pokemon = {}
for i in range(1,n+1):
    name = sys.stdin.readline().strip()
    pokemon[name] = i
    pokemon[str(i)] = name

for i in range (0,m) :
    question = sys.stdin.readline().strip()
    print(pokemon[question])


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

