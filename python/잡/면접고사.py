n = int(input())


cnt = 0
for i in range(1, 100):
    if str(n) in str(i):
        cnt += 1

print(cnt)