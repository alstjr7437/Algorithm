import Foundation

let N = readLine()!.split(separator: " ").map { Int(String($0))! }

let N1 = readLine()!
let N2 = readLine()!

let T = Int(readLine()!)!
let ant1Last = N1.first!

var result = Array(N1.reversed()) + Array(N2)

for _ in 0..<T {
    for j in 0..<(result.count - 1) {
        if N1.contains(result[j]) && N2.contains(result[j + 1]) {
            result.swapAt(j, j+1)
            if result[j + 1] == ant1Last {
                break
            }
        }
   }
}

print(String(result))