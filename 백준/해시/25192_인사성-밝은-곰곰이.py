n = int(input())
gom = set()
result = 0

for i in range(n):
    word = input()

    if word != "ENTER":
        if word not in gom:
            result += 1
            gom.add(word)
    else:
        gom.clear()

print(result)


