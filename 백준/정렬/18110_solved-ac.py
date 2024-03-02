"""
https://www.acmicpc.net/problem/18110
"""
import sys

input = sys.stdin.readline

def roundUp(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else :
        return int(n)


n = int(input())

if n != 0:

    rank = []
    for i in range(n):
        rank.append(int(input()))

    rank.sort()
    temp = roundUp(n * 0.15)

    print(roundUp(sum(rank[temp:n-temp]) / len(rank[temp:n-temp])))
else :
    print(0)