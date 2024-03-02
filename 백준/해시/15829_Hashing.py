"""
https://www.acmicpc.net/problem/15829
"""
l = int(input())
alpha = input()
answer = 0
for i in range (l):
    answer += (ord(alpha[i]) - 96) * (31 ** i)
print(answer % 1234567891)