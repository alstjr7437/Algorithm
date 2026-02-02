let T = Int(readLine()!)!

var dp = [1,1,1,2,2,3,4,5]

for i in 8...100 {
    dp.append(dp[i-5] + dp[i-1])
}

for _ in 0..<T {
    let input = Int(readLine()!)!
    
    print(dp[input-1])
}

