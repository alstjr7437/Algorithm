import Foundation

func calDate(_ date: Int) -> Int {
    let hour = date / 100
    let minute = date % 100
    return hour * 60 + minute
}

func solution(_ schedules:[Int], _ timelogs:[[Int]], _ startday:Int) -> Int {
    var result = 0
    
    for people in 0..<schedules.count {
        var day = startday
        for time in timelogs[people] {
            if (calDate(schedules[people] + 10) < calDate(time)) && !(day == 6 || day == 7) {
                result += 1
                break
            }
            day += 1
            if day > 7 { day = 1 }
        }
    }
    
    return schedules.count - result
}