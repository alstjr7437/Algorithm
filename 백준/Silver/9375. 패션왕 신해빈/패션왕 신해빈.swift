for _ in 0..<Int(readLine()!)! {
    var clothes: [String: [String]] = [:]
    for _ in 0..<Int(readLine()!)! {
        let input = readLine()!.split(separator: " ").map { String($0) }
        let clothName = input[0]
        let kind =  input[1]
        if clothes[kind] == nil {
            clothes[kind] = [clothName]
        } else {
            clothes[kind]!.append(clothName)
        }
    }
    var result = 1
    for cloth in clothes.values {
        result *= cloth.count + 1
    }
    print(result - 1)
}