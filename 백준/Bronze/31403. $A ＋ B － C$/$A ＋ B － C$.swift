var input: [Int] = []

for _ in 0..<3 {
    input.append(Int(readLine()!)!)
}

print(input[0] + input[1] - input[2])
print(Int("\(input[0])\(input[1])")! - input[2])
