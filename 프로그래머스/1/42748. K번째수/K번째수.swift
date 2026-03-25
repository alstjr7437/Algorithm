import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var result: [Int] = []
    for command in commands {
    var currentArray: [Int] = []
        for i in command[0]-1...command[1]-1 {
            currentArray.append(array[i])
        }
        let sortedArray = currentArray.sorted()
        result.append(sortedArray[command[2]-1])
    }
    
    return result
}