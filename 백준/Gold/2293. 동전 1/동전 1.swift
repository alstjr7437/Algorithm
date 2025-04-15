let input0 = readLine()!.split(separator: " ").map { Int(String($0)) }
let n = input0[0]!
let k = input0[1]!

var coin: [Int] = []
for _ in 0..<n {
    coin.append(Int(readLine()!)!)
}

var dp = Array(repeating: 0, count: k + 1)
dp[0] = 1

for i in coin {
    if k >= i {
        for j in i..<k+1 {
            dp[j] += dp[j - i]
            if dp[j] >= 2_147_483_648 {
                dp[j] = 0
            }
        }
    }
}

print(dp[k])
