let N = Int(readLine()!)!
let input = readLine()!.split(separator: " ").map { Int(String($0))! }

var result = Array(repeating: 0, count: N)
var count = 0

for i in 0..<N {
    if input[i] != i+1 {
        result[i] = (input[i])
    } else {
        count += 1
        if input[i] >= N {
            result[i] = 1
        } else {
            result[i] = input[i] + 1
        }
    }
}

print(count)
print(result.map { String($0)}.joined(separator: " "))