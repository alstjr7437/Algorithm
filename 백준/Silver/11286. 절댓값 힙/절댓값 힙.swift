struct PriorityQueue {
    var heap: [Int] = []
    
    mutating func push(_ x: Int) {
        heap.append(x)
        siftUp(heap.count - 1)
    }
    
    mutating func pop() -> Int? {
        if heap.isEmpty { return nil }
        
        heap.swapAt(0, heap.count - 1)
        let value = heap.removeLast()
        siftDown(0)
        
        return value
    }
    
    func compare(_ a: Int, _ b: Int) -> Bool {
        if abs(a) == abs(b) {
            return a < b
        }
        return abs(a) < abs(b)
    }
    
    mutating func siftUp(_ index: Int) {
        var child = index
        var parent = (child - 1) / 2
        
        while child > 0 && compare(heap[child], heap[parent]) {
            heap.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }
    
    mutating func siftDown(_ index: Int) {
        var parent = index
        
        while true {
            let left = parent * 2 + 1
            let right = parent * 2 + 2
            var candidate = parent
            
            if left < heap.count && compare(heap[left], heap[candidate]) {
                candidate = left
            }
            
            if right < heap.count && compare(heap[right], heap[candidate]) {
                candidate = right
            }
            
            if candidate == parent { break }
            
            heap.swapAt(parent, candidate)
            parent = candidate
        }
    }
}

let N = Int(readLine()!)!
var pq = PriorityQueue()

for _ in 0..<N {
    let x = Int(readLine()!)!
    
    if x == 0 {
        if let value = pq.pop() {
            print(value)
        } else {
            print(0)
        }
    } else {
        pq.push(x)
    }
}
