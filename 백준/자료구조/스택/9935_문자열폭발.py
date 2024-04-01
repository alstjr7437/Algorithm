"""
https://www.acmicpc.net/problem/9935
"""

word = input()
boom = list(input())

result = []

for i in word:
    result.append(i)
    if result[len(result)- len(boom):len(result)] == boom:
        for _ in range(len(boom)):
            result.pop()

if result:
    print("".join(result))
else :
    print("FRULA")

    