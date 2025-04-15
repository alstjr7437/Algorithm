let NM = readLine()!.split(separator: " ").map{ Int(String($0))! }
let N = NM[0]
let M = NM[1]
let H = readLine()!.split(separator: " ").map { Int(String($0))! }
var cows = Set<Int>()

let maxValue = H.reduce(0, +) + 1
var sosu = Array(repeating: true, count: maxValue)
sosu[0] = false
sosu[1] = false

for i in 2..<maxValue {
    if sosu[i] {
        var j = 2
        while i * j < maxValue {
            sosu[i * j] = false
            j += 1
        }
    }
}

func dfs(_ idx: Int, _ count: Int, _ total: Int) {
    if count == M {
        cows.insert(total)
        return
    }
    if idx == N { return }

    dfs(idx + 1, count + 1, total + H[idx])
    dfs(idx + 1, count, total)
}

dfs(0, 0, 0)

var result: [Int] = []
for cow in cows {
    if cow < maxValue && sosu[cow] {
        result.append(cow)
    }
}

if result.isEmpty {
    print(-1)
} else {
    print(result.sorted().map { String($0) }.joined(separator: " "))
}