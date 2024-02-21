"""
https://www.acmicpc.net/problem/2108

"""
import sys

n = int(input())

num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()
print(round(sum(num) / len(num)))
print(num[len(num)//2])

# 빈도수 구하기
num_count=dict()
for i in num:
    if i in num_count:
        num_count[i]+=1
    else:
        num_count[i]=1

max_count = max(num_count.values())
numbers = []

for key, value in num_count.items():
    if value == max_count:
        numbers.append(key)
if len(numbers) > 1:
    print(numbers[1])
else :
    print(numbers[0])

print(max(num) - min(num))