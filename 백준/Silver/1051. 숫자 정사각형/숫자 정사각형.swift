let NM = readLine()!.split(separator: " ").map{ Int(String($0))! }
let N = NM[0]
let M = NM[1]
var board: [[Int]] = []
var result = 1

for _ in 0..<N {
    board.append(readLine()!.map { Int(String($0))!} )
}

for size in 0..<min(N, M){
    for i in 0..<N {
        for j in 0..<M {
            if i + size >= N || j + size >= M { continue }
            let a = board[i][j]
            let b = board[i][j+size]
            let c = board[i+size][j]
            let d = board[i+size][j+size]
            if a == b && a == c && a == d {
                let resultSize = size + 1
                result = resultSize * resultSize
            }
        }
    }
}

print(result)

