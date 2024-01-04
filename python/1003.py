"""
아래와 같이 재귀로 풀면 시간 초과
def fibo(n):
    global result1, result0
    if n == 0 :
        result0 += 1
        return 0
    elif n == 1 :
        result1 += 1
        return 1
    else :
        return fibo(n-1) + fibo(n-2)
    
a = int(input())

for i in range(a):
    result0 = 0
    result1 = 0
    b = int(input())
    fibo(b)
    print(result0, result1)
"""
# 아래와 같이 0과 1의 규칙을 찾아서 진행
# 0은 n-1의 1의 호출과 동일, 1은 n-1의 0과 1의 호출의 합
"""
n = 2일때 부터 생각해보면 각각 0과 1의 호출 횟수는 1 / 1
n = 3일때 f(3) = f(2) + f(1) → 각각 1 / 2
n = 4일때 f(4) = f(3) + f(2) → n이 3일때와 2일때의 더한 합인 2 / 3
n = 5일때 f(5) = f(4) + f(3) → n이 4일때와 3일때의 더한 합인 3 / 5
n = 6 일때 f(6) = f(5) + f(4) → n이 5일때와 4일때의 더한 합인 5 / 8
"""
a = int(input())
 
for _ in range(a):
    result0, result1 = 1,0 
    n = int(input())
    for i in range(n):
        result0, result1 = result1, result0 + result1
 
    print(result0, result1)



    