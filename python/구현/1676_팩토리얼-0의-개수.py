"""
https://www.acmicpc.net/problem/1676
수학
"""

def fa(n) :
    if n <= 0:
        return 1
    
    return n * fa(n-1)

n = int(input())

count = 0
for i in str(fa(n))[::-1]:
    if i == '0':
        count += 1
    if i != '0' :
        break
print(count)

'''
참고 : https://lucian-blog.tistory.com/84
5의 배수를 계산하면 cnt가 나오는걸..

N = int(input())
print(N//5 + N//25 + N//125)

n=int(input())

cnt=0
while n>0:
  cnt+=n//5
  n//=5

print(cnt)
'''