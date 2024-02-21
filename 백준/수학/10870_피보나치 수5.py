"""
https://www.acmicpc.net/problem/10870
"""
n = int(input())

def fibo(n):
    if n <= 1  :
        return n
    else :
        return fibo(n-1) + fibo(n-2) 

print(fibo(n))