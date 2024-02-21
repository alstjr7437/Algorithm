"""
https://www.acmicpc.net/problem/20300

1. 정렬을 해준다.
2. 제일 큰수와 제일 작은 수를 더한다
    - 갯수가 홀수면 제일 뒤 큰수는 빼준다
3. 두개를 더한 값을 answer에 넣는다
4. 홀수면 마지막 제일 큰 수를 넣어준다
5. max를 이용해서 근손실이 나타나는 최솟 값을 출력한다.
"""

n = int(input())
t = list(map(int, input().split()))
t.sort()

answer = []
for i in range(n//2):
    if n % 2 == 1:
        answer.append(t[i] + t[n-i-2])
    else :
        answer.append(t[i] + t[n-i-1])
if n % 2 == 1:
    answer.append(t[-1])

print(max(answer))