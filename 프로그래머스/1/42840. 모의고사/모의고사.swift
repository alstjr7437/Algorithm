import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let one = [1,2,3,4,5]
    let two = [2,1,2,3,2,4,2,5]
    let three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    var result: [Int] = [0, 0, 0]
    
    for i in 0..<answers.count {
        if one[i%one.count] == answers[i] { result[0] += 1}
        if two[i%two.count] == answers[i] { result[1] += 1}
        if three[i%three.count] == answers[i] { result[2] += 1}
    }
    
    var result_human: [Int] = []
    
    var highScore = result.max()
    
    for i in 0..<3 {
        if highScore == result[i] { result_human.append(i+1) }
    }
    
    return result_human
}