# 듣보잡 
# 해시
# https://www.acmicpc.net/problem/1764
# 처음에 틀린 이유 : 사전순 정렬도 해주기!!
n, m = map(int, input().split())
result0 = set()
result1 = set()
for _ in range(n):
    result0.add(input())
for _ in range(m):
    result1.add(input())

result = sorted(list(result0 & result1))
print(len(result))
for i in result :
    print(i)
