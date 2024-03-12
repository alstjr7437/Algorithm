t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    dp = [[0] * m for _ in range(n)]

    for j in range(n):
        for z in range(j, m):
            if j == 0:
                dp[j][z] = z + 1
            else :
                dp[j][z] = dp[j-1][z-1] + dp[j][z-1]

    print(dp[n-1][m-1])