//
//  File.swift
//  Algorithm
//
//  Created by KimMinSeok on 4/14/24.
//

import Foundation

func 연결_요소의_개수_11724() {
    let input = readLine()!.split(separator:
                                " ").map{ Int($0)!}

    let n = input[0] , m = input[1]

    var graph : [[Int]] = Array(repeating: [], count: n + 1)
    var visited : [Bool] = Array(repeating: false, count: n + 1)
    var result : Int = 0

    for _ in 0..<m {
        let tmp = readLine()!.split(separator: " ").map { Int($0)!}
        graph[tmp[0]].append(tmp[1])
        graph[tmp[1]].append(tmp[0])
    }

    func bfs1(start: Int){
        visited[start] = true
        var queue: [Int] = [start]
        
        var idx : Int = 0
        
        while queue.count > idx {
            let current = queue[idx]
            
            idx += 1
            for i in graph[current]{
                if visited[i] == false {
                    queue.append(i)
                    visited[i] = true
                }
            }
        }
    }
    
    func bfs2(start: Int){
        visited[start] = true
        var queue: [Int] = [start]
        
        while !queue.isEmpty{
            let current = queue.removeFirst()
            
            for i in graph[current]{
                if visited[i] == false {
                    queue.append(i)
                    visited[i] = true
                }
            }
        }
    }
    
    func bfs3(start: Int){
        visited[start] = true
        var stack1: [Int] = [start]
        
        while !stack1.isEmpty{
            var temp: [Int] = []
            for i in stack1.reversed() { temp.append(i) }
            stack1 = temp
            let current = stack1.removeLast()
            for i in graph[current]{
                if visited[i] == false {
                    stack1.append(i)
                    visited[i] = true
                }
            }
        }
    }
    
    for i in 1...n{
        if visited[i] == false {
            bfs3(start : i)
            result += 1
        }
    }

    print(result)

}
