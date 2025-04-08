struct Heap {
    private var elements: [Int] = []
    
    mutating func insert(node: Int) {
        self.elements.append(node)
        
        var index = elements.count - 1
        while index > 0 {
            let parentIndex = (index - 1) / 2
            if elements[index] > elements[parentIndex] {
                elements.swapAt(index, parentIndex)
                index = parentIndex
            } else {
                break
            }
        }
    }
    
    mutating func remove() -> Int {
        guard !elements.isEmpty else { return 0 }
        if elements.count == 1 {
            return elements.removeFirst()
        }

        let maxValue = elements[0]
        elements[0] = elements.removeLast()
        var index = 0

        while index < elements.count {
            let leftChild = 2 * index + 1
            let rightChild = 2 * index + 2
            var largest = index

            if leftChild < elements.count && elements[leftChild] > elements[largest] {
                largest = leftChild
            }
            if rightChild < elements.count && elements[rightChild] > elements[largest] {
                largest = rightChild
            }

            if largest == index {
                break
            }

            elements.swapAt(index, largest)
            index = largest
        }

        return maxValue
    }
    
}

let N = Int(readLine()!)!
var heap = Heap()

for _ in 0..<N {
    let input = Int(readLine()!)!
    if input == 0 {
        print(heap.remove())
    } else {
        heap.insert(node: input)
    }
}