"""
https://www.acmicpc.net/problem/7568
"""

n = int(input())

weight = []
for i in range(n):
    weight.append(list(map(int,input().split())))

answer = []
for i in range(n):
    rank = 1
    for j in range(n):
        if weight[i][0] < weight[j][0] and weight[i][1] < weight[j][1]:
            rank += 1
    print(rank, end = " ")