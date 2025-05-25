/*
 현재 퍼즐 난이도 - diff
 현재 퍼즐 소요시간 - time_cur
 이전 퍼즐 소요시간 - time_prev
 숙련도 - level
 
 - diff <= level : 퍼즐 틀리지 않고, time_curr만큼 시간 사용
 - diff > level : (diff - level)번 퍼즐을 틀림,
    이 경우, ((diff - level) * time_curr)만큼 시간 사용하고
    time_prev만큼의 시간을 사용해서 이전 퍼즐을 다시 풀고 와야함. (이 경우 무조건 틀리지 않음.)
 - 위 과정 이후, 무조건 time_cur만큼 시간을 사용해서 해결함.
 
 ==> ((time_cur + time_prev) * (diff - level)) + time_cur
 
 전체 제한 시간 limit.
 어떤 level이 퍼즐을 모두 해결하는 최소 레벨일까?
 
 1. 레벨은 무조건 diff의 범위 안에 있음. (왜냐하면 max난이도보다 크면 다 ok임.)
 2. 해당 범위 안에서의 최소값을 찾아야함.
 */


import Foundation

func solution(_ diffs:[Int], _ times:[Int], _ limit:Int64) -> Int {
    
    // ==> ((time_cur + time_prev) * (diff - level)) + time_cur
    func isPossible(level: Int) -> Bool {
        
        var totalTime: Int64 = 0

        for i in 0..<diffs.count {
            let diff = diffs[i]
            let timeCur = times[i]
            let timePrev = (i == 0) ? 0 : times[i - 1]

            if diff <= level {
                totalTime += Int64(timeCur)
            } else {
                let failCount = diff - level
                totalTime += Int64((timeCur + timePrev) * failCount + timeCur)
            }

            if totalTime > limit {
                return false
            }
        }
        return true
    }
    
    var left = 1
    
    // 이 경우 옵셔널 강제 언래핑을 하면 안되는 경우가 뭐지?
    // var right = diffs.max()!
    // 일단 가드문 처리
    guard let maxDiff = diffs.max() else { exit(0) }
    
    var right = maxDiff
    var answer = right

    while left <= right {
        let mid = (left + right) / 2
        if isPossible(level: mid) {
            answer = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return answer
}