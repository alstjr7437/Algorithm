"""
https://www.acmicpc.net/problem/4949
"""

while 1:
    value = input()
    stack = []
    answer = "yes"
    if value == ".":
        break
    for i in value:
        if i == "[" or i == "(" :
            stack.append(i)
        elif i == "]" :
            if not stack or stack.pop() != "[":
                answer = "no"
                break
        elif i == ")" :
            if not stack or stack.pop() != "(" :
                answer = "no"
                break
    if stack :
        answer = "no"
    print(answer)