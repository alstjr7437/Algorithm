// https://level.goorm.io/exam/171192/%EC%A0%88%EC%95%BD/quiz/1

let N = Int(readLine()!)!

var total_money = 0
var result = true

for _ in 0..<N {
	let temp = readLine()!.split(separator: " ")
	let money = Int(temp[1])!
	
	if temp[0] == "in" {
		total_money += money	
	} else {
		if total_money < money {
			result = false
			break
		} else {
			total_money -= money
		}
	}
}

if result {
	print("success")
} else {
	print("fail")
}