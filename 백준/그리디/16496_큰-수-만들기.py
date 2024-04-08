import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

result = []

# 10의자리 수로 만들기
for num in nums:
    temp = []
    while len(temp) < 10 :
        for i in str(num):
            temp.append(i)
            if len(temp) >= 10:
                break
    result.append((temp, str(num)))

sorted_result = sorted(result, key=lambda x: int(''.join(x[0])),reverse=True)

# 정렬 한 결과 문자 만들기
answer = ""
for i in sorted_result:
    answer += i[-1]

# 0인지 보고 출력하기
if int(answer) == 0:
    print(0)
else :
    print(answer)
