"""
좌표 정렬하기
https://www.acmicpc.net/problem/11650
"""
n = int(input())
result = []
for i in range(n):
    x, y = map(int, input().split())
    result.append([x,y])

result.sort()

for i in range(n):
    print(result[i][0], result[i][1])