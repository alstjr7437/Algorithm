import Foundation

let T = Int(readLine()!)!

for _ in 0..<T {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    
    let base = input[0]
    let exponent = input[1]
    var result = 1
    for _ in 0..<exponent {
        result = (result * base) % 10
    }
    
    if result == 0 {
        print(10)
    } else {
        print(result)
    }
}
