let n = Int(readLine()!)!
let m = Int(readLine()!)!

let s = readLine()!.map{$0}

var result = 0
var cur = 0
var count = 0

while cur < m-2{
    if String(s[cur...cur + 2]) == "IOI"{
        count += 1
        cur += 2
        if count == n{
            result += 1
            count -= 1
        }
    } else {
        count = 0
        cur += 1
    }
}

print(result)