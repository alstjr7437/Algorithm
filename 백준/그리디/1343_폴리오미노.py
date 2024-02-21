"""
https://www.acmicpc.net/problem/1343

count + 4가 XXXX, count + 2 가 XX면 바꾸기
.이면 .추가하기
셋다 아니면 -1로 바꾸고 멈추기(안되는 경우)
"""

n = input()
count = 0
answer = ''

while count < len(n):
    if n[count: count+4] == "XXXX":
        answer += 'AAAA'
        count += 4
    elif n[count: count+2] == "XX":
        answer += 'BB'
        count += 2
    elif n[count] == "." :
        answer += '.'
        count += 1
    else : 
        answer = -1
        break

print(answer)

# n = input()

# board = n.replace("XXXX", "AAAA")
# board = n.replace("XX", "BB")

# if 'X' in n:
#     print(-1)
# else:
#     print(n)