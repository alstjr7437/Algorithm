from collections import deque

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = int(input())
c = list(map(int, input().split()))

queuestack = deque()

for i in range(n):
    if a[i] == 0:
        queuestack.append(b[i])

for i in c:
    queuestack.appendleft(i)

for i in range(m):
    print(queuestack.pop(), end=" ")


# for i in range(m):
#     for j in range(len(a)):
#         if a[j] == 0 :
#             temp = c[i]
#             c[i] = b[j]
#             b[j] = temp
#             # print(c[i], b)

# for i in range(m):
#     print(i, end=" ")