import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var dict: [String: Int] = [:]
    
    for cloth in clothes {
        dict[cloth[1], default: 0] += 1
    }
    
    var sum = 1 
    for value in dict.values {
        sum *= value + 1
    }
    
    return sum - 1
}