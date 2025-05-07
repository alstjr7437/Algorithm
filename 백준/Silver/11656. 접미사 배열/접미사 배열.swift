let S = readLine()!
var words: [String] = []

for i in 1...S.count {
    words.append(String(S.suffix(i)))
}

words.sort()

for word in words {
    print(word)
}
