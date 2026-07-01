import Foundation

func solution(_ common:[Int]) -> Int {
    let last = common[common.count - 1]
    let diff = common[1] - common[0]
    
    if common[2] - common[1] == diff {
        return last + diff
    } else {
        return last * (common[1] / common[0])
    }
}

// 1 -> 2 -> 3 -> 4
// 2 -> 4 -> 8
// 1 -> 1 -> 1