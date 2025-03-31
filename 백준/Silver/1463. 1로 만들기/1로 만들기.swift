import Foundation

let input = Int(readLine()!)!

var result = Array(repeating: 0, count: input + 1)

for i in 1...input {
    result[i] = result[i - 1] + 1
    if i % 3 == 0 {
        result[i] = min(result[i], result[i / 3] + 1)
    }
    if i % 2 == 0 {
        result[i] = min(result[i], result[i / 2] + 1)
    }
}
print(result[input] - 1)
