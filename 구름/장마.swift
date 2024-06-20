// https://level.goorm.io/exam/194982/%EC%9E%A5%EB%A7%88/quiz/1

let input = readLine()!.split(separator: " ").map{ Int(String($0))! }
let N = input[0]; let M = input[1]
var ground = readLine()!.split(separator: " ").map{ Int(String($0))! }

var drainage: Set<Int> = []

for i in 1...M{
	let temp = readLine()!.split(separator: " ").map{ Int(String($0))! }
	
	for j in temp[0] - 1..<temp[1]{
		ground[j] += 1
		drainage.insert(j)
	}
	
	if i % 3 == 0{
		for j in drainage{
			ground[j] -= 1 
		}
		drainage = []
	}
	
}

for i in ground{
	print(i, terminator: " ")
}