let T = Int(readLine()!)!

for _ in 0..<T {
    let NM = readLine()!.split(separator: " ").map { Int($0)! }
    let A = readLine()!.split(separator: " ").map { Int($0)! }
    let B = readLine()!.split(separator: " ").map { Int($0)! }
    let a = A.sorted()
    let b = B.sorted()
    
    var point = 0
    var result = 0
    for i in a {
        result += point
        for j in point..<b.count {
            if i > b[j] {
                point = j + 1
                result += 1
            }
        }
    }
    print(result)
}
