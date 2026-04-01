import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    func dfs(_ count: Int, _ index: Int, _ array: [Int]) {
        if visited[index] != 0 { return }
        
        visited[index] = count
        
        for i in 0..<array.count {
            if array[i] == 1 && index != i {
                dfs(count, i, computers[i])
            }
        }
    }
    var visited = Array(repeating: 0, count: n)
    var result = 1
    for i in 0..<n {
        if visited[i] == 0 {
            dfs(result, i, computers[i])
            result += 1
        }
    }
    
    return result - 1
}