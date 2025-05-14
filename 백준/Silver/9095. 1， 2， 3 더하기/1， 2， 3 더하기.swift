for _ in 0..<Int(readLine()!)! {
    let N = Int(readLine()!)!
    var dp = Array(repeating: 0, count: N + 1)
    dp[0] = 1
    for i in 1..<N + 1{
        if i >= 1 {
            dp[i] += dp[i - 1]
        }
        if i >= 2 {
            dp[i] += dp[i - 2]
        }
        if i >= 3 {
            dp[i] += dp[i - 3]
        }
    }
    print(dp[N])
}
