import Foundation

func solution(_ num_list:[Int]) -> Int {
    let even = num_list.filter { $0 % 2 == 0 }
    let evenNumber = Int(even.map{ String($0) }.joined()) ?? 0
    let odd = num_list.filter { $0 % 2 != 0 }.map(String.init).joined()
    let oddNumber = Int(odd.map{ String($0) }.joined()) ?? 0
    
    return evenNumber + oddNumber
}