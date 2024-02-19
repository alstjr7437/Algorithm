"""
https://www.acmicpc.net/problem/2217

1. 정렬하기
2. 작은거부터 각 개수를 곱해 max_num에 넣기
3. 제일 큰게 max_num보다 크면 제일 큰 밧줄 하나만 하기
"""

n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort()

max_num = 0
for i in range(len(rope)):
    max_num = max(rope[i] * (len(rope) - i), max_num)
print(max_num)