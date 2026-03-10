let n = Int(readLine()!)!

let list = readLine()!.split(separator: " ").map { Int(String($0))! }.sorted()

var resultSum = Int.max
var result: [Int] = []

var point1 = 0
var point2 = n - 1

while point1 < point2 {
    let current = list[point1] + list[point2]
    if resultSum > abs(current) {
        resultSum = abs(current)
        result = [list[point1], list[point2]]
    }
    if 0 < current {
        point2 -= 1
    } else {
        point1 += 1
    }
}

print(result.map { String($0) }.joined(separator: " "))
