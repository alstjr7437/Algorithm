let N = Int(readLine()!)!
var schedule = [(0,0)]

for _ in 0..<N {
    let input = readLine()!.split(separator: " ").map{ Int($0)! }
    schedule.append((input[0], input[1]))
}

var dp = Array(repeating: 0, count: 21)

for i in 1..<N+1 {
    if dp[i] > dp[i+1] { dp[i+1] = dp[i] }
    
    guard i+schedule[i].0 <= N+1 else { continue }
    
    dp[i+schedule[i].0] = max(schedule[i].1 + dp[i], dp[i+schedule[i].0])
}

print(dp.max()!)
