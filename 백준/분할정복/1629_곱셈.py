a, b, c = map(int, input().split())

def divide(n):
    if n == 1 :
        return a % c
    elif n % 2 == 0:
        return (divide(n//2) ** 2) % c
    else :
        return ((divide(n//2) ** 2)) * a % c
 
print(divide(b))