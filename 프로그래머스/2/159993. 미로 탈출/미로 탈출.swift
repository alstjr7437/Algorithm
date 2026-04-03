import Foundation

func solution(_ maps:[String]) -> Int {
    
    var width = maps[0].count
    var height = maps.count
    
    var stringMap = maps.map { Array($0.map { String($0) }) }
    
    var dx = [0, 0, -1, 1]
    var dy = [1, -1, 0, 0]
    
    var result1 = 0
    var result2 = 0
    
    func bfs(start: (Int, Int), target: String) -> Int {
        var visited = Array(repeating: Array(repeating: -1, count: width), count: height)
        var queue: [(Int, Int)] = [start]
        var index = 0
        visited[start.0][start.1] = 0
    
        while index < queue.count {
            let (x, y) = queue[index]
            index += 1

            for i in 0..<4 {
                let nx = x + dx[i]
                let ny = y + dy[i]

                if nx >= height || nx < 0 || ny >= width || ny < 0 || visited[nx][ny] != -1 {
                    continue
                }

                let current = stringMap[nx][ny]

                visited[nx][ny] = visited[x][y] + 1

                if current != "X" {
                    queue.append((nx, ny))
                }

                if current == target {
                    return visited[nx][ny]
                }
            }
        }
        return -1
    }
    
    for (index, map) in maps.enumerated() {
        for (index2, string) in map.enumerated() {
            if string == "S" { 
                result1 = bfs(start: (index, index2), target: "L")
            } else if string == "L" {
                result2 = bfs(start: (index, index2), target: "E")
            }
        }
    }
    
    if result1 == -1 || result2 == -1 {
        return -1
    } else {
        print(result1, result2)
        return result1 + result2
    }
}