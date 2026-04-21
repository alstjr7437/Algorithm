import Foundation

func solution(_ bridge_length:Int, _ weight:Int, _ truck_weights:[Int]) -> Int {
    var recent = 0
    var stamp: [Int] = []
    var outIndex = 0
    
    var time = 0
    var index = 0
    
    while index < truck_weights.count {
        time += 1
        if stamp.count != 0 {
            if stamp[outIndex] == time {
                recent -= truck_weights[outIndex]
                outIndex += 1
            }
        }
        let current = truck_weights[index] + recent
        if weight >= current {
            recent += truck_weights[index]
            index += 1
            stamp.append(time + bridge_length)
        }
    }
    
    
    return stamp[truck_weights.count - 1]
}