let N = readLine()!.split(separator: " ").map { Int(String($0))! }
let ant1 = readLine()!
let ant2 = readLine()!
let T = Int(readLine()!)!

let ant1Last = ant1.first!

var result = Array(ant1.reversed()) + Array(ant2)

for _ in 0..<T {
    for i in 0..<(result.count - 1) {
        if ant1.contains(result[i]) && ant2.contains(result[i + 1]) {
            result.swapAt(i, i+1)
            if result[i + 1] == ant1Last { break }
        }
   }
}

print(String(result))
