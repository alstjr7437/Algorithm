"""
요세푸스 문제
https://www.acmicpc.net/problem/11866
"""

n, k = map(int, input().split())
yosaepoos = []
result = []
a = 0
for i in range(1, n+1):
    yosaepoos.append(i)

while yosaepoos :
    if  a + k - 1 >= len(yosaepoos):
        a = a - len(yosaepoos)
    else : 
        result.append(str(yosaepoos.pop(a + k - 1)))
        a = a + k - 1

print("<" + ", ".join(result) + ">")

# 다시 보니 출력 개이상하게 했네..
# 대신 밑에 대로 하면 str로 안바꿔줘도 됨
# print("<", end = "")
# for i in result:
#     if i == result[-1]:
#         print(i, end="")
#     else :
#         print(i, end=", ")

# print(">")