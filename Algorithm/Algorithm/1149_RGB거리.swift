//
//  File.swift
//  Algorithm
//
//  Created by KimMinSeok on 4/15/24.
//

import Foundation

func RGB_거리_1149(){
    let n : Int = Int(readLine()!)!
    var homes : [[Int]] = Array(repeating: [], count: n+1)
    
    for i in 0..<n {
        let temp : [Int] = (readLine()?.split(separator: " ").map{ Int($0)! })!
        homes[i] = [temp[0], temp[1], temp[2]]
    }
    
    
    for i in 1..<n {
        homes[i][0] = min(homes[i-1][1], homes[i-1][2]) + homes[i][0]
        homes[i][1] = min(homes[i-1][0], homes[i-1][2]) + homes[i][1]
        homes[i][2] = min(homes[i-1][0], homes[i-1][1]) + homes[i][2]
    }
    
    print(homes[n-1].min()!)
}

        
