import Foundation



func solution(_ k:Int, _ dungeons:[[Int]]) -> Int {
    
    var result = 0
    var n = dungeons.count
    
    func dfs(_ visited: [Bool], index: Int, now: Int, nowK: Int) {
        if visited.contains(false) { 
            for i in 0..<n {
                if i == index || visited[i] { continue }
                
                var nowVisited = visited
                nowVisited[i] = true
                if nowK >= dungeons[i][0] && nowK >= dungeons[i][1] {
                    dfs(nowVisited, index: i, now: now + 1, nowK: nowK - dungeons[i][1])
                } else {
                    dfs(nowVisited, index: i, now: now, nowK: nowK)
                }
            }
        } else {
            result = max(result, now)
        }
    }
    
    for i in 0..<n {
        var visited = Array(repeating: false, count: n)
        visited[i] = true
        if k >= dungeons[i][0] && k >= dungeons[i][1] {
            dfs(visited, index: i, now: 1, nowK: k - dungeons[i][1])
        } else {
            dfs(visited, index: i, now: 0, nowK: k)
        }
    }
    
    return result
}