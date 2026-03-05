let input = readLine()!.split(separator: " ").map { String($0) }

var king = convert(input[0])
var stone = convert(input[1])
let N = Int(input[2])!

for _ in 0..<N {
    let input = readLine()!
    
    let nextKing = move(input, this: king)
    if !isInside(nextKing) { continue }
    
    if nextKing == stone {
        let nextStone = move(input, this: stone)
        if !isInside(nextStone) { continue }
        
        stone = nextStone
    }
    
    king = nextKing
}

print(convertBack(king))
print(convertBack(stone))

func convert(_ s: String) -> [Int] {
    let arr = Array(s)
    var x = 0
    switch arr[0] {
    case "A": x = 1
    case "B": x = 2
    case "C": x = 3
    case "D": x = 4
    case "E": x = 5
    case "F": x = 6
    case "G": x = 7
    case "H": x = 8
    default: x = 0
    }
    let y = Int(String(arr[1]))!
    
    return [x, y]
}

func convertBack(_ pos: [Int]) -> String {
    var x = ""
    switch pos[0] {
    case 1: x = "A"
    case 2: x = "B"
    case 3: x = "C"
    case 4: x = "D"
    case 5: x = "E"
    case 6: x = "F"
    case 7: x = "G"
    case 8: x = "H"
    default: x = ""
    }
    
    return "\(x)\(pos[1])"
}

func move(_ input: String, this: [Int]) -> [Int] {
    var moveStone = this
    
    switch input {
    case "R":
        moveStone[0] += 1
    case "L":
        moveStone[0] -= 1
    case "B":
        moveStone[1] -= 1
    case "T":
        moveStone[1] += 1
    case "RT":
        moveStone[0] += 1
        moveStone[1] += 1
    case "LT":
        moveStone[0] -= 1
        moveStone[1] += 1
    case "RB":
        moveStone[0] += 1
        moveStone[1] -= 1
    case "LB":
        moveStone[0] -= 1
        moveStone[1] -= 1
    default:
        break
    }
    return moveStone
}

func isInside(_ pos: [Int]) -> Bool {
    return pos[0] >= 1 && pos[0] <= 8 && pos[1] >= 1 && pos[1] <= 8
}
