import Foundation

func solution(_ numbers:[Int]) -> String {
    var array = numbers.map { String($0) }
    
    array.sort(by: {
        return $0 + $1 > $1 + $0
    })
    
    return array[0] == "0" ? "0" : array.joined()
}