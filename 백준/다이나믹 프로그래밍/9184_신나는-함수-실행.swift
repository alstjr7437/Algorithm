func w(a : Int, b : Int, c : Int) -> Int{
    print(a,b,c)

    if (a <= 0 || b <= 0 || c <= 0){
        return 1
    }else if (a > 20 || b > 20 || c > 20){
        return w(a: 20, b : 20, c : 20)
    }else if (a < b && b < c) {
        print("hell ")
        return  w(a: a, b: b, c:c-1) + w(a : a, b : b-1, c : c-1) - w(a: a, b: b-1, c: c)
    }else {
        return w(a: a-1,b: b, c: c) + w(a: a-1, b:b-1, c:c) + w(a:a-1, b:b, c:c-1) - w(a:a-1, b:b-1,c: c-1)
    }
}

a,b,c = readline()!.split(separator:" ").map { Int(String($0))!}

print(a,b,c)
// var dp = Array(repeating: Array(repeating:0, count: 2))

print(dp)

// print(w(a:2,b:2,c:2))