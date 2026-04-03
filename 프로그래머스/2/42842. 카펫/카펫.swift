import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    var xy = brown + yellow
    
    for i in 1..<xy/2 {
        if xy % i == 0 {
            let width = i
            let height = xy / i
            
            // 가로에 *2를 하고 +2 또는(yellow의 높이에따라 +2,4,6 등)
            if (width-2) * (height-2) == yellow {
                return [height, width]
            }
        }
    }
    
    return []
}