"""
덱
https://www.acmicpc.net/problem/10866
"""
import sys

n = int(sys.stdin.readline())
result = []

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push_front": 
        result.insert(0, cmd[1])
    if cmd[0] == "push_back": 
        result.append(cmd[1])
    if cmd[0] == "pop_front": 
        if len(result) == 0:
            print("-1")
        else :
            print(result.pop(0))
    if cmd[0] == "pop_back":  
        if len(result) == 0:
            print("-1")
        else :
            print(result.pop(-1))
    if cmd[0] == "size":
        print(len(result)) 
    if cmd[0] == "empty": 
        if len(result) == 0:
            print("1")
        else :
            print("0")
    if cmd[0] == "front": 
        if len(result) == 0:
            print("-1")
        else :
            print(result[0])
    if cmd[0] == "back":
        if len(result) == 0:
            print("-1")
        else :
            print(result[-1]) 