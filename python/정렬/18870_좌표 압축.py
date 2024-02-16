"""
https://www.acmicpc.net/problem/18870
"""
import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
arr = sorted(set(X))                                 #a를 set으로 만들고 정렬한, new_a를 생성
dictionary = {arr[i] : i for i in range(len(arr))} #딕셔너리에 '숫자 : new_a에서의 인덱스'로 저장

for i in X:                          #기존 a를 돌며
    print(dictionary[i], end = ' ')  #a[i] key에 해당하는 dictionary의 value를 출력

"""
N = int(input()) 
X = list(map(int, input().split()))
answer = []

# 각 숫자와 인덱스를 리스트에 추가합니다.
for i in range(N):
    answer.append([X[i], i])

# 숫자 기준 정렬
answer.sort(key=lambda x: x[0])

index = -1
prev_num = float('-inf')

# 각 숫자로 index 선정
for i in range(N):
    if answer[i][0] > prev_num:
        index += 1
        prev_num = answer[i][0]
    answer[i][0] = index

# 인덱스 기준 정렬
answer.sort(key=lambda x: x[1])

# 결과 출력
for i in range(N):
    print(answer[i][0], end=" ")
"""