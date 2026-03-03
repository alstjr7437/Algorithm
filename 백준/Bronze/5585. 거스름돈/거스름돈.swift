let T = Int(readLine()!)!

let money = [500, 100, 50, 10, 5, 1]

var current = 1000 - T

var result = 0

for m in money {
    if current / m > 0 {
        let i = current/m
        current -= m * i
        result += i
    }
}

print(result)