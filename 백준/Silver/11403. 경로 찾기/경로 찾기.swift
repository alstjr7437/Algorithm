let N = Int(readLine()!)!

var map: [[Int]] = []
for _ in 0..<N {
    map.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

var visited = Array(repeating: Array(repeating: 0, count: N), count: N)

func bfs(start: Int) {
    var queue: [Int] = []
    queue.append(start)
    var index = 0
    var check = Array(repeating: 0, count: N)
    
    while index < queue.count {
        let current = queue[index]
        index += 1
        
        for i in 0..<N {
            if map[current][i] == 1 && check[i] == 0 {
                queue.append(i)
                check[i] = 1
                visited[start][i] = 1
            }
        }
    }
}

for i in 0..<N {
    bfs(start: i)
}

for visit in visited {
    print(visit.map { String($0) }.joined(separator: " "))
}
