for i in 0..<3 {
    let input = Int(readLine()!)
    
    if let input = input {
        let result = input + (3 - i)
        
        if result % 3 == 0 && result % 5 == 0 {
            print("FizzBuzz")
        } else if result % 3 == 0 && result % 5 != 0 {
            print("Fizz")
        } else if result % 3 != 0 && result % 5 == 0 {
            print("Buzz")
        } else {
            print(result)
        }
        
        break
    }
}