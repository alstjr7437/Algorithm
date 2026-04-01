import Foundation

func solution(_ begin:String, _ target:String, _ words:[String]) -> Int {
    var visited = Array(repeating: false, count: words.count)
    var queue: [(String, Int)] = [(begin, 0)]
    var index = 0
    
    while index < queue.count {
        var (current, depth) = queue[index]
        index += 1
        
        if current == target { return depth }
        for i in 0..<words.count {
            if visited[i] { continue }
                
            if vaild(current, words[i]) {
                visited[i] = true
                queue.append((words[i], depth + 1))
            }
        }
    }
    
    return 0    
}

func vaild(_ a: String, _ b: String) -> Bool {
    let aArray = Array(a)
    let bArray = Array(b)

    var diff = 0
    for i in 0..<aArray.count {
        if aArray[i] != bArray[i] { diff += 1 }
    }

    return diff == 1
}