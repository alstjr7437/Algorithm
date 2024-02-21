"""
랜선 자르기
https://www.acmicpc.net/problem/1654

이분탐색으로 진행
1. start = 1, end = 랜선 길이 중 제일 긴 선
2. start가 end와 같거나 더 커지면 결과 출력
3. 이분탐색인 중간을 나눠서 진행 모든 랜선 값을 mid로 나눠서 몇개의 랜선이 나오는지 확인
4. line이 이상이면 start를 mid + 1
5. line이 이하이면 end를 mid - 1
"""

k, n = map(int, input().split())
sun = [] 

for i in range(k):
    sun.append(int(input()))

start = 1
end = max(sun)

while start <= end :
    line = 0
    mid = (start + end) // 2
    for i in sun:
        line += i // mid
    if line >= n :
        start = mid + 1
    else :
        end = mid - 1
    
print(end)