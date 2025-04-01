func solution(_ files:[String]) -> [String] {
    // head, number, tail을 나눈다 2차원 배열
    var hnt: [[String]] = []
    
    for file in files {
        var head = ""
        var number = ""
        var tail = ""
        var idx = file.startIndex

        while idx < file.endIndex, !file[idx].isNumber {
            head.append(file[idx])
            idx = file.index(after: idx)
        }
        
        while idx < file.endIndex, file[idx].isNumber {
            number.append(file[idx])
            idx = file.index(after: idx)
        }
        
        tail = String(file[idx...])
        
        hnt.append([head, number, tail])
    }
    
    // head 정렬, number 정렬, tail 정렬을 실행한다.
    hnt.sort{
        let head1 = $0[0].lowercased()
        let head2 = $1[0].lowercased()
        
        if head1 == head2 {
            let number1 = Int($0[1])!
            let number2 = Int($1[1])!
            return number1 < number2
        } else {
            return head1 < head2
        }
    }
    
    
    // 다시 합쳐서 하나의 1차원 배열로 만든다.
    let result = hnt.map { $0[0] + $0[1] + $0[2] }
    
    return result
}