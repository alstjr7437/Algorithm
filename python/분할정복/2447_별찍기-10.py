"""
별찍기 - 10 
분할정복
https://www.acmicpc.net/problem/2447
"""
"""
잘못 푼 예제 33일때만 중간이 비어지는 
>> 재귀문제를 이렇게 반복문을 사용해서 print를 바로해도 될까?
for i in range(n):
    for j in range(n):
        if i % 3 == 1 and j % 3 == 1 :
            print(" ", end = "")
        else :
            print("*", end="")
    print()
"""
n = int(input())

def star(n):
    result = []
    if n == 1:
        return '*'
    stars = star(n//3)

    for i in stars:
        result.append(i * 3)
    for i in stars:
        result.append(i + ' ' * (n//3) + i)
    for i in stars:
        result.append(i * 3)
    return result

for i in star(n):
    print(i)
    