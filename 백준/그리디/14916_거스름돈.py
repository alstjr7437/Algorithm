"""
https://www.acmicpc.net/problem/14916

그리디와 DP 두가지 풀이 가능
"""

# n = int(input())
# money = [5, 2]
# count = 0

# while n > 0:
#     if n % 5 == 0:
#         count += n // 5
#         break
#     n -= 2
#     count += 1

# if n < 0:
#     print(-1)
# else :
#     print(count)

n = int(input())
dp = [-1, -1, 1, -1, 2, 1, 3, 2, 4, 3]
for i in range(10,n+1):
    dp.append(dp[i-5]+1)

print(dp[n])