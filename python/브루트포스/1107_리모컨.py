"""
리모컨
브루트 포스
https://www.acmicpc.net/problem/1107
"""
"""
처음에 생각을 반복문을 이용해서 각 문자열을 비교해주고 계속해서 count를 추가해주는 방식 생각
하지만 틀렸다고 생각해서 인터넷 참고

그리고 런타임 에러 발생
EOFError 예외처리 에러 발생
    m -> error가 없을때 처리를 안해줘서
NameError 발생
    else 부분을 처리해서 error가 없을때도 error 빈배열 안만들어줘서
"""

n = int(input())
m = int(input())
if m != 0:
    error = list(map(int, input().split()))
else : 
    error = []

# 현재 채널에서 + - 만 쓰는 경우
count = abs(100-n)

# 50000이지만 작은수 -> 큰수 / 큰수 -> 작은수가 있기 때문
for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        # 각 숫자가 고장났는지 확인 후 고장 났으면 break로 돌아감
        if int(num[j]) in error:
            break
        # 고장난 숫자 없이 마지막 자리까지 왔으면 min으로 제일 작은거 업데이트
        elif j == len(num) - 1: 
            # 기존답, 번호 누른 횟수 + 해당 번호로부터 타겟까지 차이(+, -)
            count = min(count, len(num) + abs(int(num) - n))
print(count)
