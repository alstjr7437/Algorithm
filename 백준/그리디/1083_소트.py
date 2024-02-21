"""
https://www.acmicpc.net/problem/1083
바로 뒤에 부분만 확인하고 교체하면 되는 형식인줄 알았음

하지만 사전순으로 정렬이 되는 것이면 뒤에 있는 수중 가장 큰수와 비교해서
그 수가 들어가야 하는 것을 다른 부분을 참고하고 깨달음
"""

n = int(input())
a = list(map(int, input().split()))
s = int(input())

i = 0

while 0 < s and i < n-1:
    id = a.index(max(a[i:i+s+1]))
    print(i, s, id)
    if id != i:
        a[id], a[id-1] = a[id-1], a[id]
        s -= 1
    else :
        i += 1

print(*a)
