let T = Int(readLine()!)!

for _ in 0..<T {
    let NM = readLine()!.split(separator: " ").map { Int($0)! }
    var A = readLine()!.split(separator: " ").map { Int($0)! }
    A.sort()
    var B = readLine()!.split(separator: " ").map { Int($0)! }
    B.sort()
    
    var point = 0
    var result = 0
    for i in A {
        result += point
        for j in point..<B.count {
            if i > B[j] {
                point = j + 1
                result += 1
            }
        }
    }
    print(result)
}
