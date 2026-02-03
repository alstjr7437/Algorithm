let n = Int(readLine()!)!

var dp = [Int](repeating: 0, count: n + 1)

dp[0] = 0

for i in 1...n {
    dp[i] = dp[i-1] + 1
    
    var j = 1
    while i - j * j >= 0 {
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1
    }
}

print(dp[n])