"""
https://www.acmicpc.net/problem/10989
"""
import sys
input = sys.stdin.readline

n = int(input())
answer = [0] * 10001

for i in range(n):
    answer[int(input())] += 1

for i in range(len(answer)):
    if answer[i] != 0:
        for _ in range(answer[i]):
            print(i)
