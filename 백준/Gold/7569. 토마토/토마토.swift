import Foundation

let MNH: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
let M = MNH[0]
let N = MNH[1]
let H = MNH[2]

let dx: [Int] = [0, 0, -1, 1, 0, 0]
let dy: [Int] = [1, -1, 0, 0, 0, 0]
let dz: [Int] = [0, 0, 0, 0, 1, -1]

var queue: [(Int, Int, Int)] = []

var map: [[[Int]]] = Array(repeating: [], count: H)
var visit: [[[Bool]]] = Array(repeating: Array(repeating: Array(repeating: false, count: M), count: N), count: H)

for i in 0..<H {
    for _ in 0..<N {
        let input: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
        map[i].append(input)
    }
}

for i in 0..<H {
    for j in 0..<N {
        for k in 0..<M {
            if map[i][j][k] == 1 {
                queue.append((k, j, i))
            }
        }
    }
}

var index = 0

while index < queue.count {
    let current = queue[index]
    visit[current.2][current.1][current.0] = true
    index += 1
    
    for i in 0..<6 {
        let nx = current.0 + dx[i]
        let ny = current.1 + dy[i]
        let nz = current.2 + dz[i]
        
        if nx < 0 || nx >= M || ny < 0 || ny >= N || nz < 0 || nz >= H || visit[nz][ny][nx] { continue }
        
        if map[nz][ny][nx] == 0 {
            queue.append((nx, ny, nz))
            map[nz][ny][nx] = map[current.2][current.1][current.0] + 1
        }
    }
}

var result = 1

for z in 0..<H {
    for y in 0..<N {
        for x in 0..<M {
            if map[z][y][x] == 0 {
                print(-1)
                exit(0)
            } else {
                result = max(result, map[z][y][x])
            }
        }
    }
}
print(result - 1)
