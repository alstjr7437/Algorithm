"""
이항 계수1
https://www.acmicpc.net/problem/11050
동적계획법 이용

이항계수란? 
뽑거나 안뽑거나 2를 상징하는 이항
전체 집합에서 원소의 개수 n에 대해 k개의 아이템을 뽑는 이항계수
nCk = n! / (n-k)!k!(단, 0 <= k <= n 이면 1)
nCk-> factorial(n)//(factorial(k)*factorial(n-k)) 도 가능
"""

n, k = map(int, input().split())

def fibo(n, k):
    if k == 0 or n == k:
        return 1
    return fibo(n-1, k) + fibo(n-1, k-1)

def fibo2(n):
    if n == 0 :
        return 1
    return n * fibo2(n-1)

print(fibo2(n)// (fibo2(n-k) * fibo2(k)))

# print(fibo(n,k))