n, m = map(int, input().split())

A = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(sum(C) + 1)] for _ in range(n + 1)]
result = sum(C)

for i in range(1, n+1):
    ci, Ai = C[i], A[i]
    for j in range(sum(C) + 1):
        dp[i][j] = dp[i-1][j]
    for j in range(ci, sum(C) + 1):
        dp[i][j] = max(dp[i-1][j-ci] + Ai, dp[i][j])
        if dp[i][j] >= m:
            result = min(result, j)

print(result)