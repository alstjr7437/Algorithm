"""
영화감독 숌
https://www.acmicpc.net/problem/1436
"""
n = int(input())
boom = 666
count = 0

while 1:
    if '666' in str(boom):
        count += 1
    if count == n :
        break
    boom += 1
print(boom)