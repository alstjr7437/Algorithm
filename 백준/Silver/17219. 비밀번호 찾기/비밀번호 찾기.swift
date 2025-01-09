import Foundation

let input = readLine()!.split(separator: " ").map{ Int($0)! }

var passwordList: [String: String] = [:]
var siteInput: [String] = []

for _ in 0..<input[0] {
    let inputData = readLine()!.split(separator: " ").map { String($0) }
    passwordList[inputData[0]] = inputData[1]
}

for _ in 0..<input[1] {
    let siteInput = readLine()!
    if let sitePassword = passwordList[siteInput] {
        print(sitePassword)
    }
}
