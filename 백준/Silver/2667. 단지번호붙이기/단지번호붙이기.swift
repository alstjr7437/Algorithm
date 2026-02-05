let N = Int(readLine()!)!

var map: [[Int]] = []

for _ in 0..<N {
    let input = readLine()!.map { Int(String($0))! }
    map.append(input)
}


let dx: [Int] = [0, 0, 1, -1]
let dy: [Int] = [1, -1, 0, 0]

var result: [Int] = []

for y in 0..<N {
    for x in 0..<N {
        let current = map[y][x]
        
        if current == 0 { map[y][x] = 2 }
        if current == 1 {
            result.append(dfs(x: x, y: y, value: 0))
        }
    }
}

print(result.count)
result.sorted().forEach { print($0) }

func dfs(x: Int, y: Int, value: Int) -> Int {
    map[y][x] = 2;
    var result = value + 1
    
    for i in 0..<4 {
        let nx = x + dx[i]
        let ny = y + dy[i]
        
        if nx < 0 || nx >= N || ny < 0 || ny >= N { continue }
        
        if map[ny][nx] != 1 { continue }
        
        result += dfs(x: nx, y: ny, value: value)
    }
    
    return result
}
