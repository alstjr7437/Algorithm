'''
https://www.acmicpc.net/problem/17103
'''

# 함수를 이용하니 두번 되므로 무조건 시간초과...
# import math

# def is_prime_num(n):
#     for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
#         if n % i == 0:
#             return False

#     return True

# sosu = []
# for i in range(2, 1_000_001):
#     sosu.append(is_prime_num(i))



sosu = [True for i in range (1000001)]    # 우선 모두 True로 초기화

# 에레토스테네스의 체를 이용하여 소수들 걸러내기
for i in range (2,1001) :
    if sosu[i] :
        for k in range (i*2, 1000001, i):
            sosu[k] = False

# print(sosu)
T = int(input())

#문제 풀이
for i in range(T):
    count = 0
    N = int(input())
    for j in range(2, N//2+1):
        if sosu[j] and sosu[N-j]:
            count += 1
    print(count)