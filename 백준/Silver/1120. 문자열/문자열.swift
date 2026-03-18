let input = readLine()!.split(separator: " ").map { String($0) }
var A = input[0].map { String($0) }
var B = input[1].map { String($0) }

var result: [Int] = []


for i in 0..<B.count - A.count + 1 {
    var count = 0
    for j in 0..<A.count {
        if A[j] != B[i+j] {
            count += 1
        }
    }
    result.append(count)
}

print(result.min() ?? 0)
