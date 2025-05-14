import Foundation

func solution(_ record:[String]) -> [String] {
    var name: [String: String] = [:]
    // 닉네임, 방문 여부(1: 방문 0: 이탈)
    var visited: [String] = []
    
    for current in record {
        // 0: 명령어 1: 아이디 2: 닉네임
        let order = current.split(separator: " ").map { String($0) }
        
        if order[0] == "Enter" {
            visited.append("방문 \(order[1])")
            name[order[1]] = order[2]
        } else if order[0] == "Leave" {
            visited.append("이탈 \(order[1])")
        } else if order[0] == "Change" {
            name[order[1]] = order[2]
        }
    }
    
    var result: [String] = []
    
    for visit in visited {
        let order = visit.split(separator: " ").map { String($0) }
        
        if order[0] == "방문" {
            result.append("\(name[order[1]]!)님이 들어왔습니다.")
        } else if order[0] == "이탈" {
            result.append("\(name[order[1]]!)님이 나갔습니다.")
        }
    }
    
    return result
}