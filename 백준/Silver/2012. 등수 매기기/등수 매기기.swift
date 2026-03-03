let N = Int(readLine()!)!

var people: [Int] = []

var result = 0

for _ in 0..<N {
    people.append(Int(readLine()!)!)
}

people = people.sorted(by: <)

for i in 0..<N {
    if people[i]-1 != i {
        result += abs(people[i]-1 - i)
        
    }
}

print(result)
