"""
연속합
https://www.acmicpc.net/problem/1912

처음에 이중 반복문으로 시간 초과 발생
"""

n = int(input())
a = list(map(int, input().split()))


for i in range(1,n):
    a[i] = max(a[i], a[i] + a[i-1])

print(max(a))


# result = []
# for i in range(n):
#     current = []
#     v = 0
#     for j in range(i, n):
#         v += a[j]
#         current.append(v) 
#     result.append(max(current))

# print(max(result))