//하얀칸 검은칸 번갈아가면서
//하얀 검은
//검은 하얀

var result = 0

for i in 0..<8 {
    let input = readLine()!.map { String($0) }

    for j in 0..<8 {
        if input[j] == "F" && j % 2 == 0 && i % 2 == 0 {
            result += 1
        } else if input[j] == "F" && j % 2 != 0 && i % 2 != 0 {
            result += 1
        }
    }
}

print(result)
