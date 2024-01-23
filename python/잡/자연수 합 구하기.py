def sum_all(n):
    print(n)
    if n <= 1 :
        return 1
    else :
        return n + sum_all(n-1)

print(sum_all(5))