import Foundation

func solution(_ numbers:String) -> Int {
    let numbers = numbers.map { String($0) }
    
    func dfs(_ current: String) {
        if !current.isEmpty { numberSet.insert(Int(current)!) }
        
        for i in 0..<numbers.count {
            if visited[i] { continue }
            
            visited[i] = true
            
            dfs(current + numbers[i])
            visited[i] = false
        }
    }
    
    func isPrimeNumber(n: Int) -> Bool {
        if n < 2 {
            return false
        }
        for i in 2..<n {
            if n % i == 0 { return false }
        }
        return true
    }
    
    var numberSet = Set<Int>()
    var visited = Array(repeating: false, count: numbers.count)
    dfs("")
    
    var result = 0
    for number in numberSet {
        if isPrimeNumber(n: number) { result += 1 }
    }
    
    return result
}