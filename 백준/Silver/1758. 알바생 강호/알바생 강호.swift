var visitor: [Int] = []

for _ in 0..<Int(readLine()!)! {
    visitor.append(Int(readLine()!)!)
}

visitor.sort(by: >)

var result = 0

for i in 0..<visitor.count {
    let money = visitor[i] - ((i + 1) - 1)
    if 0 < money { result += money }
}

print(result)
