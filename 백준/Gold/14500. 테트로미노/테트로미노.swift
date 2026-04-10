let shapes: [[(Int, Int)]] = [

    // I
    [(0,1),(0,2),(0,3)],
    [(1,0),(2,0),(3,0)],

    // O
    [(0,1),(1,0),(1,1)],

    // L
    [(1,0),(2,0),(2,1)],
    [(1,0),(2,0),(2,-1)],
    [(0,1),(0,2),(1,0)],
    [(0,1),(0,2),(-1,0)],

    // J
    [(1,0),(2,0),(0,1)],
    [(1,0),(2,0),(0,-1)],
    [(0,1),(0,2),(1,2)],
    [(0,1),(0,2),(-1,2)],

    // S
    [(0,1),(1,1),(1,2)],
    [(1,0),(1,-1),(2,-1)],

    // Z
    [(0,1),(-1,1),(-1,2)],
    [(1,0),(1,1),(2,1)],

    // T
    [(0,-1),(0,1),(1,0)],
    [(0,-1),(0,1),(-1,0)],
    [(-1,0),(1,0),(0,1)],
    [(-1,0),(1,0),(0,-1)]
]

let NM = readLine()!.split(separator: " ").map { Int(String($0))! }

var map: [[Int]] = []

for _ in 0..<NM[0] {
    map.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

var result = 0

for i in 0..<NM[0] {
    for j in 0..<NM[1] {
        for shape in shapes {
            var current = map[i][j]
            var isValid = true
            
            for (dx, dy) in shape {
                let ni = i + dx
                let nj = j + dy
                
                if ni < 0 || nj < 0 || ni >= NM[0] || nj >= NM[1] {
                    isValid = false
                    break
                }
                
                current += map[ni][nj]
            }
            
            if isValid {
                result = max(result, current)
            }
        }
    }
}

print(result)
