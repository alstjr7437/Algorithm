import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    var dict: [String: [(Int, Int)]] = [:]
    var total: [String: Int] = [:]
    
    for i in 0..<genres.count {
        if dict[genres[i]] == nil{
            dict[genres[i]] = [(plays[i], i)]
            total[genres[i]] = plays[i]
        } else {
            dict[genres[i]]!.append((plays[i], i))
            total[genres[i]]! += plays[i]
        }
    }
    
    let sortedTotal = total.sorted { $0.value > $1.value }
    
    for key in dict.keys {
        dict[key]!.sort {
            if $0.0 == $1.0 {
                return $0.1 < $1.1   // 인덱스 작은 순
            }
            return $0.0 > $1.0       // 재생 수 큰 순
        }
    }

    var result: [Int] = []
    
    for (genre, _) in sortedTotal {
        let songs = dict[genre]!
        
        for i in 0..<min(2, songs.count) {
            result.append(songs[i].1)
        }
    }
    
    
    return result
}