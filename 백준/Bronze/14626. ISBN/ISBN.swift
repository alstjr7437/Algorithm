let input = readLine()!.map { Int(String($0)) ?? nil }

var result = 0

var idx = 0

for i in 0..<input.count {
    if let value = input[i] {
        if i % 2 == 0 {
            result += value
        } else {
            result += value * 3
        }
    } else {
        idx = i
    }
}

let a = idx % 2 == 0 ? 1 : 3

for i in 0...9 {
    if (result + a * i) % 10 == 0 {
        print(i)
        break
    }
}
