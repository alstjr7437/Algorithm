"""
https://www.acmicpc.net/problem/11727

풀이
https://github.com/AlgoLeadMe/AlgoLeadMe-4/pull/62
"""

dp = [0] * 1002
n = int(input())
dp[1] = 1
for i in range(2, 1002):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007


print(dp[n+1])