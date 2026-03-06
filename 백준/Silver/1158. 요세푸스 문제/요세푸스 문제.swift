let input = readLine()!.split(separator: " ").map { Int(String($0))! }

var n = Array(1...input[0])
var result: [Int] = []
var index: Int = 0

while !n.isEmpty {
    index = (index + input[1] - 1) % n.count
    result.append(n.remove(at: index))
}

print("<\(result.map{ String($0) }.joined(separator: ", "))>")
