let n = Int(readLine()!)!

let list = readLine()!.split(separator: " ").map { Int(String($0))! }.sorted()

let x = Int(readLine()!)!

var result = 0

var point1 = 0
var point2 = n - 1

while point1 != point2 {
    let current = list[point1] + list[point2]
    
    if current > x {
        point2 -= 1
    } else if current < x {
        point1 += 1
    } else if current == x {
        result += 1
        point1 += 1
    }
}

print(result)
