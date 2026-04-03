let MN = readLine()!.split(separator: " ").map { Int(String($0))! }

var map: [[Int]] = []
var dx = [0,0,-1,1]
var dy = [1,-1,0,0]

for _ in 0..<MN[1] {
    map.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

var visited = Array(repeating: Array(repeating: -1, count: MN[0]), count: MN[1])

var queue: [(Int, Int)] = []
var index = 0

for i in 0..<MN[1] {
    for j in 0..<MN[0] {
        if map[i][j] == 1 {
            queue.append((i, j))
            visited[i][j] = 0
        } else if map[i][j] == -1 {
            visited[i][j] = 0
        }
    }
}

while index < queue.count {
    let (y, x) = queue[index]
    index += 1
    
    for i in 0..<4 {
        let nx = x + dx[i]
        let ny = y + dy[i]
        
        if nx < 0 || nx >= MN[0] || ny < 0 || ny >= MN[1] || visited[ny][nx] != -1 { continue }
        
        visited[ny][nx] = visited[y][x] + 1
        
        if map[ny][nx] == 0 {
            queue.append((ny, nx))
        }
    }
}

if visited.map({ $0.contains(-1) }).contains(true) {
    print(-1)
} else {
    print(visited.map { $0.max()! }.max()!)
}
