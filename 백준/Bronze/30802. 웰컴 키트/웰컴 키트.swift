import Foundation

let n = Int(readLine()!)!
let people = readLine()!.split(separator: " ").map { Int($0)! }
let tp = readLine()!.split(separator: " ").map { Int($0)! }
let T = tp[0]
let P = tp[1]
var result = 0

for person in people {
    if person % T == 0 {
        result += person / T
    } else {
        result += person / T + 1
    }
}

print(result)
print("\(n / P) \(n % P)")