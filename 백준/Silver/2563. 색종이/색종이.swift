var peper = Array(repeating: Array(repeating: false, count: 100), count: 100)
var result = 0

for _ in 0..<Int(readLine()!)! {
    let point = readLine()!.split(separator: " ").map { Int(String($0))! }
    
    for x in point[0]..<point[0] + 10 {
        for y in point[1]..<point[1] + 10 {
            if x <= 100 && y <= 100 && peper[y][x] != true{
                peper[y][x] = true
                result += 1
            }
        }
    }
}

print(result)