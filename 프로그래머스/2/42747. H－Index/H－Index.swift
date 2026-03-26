import Foundation

func solution(_ citations:[Int]) -> Int {
    let array = citations.sorted(by: >)
    
    for i in 0..<citations.count {
        print(i, array[i])
        if i >= array[i] {
            return i
            break
        }
    }
    
    return array.count
}