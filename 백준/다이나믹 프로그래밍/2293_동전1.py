n, k = map(int, input().split())

dp = [0] * (k + 1)
dp[0] = 1

coin = []
for i in range(n):
    coin.append(int(input()))

for i in coin:
    for j in range(i, k+1):
        dp[j] = dp[j] + dp[j-i]
        
print(dp[k])