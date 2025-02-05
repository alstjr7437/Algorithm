let input = readLine()!.split(separator: " ").map{Int($0)!}
let N = input[0]
let M = input[1]

var result: [Int] = []

func dfs(_ now: Int){
    if result.count == M {
        print(result.map{ String($0) }.joined(separator: " "))
        return
    }
    for i in now...N {
        result.append(i)
        dfs(i)
        _ = result.popLast()!
    }
}

dfs(1)